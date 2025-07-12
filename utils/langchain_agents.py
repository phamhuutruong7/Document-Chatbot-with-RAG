from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing import List, Dict, Any, Optional
import os
from .embeddings import get_embeddings
from .pinecone_client import PineconeClient
from .chunker import chunk_text
import json

class DocumentRAGAgent:
    """LangChain agent with RAG-specific tools for document interaction."""
    
    def __init__(self, session_id: str, pinecone_client: PineconeClient):
        self.session_id = session_id
        self.pinecone_client = pinecone_client
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
            temperature=0.1
        )
        self.tools = self._create_tools()
        self.agent = self._create_agent()
    
    def _create_tools(self) -> List[Tool]:
        """Create RAG-specific tools for the agent."""
        
        def search_documents(query: str) -> str:
            """Search through uploaded documents for relevant information."""
            try:
                # Get query embedding
                query_embedding = get_embeddings([query])[0]
                
                # Search in session namespace
                results = self.pinecone_client.query_session_vectors(
                    query_embedding=query_embedding,
                    session_id=self.session_id,
                    top_k=5
                )
                
                if not results or not results.get('matches'):
                    return "SEARCH_RESULT: No relevant documents found in the current session for the query."
                
                # Format results with detailed source information
                formatted_results = []
                for i, match in enumerate(results['matches'], 1):
                    metadata = match.get('metadata', {})
                    text = metadata.get('text', 'No text available')
                    score = match.get('score', 0)
                    doc_name = metadata.get('document_name', 'Unknown')
                    chunk_index = metadata.get('chunk_index', 'Unknown')
                    
                    # Calculate approximate page/section reference
                    page_ref = f"Chunk {chunk_index}" if chunk_index != 'Unknown' else "Unknown location"
                    
                    formatted_results.append(
                        f"[SOURCE {i}]\n"
                        f"Document: {doc_name}\n"
                        f"Location: {page_ref}\n"
                        f"Relevance Score: {score:.3f}\n"
                        f"Content: {text}\n"
                    )
                
                return "SEARCH_RESULT:\n" + "\n---\n".join(formatted_results)
                
            except Exception as e:
                return f"SEARCH_ERROR: Error searching documents: {str(e)}"
        
        def summarize_document_section(query: str) -> str:
            """Summarize specific sections of documents based on a topic or question."""
            try:
                # Search for relevant sections
                search_result = search_documents(query)
                
                if "SEARCH_RESULT: No relevant documents found" in search_result or "SEARCH_ERROR" in search_result:
                    return search_result
                
                # Use LLM to summarize the found sections with strict document-based rules
                summary_prompt = f"""
                CRITICAL INSTRUCTIONS: You must provide a summary STRICTLY based on the document sections provided below. Do not add any information from your general knowledge.
                
                Rules:
                1. Only use information explicitly stated in the document sections
                2. Include source citations for each piece of information: "According to [Document Name, Location]: [information]"
                3. If the documents don't contain enough information about the topic, state: "The uploaded documents contain limited information about this topic"
                4. Do not make assumptions or inferences beyond what is explicitly stated
                
                Topic to summarize: {query}
                
                Document Sections:
                {search_result}
                
                Summary with source citations:
                """
                
                response = self.llm.invoke(summary_prompt)
                return response.content
                
            except Exception as e:
                return f"Error summarizing document section: {str(e)}"
        
        def compare_documents(topic: str) -> str:
            """Compare information across different documents on a specific topic."""
            try:
                # Get query embedding
                query_embedding = get_embeddings([topic])[0]
                
                # Search for more results to compare
                results = self.pinecone_client.query_session_vectors(
                    query_embedding=query_embedding,
                    session_id=self.session_id,
                    top_k=10
                )
                
                if not results or not results.get('matches'):
                    return "No documents found to compare."
                
                # Group by document
                doc_groups = {}
                for match in results['matches']:
                    metadata = match.get('metadata', {})
                    doc_name = metadata.get('document_name', 'Unknown')
                    text = metadata.get('text', '')
                    score = match.get('score', 0)
                    
                    if doc_name not in doc_groups:
                        doc_groups[doc_name] = []
                    doc_groups[doc_name].append((text, score))
                
                if len(doc_groups) < 2:
                    return "Need at least 2 different documents to perform comparison."
                
                # Format comparison data
                comparison_data = []
                for doc_name, chunks in doc_groups.items():
                    # Get best chunk for this document
                    best_chunk = max(chunks, key=lambda x: x[1])
                    comparison_data.append(
                        f"Document: {doc_name}\n"
                        f"Relevant Content: {best_chunk[0][:400]}...\n"
                    )
                
                # Use LLM to compare with strict document-based rules
                comparison_prompt = f"""
                CRITICAL INSTRUCTIONS: Compare the documents STRICTLY based on the content provided below. Do not add any external knowledge.
                
                Rules:
                1. Only compare information explicitly stated in the document sections
                2. Include source citations: "According to [Document Name]: [information]"
                3. If documents don't contain comparable information, state: "The documents do not contain sufficient comparable information on this topic"
                4. Highlight what is explicitly stated vs. what is missing from each document
                
                Topic for comparison: {topic}
                
                {chr(10).join(comparison_data)}
                
                Detailed comparison with source citations:
                """
                
                response = self.llm.invoke(comparison_prompt)
                return response.content
                
            except Exception as e:
                return f"Error comparing documents: {str(e)}"
        
        def get_document_statistics(query: str = "") -> str:
            """Get statistics about the documents in the current session."""
            try:
                stats = self.pinecone_client.get_session_stats(self.session_id)
                
                if not stats:
                    return "No document statistics available for this session."
                
                # Get document names from metadata search
                results = self.pinecone_client.search_by_metadata(
                    filter_dict={"session_id": self.session_id},
                    top_k=100,
                    namespace=self.session_id
                )
                
                doc_names = set()
                chunk_count = 0
                
                if results and results.get('matches'):
                    for match in results['matches']:
                        metadata = match.get('metadata', {})
                        doc_name = metadata.get('document_name')
                        if doc_name:
                            doc_names.add(doc_name)
                        chunk_count += 1
                
                return f"""
                Document Statistics for Current Session:
                - Total Documents: {len(doc_names)}
                - Total Text Chunks: {chunk_count}
                - Document Names: {', '.join(doc_names) if doc_names else 'None'}
                - Vector Count: {stats.get('total_vector_count', 0)}
                """
                
            except Exception as e:
                return f"Error getting document statistics: {str(e)}"
        
        def extract_key_concepts(topic: str = "") -> str:
            """Extract key concepts and themes from the documents."""
            try:
                # Search for relevant content
                if topic:
                    search_result = search_documents(topic)
                else:
                    # Get a sample of documents
                    results = self.pinecone_client.search_by_metadata(
                        filter_dict={"session_id": self.session_id},
                        top_k=10,
                        namespace=self.session_id
                    )
                    
                    if not results or not results.get('matches'):
                        return "No documents found to extract concepts from."
                    
                    # Format sample content
                    sample_content = []
                    for match in results['matches']:
                        metadata = match.get('metadata', {})
                        text = metadata.get('text', '')
                        sample_content.append(text[:300])
                    
                    search_result = "\n---\n".join(sample_content)
                
                # Use LLM to extract concepts with strict document-based rules
                concept_prompt = f"""
                CRITICAL INSTRUCTIONS: Extract key concepts STRICTLY from the document content provided below. Do not add concepts from your general knowledge.
                
                Rules:
                1. Only extract concepts explicitly mentioned or clearly implied in the document content
                2. Include source citations: "According to [Document Name, Location]: [concept/theme]"
                3. If documents contain limited information, state: "The uploaded documents contain limited conceptual information"
                4. Group concepts by source document when possible
                
                Focus area: {topic if topic else "general themes and concepts"}
                
                Content:
                {search_result}
                
                Key Concepts and Themes with source citations:
                """
                
                response = self.llm.invoke(concept_prompt)
                return response.content
                
            except Exception as e:
                return f"Error extracting key concepts: {str(e)}"
        
        # Create tool objects
        tools = [
            Tool(
                name="search_documents",
                description="Search through uploaded documents for information relevant to a query. Returns results with source citations including document name and location. Use this as the primary tool to find specific information in the documents.",
                func=search_documents
            ),
            Tool(
                name="summarize_document_section",
                description="Summarize specific sections of documents based on a topic or question. Provides summaries strictly based on document content with source citations. Use this when you need a concise summary of information about a particular topic.",
                func=summarize_document_section
            ),
            Tool(
                name="compare_documents",
                description="Compare information across different documents on a specific topic. Provides comparisons strictly based on document content with source citations. Use this when you need to analyze similarities and differences between documents.",
                func=compare_documents
            ),
            Tool(
                name="get_document_statistics",
                description="Get statistics about the documents in the current session including document count, chunk count, and document names. Use this to understand what documents are available.",
                func=get_document_statistics
            ),
            Tool(
                name="extract_key_concepts",
                description="Extract key concepts and themes from the documents with source citations. Optionally focus on a specific topic. Provides analysis strictly based on document content. Use this for thematic analysis.",
                func=extract_key_concepts
            )
        ]
        
        return tools
    
    def _create_agent(self) -> AgentExecutor:
        """Create the ReAct agent with RAG tools."""
        
        # Define the prompt template
        prompt_template = """
        You are a document analysis assistant that provides answers STRICTLY based on the uploaded documents. You must follow these rules:
        
        CRITICAL RULES:
        1. ONLY answer based on information found in the documents through tool searches
        2. If information is not found in the documents, explicitly state "This information is not found or mentioned in the uploaded documents"
        3. NEVER guess, assume, or provide information from your general knowledge
        4. ALWAYS cite the specific source (document name and location) for each piece of information
        5. Use the format: "According to [Document Name, Location]: [information]"
        6. If multiple sources support the same information, cite all relevant sources
        
        Available tools:
        {tools}
        
        Use the following format:
        
        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: Based on the document search results, provide your answer with proper source citations. If no relevant information was found, clearly state that the information is not available in the uploaded documents.
        
        Question: {input}
        Thought: {agent_scratchpad}
        """
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["input", "agent_scratchpad"],
            partial_variables={
                "tools": "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools]),
                "tool_names": ", ".join([tool.name for tool in self.tools])
            }
        )
        
        # Create the agent
        agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
        
        # Create agent executor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            max_iterations=5,
            handle_parsing_errors=True
        )
        
        return agent_executor
    
    def query(self, question: str) -> str:
        """Query the agent with a question."""
        try:
            result = self.agent.invoke({"input": question})
            return result.get("output", "No response generated.")
        except Exception as e:
            return f"Error processing query: {str(e)}"
    
    def get_available_tools(self) -> List[str]:
        """Get list of available tool names."""
        return [tool.name for tool in self.tools]