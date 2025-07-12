import os
from typing import Dict, Any, List
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from utils.embeddings import get_embeddings
from utils.file_parser import extract_sections
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LangSmith tracing if configured
if os.getenv("LANGCHAIN_TRACING_V2") == "true":
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    if os.getenv("LANGCHAIN_ENDPOINT"):
        os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
    if os.getenv("LANGCHAIN_API_KEY"):
        os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    if os.getenv("LANGCHAIN_PROJECT"):
        os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

class CommandRouter:
    """
    Router for handling special chatbot commands
    """
    
    def __init__(self):
        """
        Initialize command router
        """
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4"),
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_api_base=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        )
        
        # Define available commands
        self.commands = {
            '/summarize': self.summarize_documents,
            '/list-sections': self.list_sections,
            '/translate': self.translate_content,
            '/clear': self.clear_chat,
            '/help': self.show_help
        }
    
    def handle_command(self, command_input: str, pinecone_client) -> str:
        """
        Handle command input and route to appropriate handler
        
        Args:
            command_input (str): Command string from user
            pinecone_client: Pinecone client instance
            
        Returns:
            str: Command response
        """
        try:
            # Parse command and arguments
            parts = command_input.strip().split()
            command = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
            
            # Check if command exists
            if command in self.commands:
                return self.commands[command](args, pinecone_client)
            else:
                return f"Unknown command: {command}. Type /help for available commands."
                
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    def summarize_documents(self, args: List[str], pinecone_client) -> str:
        """
        Summarize all uploaded documents
        
        Args:
            args (List[str]): Command arguments
            pinecone_client: Pinecone client instance
            
        Returns:
            str: Document summary
        """
        try:
            # Get index statistics
            stats = pinecone_client.get_index_stats()
            total_vectors = stats.get('total_vector_count', 0)
            
            if total_vectors == 0:
                return "No documents have been uploaded yet. Please upload some documents first."
            
            # Query for a sample of document chunks
            dummy_query = "document content summary overview"
            query_embedding = get_embeddings(dummy_query)
            
            # Get more chunks for better summary
            results = pinecone_client.query_vectors(query_embedding, top_k=20)
            
            if not results.get('matches'):
                return "No document content found for summarization."
            
            # Collect document content
            document_texts = []
            filenames = set()
            
            for match in results['matches']:
                metadata = match.get('metadata', {})
                text = metadata.get('text', '')
                filename = metadata.get('filename', 'Unknown')
                
                if text:
                    document_texts.append(text)
                    filenames.add(filename)
            
            # Combine texts for summarization
            combined_text = "\n\n".join(document_texts[:10])  # Limit to avoid token limits
            
            # Create summarization prompt
            prompt = f"""Please provide a comprehensive summary of the following document content:

Document(s): {', '.join(filenames)}

Content:
{combined_text}

Summary:"""
            
            # Get summary from LLM
            response = self.llm.invoke([HumanMessage(content=prompt)])
            
            return f"📄 **Document Summary**\n\n{response.content}\n\n*Based on {len(filenames)} document(s): {', '.join(filenames)}*"
            
        except Exception as e:
            return f"Error generating summary: {str(e)}"
    
    def list_sections(self, args: List[str], pinecone_client) -> str:
        """
        List document sections/headers
        
        Args:
            args (List[str]): Command arguments
            pinecone_client: Pinecone client instance
            
        Returns:
            str: List of document sections
        """
        try:
            # Get index statistics
            stats = pinecone_client.get_index_stats()
            total_vectors = stats.get('total_vector_count', 0)
            
            if total_vectors == 0:
                return "No documents have been uploaded yet. Please upload some documents first."
            
            # Query for document chunks
            dummy_query = "section header title chapter"
            query_embedding = get_embeddings(dummy_query)
            
            results = pinecone_client.query_vectors(query_embedding, top_k=50)
            
            if not results.get('matches'):
                return "No document content found."
            
            # Collect all document texts by filename
            documents_by_file = {}
            
            for match in results['matches']:
                metadata = match.get('metadata', {})
                text = metadata.get('text', '')
                filename = metadata.get('filename', 'Unknown')
                chunk_index = metadata.get('chunk_index', 0)
                
                if filename not in documents_by_file:
                    documents_by_file[filename] = []
                
                documents_by_file[filename].append((chunk_index, text))
            
            # Extract sections for each file
            all_sections = []
            
            for filename, chunks in documents_by_file.items():
                # Sort chunks by index
                chunks.sort(key=lambda x: x[0])
                
                # Combine text from chunks
                combined_text = "\n\n".join([chunk[1] for chunk in chunks])
                
                # Extract sections
                sections = extract_sections(combined_text)
                
                if sections:
                    all_sections.append(f"**{filename}:**")
                    for i, section in enumerate(sections[:20], 1):  # Limit to 20 sections
                        all_sections.append(f"  {i}. {section}")
                    all_sections.append("")  # Empty line between files
            
            if not all_sections:
                return "No clear sections or headers found in the uploaded documents."
            
            return f"📋 **Document Sections**\n\n" + "\n".join(all_sections)
            
        except Exception as e:
            return f"Error listing sections: {str(e)}"
    
    def translate_content(self, args: List[str], pinecone_client) -> str:
        """
        Translate document content to specified language
        
        Args:
            args (List[str]): Command arguments (target language)
            pinecone_client: Pinecone client instance
            
        Returns:
            str: Translation response
        """
        try:
            if not args:
                return "Please specify a target language. Example: /translate vi (for Vietnamese)"
            
            target_language = args[0]
            
            # Language mapping
            language_map = {
                'vi': 'Vietnamese',
                'en': 'English',
                'es': 'Spanish',
                'fr': 'French',
                'de': 'German',
                'zh': 'Chinese',
                'ja': 'Japanese',
                'ko': 'Korean'
            }
            
            full_language = language_map.get(target_language.lower(), target_language)
            
            # Get index statistics
            stats = pinecone_client.get_index_stats()
            total_vectors = stats.get('total_vector_count', 0)
            
            if total_vectors == 0:
                return "No documents have been uploaded yet. Please upload some documents first."
            
            # Query for document content
            dummy_query = "main content important information"
            query_embedding = get_embeddings(dummy_query)
            
            results = pinecone_client.query_vectors(query_embedding, top_k=5)
            
            if not results.get('matches'):
                return "No document content found for translation."
            
            # Get sample content for translation
            sample_texts = []
            for match in results['matches'][:3]:  # Limit to 3 chunks
                metadata = match.get('metadata', {})
                text = metadata.get('text', '')
                if text:
                    sample_texts.append(text[:500])  # Limit text length
            
            if not sample_texts:
                return "No text content found for translation."
            
            combined_text = "\n\n".join(sample_texts)
            
            # Create translation prompt
            prompt = f"""Please translate the following text to {full_language}:

{combined_text}

Translation:"""
            
            # Get translation from LLM
            response = self.llm.invoke([HumanMessage(content=prompt)])
            
            return f"🌐 **Translation to {full_language}**\n\n{response.content}\n\n*Note: This is a sample translation of the document content.*"
            
        except Exception as e:
            return f"Error translating content: {str(e)}"
    
    def clear_chat(self, args: List[str], pinecone_client) -> str:
        """
        Clear chat history (handled in main app)
        
        Args:
            args (List[str]): Command arguments
            pinecone_client: Pinecone client instance
            
        Returns:
            str: Clear confirmation
        """
        return "Chat history will be cleared."
    
    def show_help(self, args: List[str], pinecone_client) -> str:
        """
        Show available commands
        
        Args:
            args (List[str]): Command arguments
            pinecone_client: Pinecone client instance
            
        Returns:
            str: Help text
        """
        help_text = """🔧 **Available Commands:**

• `/summarize` - Generate a summary of all uploaded documents
• `/list-sections` - List section headers from uploaded documents
• `/translate [lang]` - Translate content to specified language
  - Examples: `/translate vi` (Vietnamese), `/translate es` (Spanish)
• `/clear` - Clear chat history
• `/help` - Show this help message

**Supported Languages for Translation:**
- vi (Vietnamese), en (English), es (Spanish)
- fr (French), de (German), zh (Chinese)
- ja (Japanese), ko (Korean)

**Usage Tips:**
- Upload documents first before using commands
- Commands are case-insensitive
- Use regular questions for document Q&A"""
        
        return help_text