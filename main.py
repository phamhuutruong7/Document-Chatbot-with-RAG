import streamlit as st
import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from utils.file_parser import parse_file
from utils.chunker import chunk_text
from utils.embeddings import get_embeddings, get_batch_embeddings
from utils.pinecone_client import PineconeClient
from utils.commands import CommandRouter
from utils.session_manager import SessionManager
from utils.rag_tracer import RAGTracer
from utils.langchain_agents import DocumentRAGAgent
from utils.config import load_config, validate_config
from utils.decorators import (
    handle_errors, log_execution_time, streamlit_spinner,
    log_user_action, validate_inputs, is_non_empty_string,
    is_valid_file_size, is_valid_file_extension
)
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load environment variables
load_dotenv()

# Load and validate configuration
try:
    config = load_config()
    config_issues = validate_config(config)
    if config_issues:
        st.error("Configuration Issues:")
        for issue in config_issues:
            st.error(f"• {issue}")
        st.stop()
except Exception as e:
    st.error(f"Failed to load configuration: {e}")
    st.stop()

# Initialize LangSmith tracing if configured
if config.langsmith.tracing and config.langsmith.api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = config.langsmith.endpoint or "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = config.langsmith.api_key
    if config.langsmith.project:
        os.environ["LANGCHAIN_PROJECT"] = config.langsmith.project
    print("✅ LangSmith tracing enabled")
else:
    print("ℹ️ LangSmith tracing disabled")

# Initialize session state components
@st.cache_resource
def get_pinecone_client():
    return PineconeClient()

@st.cache_resource
def get_session_manager():
    return SessionManager(config.data_dir)

@st.cache_resource
def get_rag_tracer():
    return RAGTracer(config.data_dir)

@st.cache_resource
def get_command_router():
    return CommandRouter()

# Initialize core components
if 'pinecone_client' not in st.session_state:
    st.session_state.pinecone_client = get_pinecone_client()
if 'session_manager' not in st.session_state:
    st.session_state.session_manager = get_session_manager()
if 'rag_tracer' not in st.session_state:
    st.session_state.rag_tracer = get_rag_tracer()
if 'command_router' not in st.session_state:
    st.session_state.command_router = get_command_router()

# Initialize session-specific components
if 'current_session_id' not in st.session_state:
    st.session_state.current_session_id = None
if 'rag_agent' not in st.session_state:
    st.session_state.rag_agent = None
if 'llm' not in st.session_state:
    st.session_state.llm = ChatOpenAI(
        model=config.openai.model,
        temperature=config.openai.temperature,
        api_key=config.openai.api_key,
        base_url=config.openai.base_url,
        max_tokens=config.openai.max_tokens
    )

@handle_errors()
@log_execution_time
def initialize_session(session_id: Optional[str] = None) -> str:
    """Initialize or load a chat session"""
    session_manager = st.session_state.session_manager
    
    if session_id:
        # Load existing session
        session_data = session_manager.get_session(session_id)
        if session_data:
            st.session_state.current_session_id = session_id
            # Initialize RAG agent for this session
            st.session_state.rag_agent = DocumentRAGAgent(
                session_id=session_id,
                pinecone_client=st.session_state.pinecone_client
            )
            return session_id
    
    # Create new session
    new_session_id = session_manager.create_new_session()
    st.session_state.current_session_id = new_session_id
    st.session_state.rag_agent = DocumentRAGAgent(
        session_id=new_session_id,
        pinecone_client=st.session_state.pinecone_client
    )
    return new_session_id

@handle_errors()
def get_current_chat_history() -> List[Dict[str, Any]]:
    """Get simple chat history from session state"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    return st.session_state.chat_history

@handle_errors()
def save_current_chat_history(history: List[Dict[str, Any]]):
    """Save simple chat history to session state"""
    st.session_state.chat_history = history

@handle_errors()
@log_execution_time
@streamlit_spinner("Processing uploaded file...")
@log_user_action()
@validate_inputs([
    (lambda f: f is not None, "File must be provided"),
    (lambda f: is_valid_file_size(f, config.file_upload.max_size_mb), 
     f"File size must be less than {config.file_upload.max_size_mb}MB"),
    (lambda f: is_valid_file_extension(f.name, config.file_upload.allowed_extensions),
     f"File type must be one of: {', '.join(config.file_upload.allowed_extensions)}")
])
def process_uploaded_file(uploaded_file) -> bool:
    """Process uploaded file and store in Pinecone with session management"""
    if not st.session_state.current_session_id:
        st.error("No active session. Please start a new session first.")
        return False
    
    # Parse the file
    content = parse_file(uploaded_file)
    if not content:
        st.error("Could not extract content from the file.")
        return False
    
    # Chunk the content
    chunks = chunk_text(
        content,
        chunk_size=config.chunking.chunk_size,
        chunk_overlap=config.chunking.chunk_overlap
    )
    if not chunks:
        st.error("Could not create chunks from the content.")
        return False
    
    # Create embeddings and store in Pinecone with session context
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Batch process embeddings for better performance
        batch_size = 10
        vectors = []
        
        for batch_start in range(0, len(chunks), batch_size):
            batch_end = min(batch_start + batch_size, len(chunks))
            batch_chunks = chunks[batch_start:batch_end]
            
            # Update progress
            progress = batch_end / len(chunks)
            progress_bar.progress(progress)
            status_text.text(f"Processing chunks {batch_start + 1}-{batch_end} of {len(chunks)}...")
            
            # Get batch embeddings
            batch_embeddings = get_batch_embeddings(batch_chunks)
            
            for i, (chunk, embedding) in enumerate(zip(batch_chunks, batch_embeddings)):
                if embedding:
                    chunk_index = batch_start + i
                    vectors.append({
                        'id': f"{st.session_state.current_session_id}_{uploaded_file.name}_{chunk_index}",
                        'values': embedding,
                        'metadata': {
                            'text': chunk,
                            'source': uploaded_file.name,
                            'chunk_index': chunk_index,
                            'session_id': st.session_state.current_session_id,
                            'timestamp': datetime.now().isoformat(),
                            'file_size': len(content),
                            'chunk_size': len(chunk)
                        }
                    })
        
        progress_bar.progress(1.0)
        status_text.text("Storing vectors in Pinecone...")
        
        if vectors:
            # Extract texts and embeddings from vectors
            texts = [v['metadata']['text'] for v in vectors]
            embeddings = [v['values'] for v in vectors]
            
            success = st.session_state.pinecone_client.create_session_vectors(
                texts=texts,
                embeddings=embeddings,
                session_id=st.session_state.current_session_id,
                document_name=uploaded_file.name
            )
            if success:
                # Update session metadata
                session_data = st.session_state.session_manager.get_session(
                    st.session_state.current_session_id
                )
                if session_data:
                    documents = session_data.get('documents', [])
                    documents.append({
                        'filename': uploaded_file.name,
                        'chunks_count': len(vectors),
                        'file_size': len(content),
                        'upload_time': datetime.now().isoformat()
                    })
                    st.session_state.session_manager.update_session(
                        st.session_state.current_session_id,
                        documents=documents
                    )
                
                progress_bar.empty()
                status_text.empty()
                st.success(f"Successfully processed {uploaded_file.name} with {len(vectors)} chunks.")
                return True
            else:
                st.error("Failed to store vectors in Pinecone.")
                return False
        else:
            st.error("No valid embeddings were created.")
            return False
            
    finally:
        progress_bar.empty()
        status_text.empty()

@handle_errors()
@log_execution_time
@validate_inputs([
    (lambda q: is_non_empty_string(q), "Query must be a non-empty string")
])
def get_response(query: str) -> str:
    """Get response using RAG with tracing and agent integration"""
    if not st.session_state.current_session_id:
        return "No active session. Please start a new session first."
    
    if not st.session_state.rag_agent:
        return "RAG agent not initialized. Please start a new session."
    
    # Start RAG tracing
    trace_id = st.session_state.rag_tracer.start_operation(
        query=query,
        session_id=st.session_state.current_session_id,
        model="gpt-4",
        embedding_model="text-embedding-ada-002"
    )
    
    try:
        # Check if it's a command
        if query.startswith('/'):
            return st.session_state.command_router.handle_command(
                query, st.session_state.pinecone_client
            )
        
        # Check if query looks like it needs agent tools
        agent_keywords = [
            'summarize', 'summary', 'compare', 'comparison', 'statistics', 
            'stats', 'key concepts', 'main points', 'overview', 'analyze'
        ]
        
        use_agent = any(keyword in query.lower() for keyword in agent_keywords)
        
        if use_agent:
            # Use LangChain agent for complex queries
            st.session_state.rag_tracer.start_retrieval(trace_id)
            
            try:
                response = st.session_state.rag_agent.query(query)
                
                st.session_state.rag_tracer.end_retrieval(
                    trace_id, 
                    chunks=[],  # Agent handles this internally
                    scores=[]
                )
                
                st.session_state.rag_tracer.start_generation(trace_id)
                st.session_state.rag_tracer.end_generation(
                    trace_id,
                    response=response
                )
                
                return response
                
            except Exception as e:
                st.warning(f"Agent failed, falling back to standard RAG: {e}")
                use_agent = False
        
        if not use_agent:
            # Standard RAG pipeline with tracing
            st.session_state.rag_tracer.start_retrieval(trace_id)
            
            # Get relevant chunks from Pinecone
            query_embedding = get_embeddings(query)
            relevant_chunks = st.session_state.pinecone_client.query_vectors(
                query_embedding, 
                top_k=config.rag.top_k,
                namespace=st.session_state.current_session_id
            )
            
            if not relevant_chunks or 'matches' not in relevant_chunks:
                st.session_state.rag_tracer.complete_operation(trace_id)
                return "I couldn't find relevant information in the uploaded documents. Please make sure you've uploaded some documents first."
            
            # Extract context and scores
            context_chunks = []
            scores = []
            
            for match in relevant_chunks['matches']:
                if 'metadata' in match and 'text' in match['metadata']:
                    context_chunks.append(match['metadata']['text'])
                    scores.append(match.get('score', 0.0))
            
            if not context_chunks:
                st.session_state.rag_tracer.complete_operation(trace_id)
                return "I couldn't find relevant information in the uploaded documents."
            
            st.session_state.rag_tracer.end_retrieval(
                trace_id, 
                chunks=context_chunks,
                scores=scores
            )
            
            # Combine context
            context = "\n\n".join(context_chunks[:config.rag.max_context_chunks])
            
            # Create prompt
            prompt = f"""Based on the following context from uploaded documents, please answer the question.
            
Context:
{context}
            
Question: {query}
            
Please provide a comprehensive answer based on the context. If the context doesn't contain enough information to fully answer the question, please mention what information is missing.
            
Answer:"""
            
            # Get response from LLM
            st.session_state.rag_tracer.start_generation(trace_id)
            
            response = st.session_state.llm.invoke([HumanMessage(content=prompt)])
            
            response_text = response.content
            
            st.session_state.rag_tracer.end_generation(
                trace_id,
                response=response_text
            )
            
            return response_text
    
    except Exception as e:
        st.session_state.rag_tracer.complete_operation(trace_id)
        return f"Error generating response: {str(e)}"
    
    finally:
        st.session_state.rag_tracer.complete_operation(trace_id)

@handle_errors()
def render_session_sidebar():
    """Render session management sidebar"""
    st.sidebar.header("🔄 Session Management")
    
    # Current session info
    if st.session_state.current_session_id:
        st.sidebar.success(f"Active Session: {st.session_state.current_session_id[:8]}...")
        
        # Session statistics
        session_data = st.session_state.session_manager.get_session(
            st.session_state.current_session_id
        )
        if session_data:
            docs_count = len(session_data.get('documents', []))
            chat_count = len(session_data.get('chat_history', []))
            st.sidebar.info(f"📄 Documents: {docs_count} | 💬 Messages: {chat_count}")
    else:
        st.sidebar.warning("No active session")
    
    # Session controls
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("🆕 New Session", key="new_session_btn", use_container_width=True):
            new_session_id = initialize_session()
            st.sidebar.success(f"Created session: {new_session_id[:8]}...")
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear Session", key="clear_session_btn", use_container_width=True):
            if st.session_state.current_session_id:
                # Clear session data including Pinecone vectors
                st.session_state.pinecone_client.clear_session_data(
                    st.session_state.current_session_id
                )
                st.session_state.session_manager.delete_session(
                    st.session_state.current_session_id
                )
                st.session_state.current_session_id = None
                st.session_state.rag_agent = None
                st.sidebar.success("Session cleared!")
                st.rerun()
    
    # Load existing session
    sessions = st.session_state.session_manager.list_sessions()
    if sessions:
        st.sidebar.subheader("📋 Load Session")
        session_options = {f"{s['id'][:8]}... ({s['created_at'][:10]})": s['id'] for s in sessions}
        
        selected_session = st.sidebar.selectbox(
            "Select session to load:",
            options=list(session_options.keys()),
            index=None,
            placeholder="Choose a session..."
        )
        
        if selected_session and st.sidebar.button("📂 Load Selected", key="load_session_btn"):
            session_id = session_options[selected_session]
            initialize_session(session_id)
            st.sidebar.success(f"Loaded session: {session_id[:8]}...")
            st.rerun()

@handle_errors()
def render_rag_metrics():
    """Render RAG performance metrics"""
    if not st.session_state.current_session_id:
        return
    
    # Get performance statistics (returns dict)
    stats = st.session_state.rag_tracer.get_performance_stats(
        st.session_state.current_session_id
    )
    
    if not stats:
        return
    
    with st.expander("📊 RAG Performance Metrics", expanded=False):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Queries", stats['total_queries'])
        with col2:
            st.metric("Avg Retrieval Time", f"{stats['avg_retrieval_time']:.2f}s")
        with col3:
            st.metric("Avg Generation Time", f"{stats['avg_generation_time']:.2f}s")
        with col4:
            st.metric("Avg Total Time", f"{stats['avg_total_time']:.2f}s")
        
        # Get raw metrics for chart
        raw_metrics = st.session_state.rag_tracer.get_session_metrics(
            st.session_state.current_session_id
        )
        
        # Performance chart
        if len(raw_metrics) > 1:
            df = pd.DataFrame(raw_metrics)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            fig = px.line(
                df, x='timestamp', y='total_time',
                title='Query Response Time Over Time',
                labels={'total_time': 'Response Time (s)', 'timestamp': 'Time'}
            )
            st.plotly_chart(fig, use_container_width=True)

def main():
    st.set_page_config(
        page_title="Document Chat Assistant",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Clean and minimal CSS styling
    st.markdown("""
    <style>
    /* Clean, minimal styling for better UX */
    .stApp {
        background: #f8f9fa;
    }
    
    .main .block-container {
        padding-top: 1rem;
        background: white;
        border-radius: 8px;
        margin-top: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        max-width: 1200px;
    }
    
    /* Simple header styling */
    .main-header {
        background: #ffffff;
        color: #333;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 1.5rem;
        border: 1px solid #e9ecef;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
        color: #6c757d;
    }
    
    /* Simple metric cards */
    .metric-card {
        background: #ffffff;
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid #e9ecef;
        margin: 0.5rem 0;
    }
    
    /* Clean chat container */
    .chat-container {
        background: #ffffff;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    
    /* Simple chat messages */
    .stChatMessage {
        border-radius: 6px;
        margin: 0.5rem 0;
    }
    
    /* Clean sidebar sections */
    .sidebar-section {
        background: #ffffff;
        padding: 1rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        border: 1px solid #e9ecef;
    }
    
    /* Simple buttons */
    .stButton > button {
        border-radius: 6px;
        border: 1px solid #dee2e6;
        background: #ffffff;
        color: #495057;
        font-weight: 500;
        transition: all 0.2s ease;
        padding: 0.5rem 1rem;
    }
    
    .stButton > button:hover {
        background: #f8f9fa;
        border-color: #adb5bd;
    }
    
    /* Primary buttons */
    .stButton > button[kind="primary"] {
        background: #007bff;
        color: white;
        border-color: #007bff;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: #0056b3;
        border-color: #0056b3;
    }
    
    /* Simple file uploader */
    .stFileUploader {
        border: 2px dashed #dee2e6;
        border-radius: 6px;
        padding: 1rem;
        background: #ffffff;
    }
    
    .stFileUploader:hover {
        border-color: #adb5bd;
    }
    
    /* Clean expander */
    .streamlit-expanderHeader {
        background: #f8f9fa;
        border-radius: 4px;
        font-weight: 500;
    }
    
    /* Subtle messages */
    .stSuccess {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 6px;
        padding: 0.75rem;
    }
    
    .stError {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 6px;
        padding: 0.75rem;
    }
    
    .stInfo {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 6px;
        padding: 0.75rem;
    }
    
    /* Simple progress bar */
    .stProgress > div > div {
        background: #007bff;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 1.5rem;
        }
        
        .main .block-container {
            padding: 0.5rem;
        }
        
        .chat-container {
            padding: 0.75rem;
        }
        
        .sidebar-section {
            padding: 0.75rem;
        }
    }
    
    /* Clean scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f8f9fa;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #dee2e6;
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #adb5bd;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 0.75rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    .warning-message {
        background: #fff3cd;
        color: #856404;
        padding: 0.75rem;
        border-radius: 5px;
        border: 1px solid #ffeaa7;
    }
    .info-badge {
        background: #e3f2fd;
        color: #1565c0;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Enhanced header
    st.markdown("""
    <div class="main-header">
        <h1>📚 Document Chat Assistant</h1>
        <p>Intelligent document analysis with AI-powered conversations and advanced RAG capabilities</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session if none exists
    if not st.session_state.current_session_id:
        initialize_session()
    
    # Enhanced Sidebar
    with st.sidebar:
        # Session Management Section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        render_session_sidebar()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # File Upload Section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("### 📁 Upload Documents")
        
        # Show upload tips
        with st.expander("📋 Upload Guidelines", expanded=False):
            st.markdown(f"""
            **Supported formats:** {', '.join(config.file_upload.allowed_extensions)}
            
            **Max file size:** {config.file_upload.max_size_mb}MB
            
            **Tips:**
            - PDF files work best for text extraction
            - Ensure documents have clear, readable text
            - Multiple documents can be uploaded per session
            """)
        
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=config.file_upload.allowed_extensions,
            help=f"Upload files up to {config.file_upload.max_size_mb}MB"
        )
        
        if uploaded_file is not None:
            st.info(f"📄 Selected: {uploaded_file.name} ({uploaded_file.size:,} bytes)")
            if st.button("📤 Process File", key="process_file_btn", use_container_width=True, type="primary"):
                success = process_uploaded_file(uploaded_file)
                if success:
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick Actions Section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("### ⚡ Quick Actions")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🧹 Clear Chat", key="clear_chat_btn", use_container_width=True):
                if st.session_state.current_session_id:
                    save_current_chat_history([])
                    st.success("Chat cleared!")
                    st.rerun()
        
        with col2:
            if st.button("📊 Show Stats", key="show_stats_btn", use_container_width=True):
                if st.session_state.current_session_id:
                    st.session_state.show_stats = True
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Commands Help Section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        with st.expander("🔧 Available Commands", expanded=False):
            st.markdown("""
            **Chat Commands:**
            - `/clear` - Clear chat history
            - `/help` - Show help information
            - `/status` - Show system status
            - `/stats` - Show document statistics
            - `/summary` - Get session summary
            
            **Agent Keywords:**
            Use these words to trigger advanced analysis:
            - "summarize", "summary"
            - "compare", "comparison" 
            - "statistics", "stats"
            - "key concepts", "main points"
            - "overview", "analyze"
            """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content area with enhanced layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Chat container with styling
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # Chat header with session info
        if st.session_state.current_session_id:
            session_data = st.session_state.session_manager.get_session(
                st.session_state.current_session_id
            )
            docs_count = len(session_data.get('documents', [])) if session_data else 0
            
            st.markdown(f"""
            <div style="background: #e3f2fd; padding: 0.5rem; border-radius: 5px; margin-bottom: 1rem;">
                💬 <strong>Chat Session:</strong> {st.session_state.current_session_id[:8]}... 
                | 📄 <strong>Documents:</strong> {docs_count}
                | 🤖 <strong>AI Mode:</strong> Advanced RAG + Agent
            </div>
            """, unsafe_allow_html=True)
        
        # Display chat history with enhanced styling
        chat_history = get_current_chat_history()
        
        if not chat_history:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #666;">
                <h3>👋 Welcome to Document Chat!</h3>
                <p>Upload documents using the sidebar and start asking questions.</p>
                <p><strong>Try asking:</strong></p>
                <ul style="text-align: left; display: inline-block;">
                    <li>"Summarize the main points"</li>
                    <li>"What are the key concepts?"</li>
                    <li>"Compare different sections"</li>
                    <li>"Show document statistics"</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        for i, message in enumerate(chat_history):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
                # Add timestamp for messages
                if "timestamp" in message:
                    st.caption(f"⏰ {message['timestamp']}")
        
        # Enhanced chat input with suggestions
        st.markdown("### 💭 Ask a Question")
        
        # Quick suggestion buttons
        if docs_count > 0:
            st.markdown("**Quick suggestions:**")
            suggestion_cols = st.columns(4)
            
            suggestions = [
                "📝 Summarize documents",
                "🔍 Key concepts", 
                "📊 Document stats",
                "🔄 Compare content"
            ]
            
            for i, (col, suggestion) in enumerate(zip(suggestion_cols, suggestions)):
                with col:
                    if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                        # Auto-fill the chat input based on suggestion
                        if i == 0:
                            prompt = "Please provide a comprehensive summary of all uploaded documents"
                        elif i == 1:
                            prompt = "Extract the key concepts and main themes from the documents"
                        elif i == 2:
                            prompt = "/stats"
                        else:
                            prompt = "Compare the main topics across different documents"
                        
                        # Process the suggestion
                        chat_history.append({"role": "user", "content": prompt, "timestamp": datetime.now().strftime("%H:%M:%S")})
                        with st.chat_message("user"):
                            st.markdown(prompt)
                        
                        with st.chat_message("assistant"):
                            with st.spinner("🤔 Analyzing documents..."):
                                response = get_response(prompt)
                                st.markdown(response)
                        
                        chat_history.append({"role": "assistant", "content": response, "timestamp": datetime.now().strftime("%H:%M:%S")})
                        save_current_chat_history(chat_history)
                        st.rerun()
        
        # Chat input
        if prompt := st.chat_input("💬 Ask anything about your documents...", key="main_chat_input"):
            # Add user message to chat history with timestamp
            chat_history.append({
                "role": "user", 
                "content": prompt,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            with st.chat_message("user"):
                st.markdown(prompt)
                st.caption(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
            
            # Get and display assistant response
            with st.chat_message("assistant"):
                with st.spinner("🤔 Analyzing and generating response..."):
                    response = get_response(prompt)
                    st.markdown(response)
                    st.caption(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
            
            # Add assistant response to chat history with timestamp
            chat_history.append({
                "role": "assistant", 
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            
            # Save chat history
            save_current_chat_history(chat_history)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Enhanced right sidebar
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        
        # RAG metrics with enhanced display
        if st.session_state.current_session_id:
            st.markdown("---")
            st.markdown("### 📊 Performance Metrics")
            render_rag_metrics()
            
            # Additional session insights
            session_data = st.session_state.session_manager.get_session(
                st.session_state.current_session_id
            )
            
            if session_data:
                st.markdown("---")
                st.markdown("### 📈 Session Insights")
                
                # Chat statistics
                chat_history = get_current_chat_history()
                total_messages = len(chat_history)
                user_messages = len([m for m in chat_history if m['role'] == 'user'])
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("💬 Total Messages", total_messages)
                with col_b:
                    st.metric("❓ Questions Asked", user_messages)
                
                # Document info
                docs = session_data.get('documents', [])
                if docs:
                    st.markdown("**📄 Uploaded Documents:**")
                    for i, doc in enumerate(docs[:3]):  # Show first 3
                        st.markdown(f"• {doc.get('filename', f'Document {i+1}')}")
                    if len(docs) > 3:
                        st.markdown(f"• ... and {len(docs) - 3} more")
                
                # Quick actions
                st.markdown("---")
                st.markdown("### ⚡ Quick Actions")
                
                action_col1, action_col2 = st.columns(2)
                with action_col1:
                    if st.button("🔄 Refresh", key="refresh_btn", use_container_width=True):
                        st.rerun()
                
                with action_col2:
                    if st.button("📋 Export Chat", key="export_chat_btn", use_container_width=True):
                        if chat_history:
                            # Create exportable chat format
                            export_text = f"Chat Export - Session: {st.session_state.current_session_id}\n"
                            export_text += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                            
                            for msg in chat_history:
                                role = "User" if msg['role'] == 'user' else "Assistant"
                                timestamp = msg.get('timestamp', 'N/A')
                                export_text += f"[{timestamp}] {role}: {msg['content']}\n\n"
                            
                            st.download_button(
                                label="💾 Download Chat",
                                data=export_text,
                                file_name=f"chat_export_{st.session_state.current_session_id[:8]}.txt",
                                mime="text/plain",
                                use_container_width=True
                            )
                        else:
                            st.info("No chat history to export")
                
                # Session documents
                if session_data.get('documents'):
                    st.markdown("---")
                    with st.expander("📄 Session Documents", expanded=True):
                        for doc in session_data['documents']:
                            st.write(f"**{doc['filename']}**")
                            st.caption(f"Chunks: {doc['chunks_count']} | Size: {doc['file_size']} bytes")
                            st.caption(f"Uploaded: {doc['upload_time'][:19]}")
                            st.divider()
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()