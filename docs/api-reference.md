# 📚 API Reference

## Overview

This document provides comprehensive technical documentation for the Document Chatbot's internal APIs, functions, classes, and interfaces. This reference is intended for developers who want to understand, extend, or integrate with the application.

## 🏗️ Core Architecture

### Main Application (`main.py`)

The main Streamlit application entry point.

#### Functions

##### `main()`
```python
def main() -> None:
    """Main application entry point."""
```
**Description**: Initializes and runs the Streamlit application.

**Returns**: None

**Side Effects**:
- Sets up Streamlit page configuration
- Initializes session state
- Renders the main UI

##### `initialize_session()`
```python
def initialize_session() -> None:
    """Initialize session state variables."""
```
**Description**: Sets up default values for Streamlit session state.

**Session State Variables**:
- `messages`: List of chat messages
- `session_id`: Unique session identifier
- `documents`: List of uploaded documents
- `rag_agent`: RAG agent instance

##### `handle_file_upload(uploaded_file: UploadedFile) -> bool`
```python
def handle_file_upload(uploaded_file: UploadedFile) -> bool:
    """Process uploaded file and add to knowledge base."""
```
**Parameters**:
- `uploaded_file` (UploadedFile): Streamlit uploaded file object

**Returns**: 
- `bool`: True if processing successful, False otherwise

**Raises**:
- `ValueError`: If file format is unsupported
- `FileSizeError`: If file exceeds size limit

##### `process_user_input(user_input: str) -> str`
```python
def process_user_input(user_input: str) -> str:
    """Process user input and generate response."""
```
**Parameters**:
- `user_input` (str): User's question or command

**Returns**:
- `str`: AI-generated response

**Raises**:
- `APIError`: If external API call fails
- `RateLimitError`: If rate limit exceeded

## 🔧 Configuration Module (`utils/config.py`)

### Classes

#### `OpenAIConfig`
```python
class OpenAIConfig(BaseModel):
    """OpenAI API configuration."""
    api_key: str
    model: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 1000
    timeout: int = 30
```

**Attributes**:
- `api_key` (str): OpenAI API key
- `model` (str): Model name (default: "gpt-4")
- `temperature` (float): Response creativity (0.0-2.0)
- `max_tokens` (int): Maximum response tokens
- `timeout` (int): Request timeout in seconds

#### `PineconeConfig`
```python
class PineconeConfig(BaseModel):
    """Pinecone vector database configuration."""
    api_key: str
    environment: str
    index_name: str
    namespace: str = "default"
    timeout: int = 30
```

**Attributes**:
- `api_key` (str): Pinecone API key
- `environment` (str): Pinecone environment
- `index_name` (str): Index name
- `namespace` (str): Namespace for data isolation
- `timeout` (int): Request timeout in seconds

#### `EmbeddingConfig`
```python
class EmbeddingConfig(BaseModel):
    """Embedding model configuration."""
    provider: str = "openai"
    model: str = "text-embedding-ada-002"
    dimensions: int = 1536
    batch_size: int = 100
```

**Attributes**:
- `provider` (str): Embedding provider
- `model` (str): Embedding model name
- `dimensions` (int): Embedding vector dimensions
- `batch_size` (int): Batch size for embedding

#### `ChunkingConfig`
```python
class ChunkingConfig(BaseModel):
    """Text chunking configuration."""
    chunk_size: int = 1000
    chunk_overlap: int = 200
    strategy: str = "recursive"
    separators: List[str] = ["\n\n", "\n", " ", ""]
```

**Attributes**:
- `chunk_size` (int): Characters per chunk
- `chunk_overlap` (int): Overlap between chunks
- `strategy` (str): Chunking strategy
- `separators` (List[str]): Text separators

#### `RAGConfig`
```python
class RAGConfig(BaseModel):
    """RAG (Retrieval Augmented Generation) configuration."""
    top_k: int = 5
    similarity_threshold: float = 0.7
    strategy: str = "similarity"
    max_context_length: int = 4000
```

**Attributes**:
- `top_k` (int): Number of documents to retrieve
- `similarity_threshold` (float): Minimum similarity score
- `strategy` (str): Retrieval strategy
- `max_context_length` (int): Maximum context characters

#### `AppConfig`
```python
class AppConfig(BaseModel):
    """Main application configuration."""
    openai: OpenAIConfig
    pinecone: PineconeConfig
    embedding: EmbeddingConfig
    chunking: ChunkingConfig
    rag: RAGConfig
    file_upload: FileUploadConfig
    session: SessionConfig
```

### Functions

##### `load_config() -> AppConfig`
```python
def load_config() -> AppConfig:
    """Load configuration from environment variables."""
```
**Returns**: 
- `AppConfig`: Complete application configuration

**Raises**:
- `ValidationError`: If required environment variables are missing
- `ConfigurationError`: If configuration values are invalid

##### `validate_config(config: AppConfig) -> bool`
```python
def validate_config(config: AppConfig) -> bool:
    """Validate configuration settings."""
```
**Parameters**:
- `config` (AppConfig): Configuration to validate

**Returns**:
- `bool`: True if valid, False otherwise

## 📄 File Processing (`utils/file_processing.py`)

### Classes

#### `FileProcessor`
```python
class FileProcessor:
    """Base class for file processing."""
    
    def __init__(self, config: FileUploadConfig):
        self.config = config
    
    def process(self, file_path: str) -> str:
        """Process file and extract text."""
        raise NotImplementedError
```

#### `PDFProcessor(FileProcessor)`
```python
class PDFProcessor(FileProcessor):
    """PDF file processor."""
    
    def process(self, file_path: str) -> str:
        """Extract text from PDF file."""
```

**Parameters**:
- `file_path` (str): Path to PDF file

**Returns**:
- `str`: Extracted text content

**Raises**:
- `PDFProcessingError`: If PDF cannot be processed
- `FileNotFoundError`: If file doesn't exist

#### `DocxProcessor(FileProcessor)`
```python
class DocxProcessor(FileProcessor):
    """Word document processor."""
    
    def process(self, file_path: str) -> str:
        """Extract text from DOCX file."""
```

**Parameters**:
- `file_path` (str): Path to DOCX file

**Returns**:
- `str`: Extracted text content

**Raises**:
- `DocxProcessingError`: If DOCX cannot be processed

### Functions

##### `get_file_processor(file_extension: str) -> FileProcessor`
```python
def get_file_processor(file_extension: str) -> FileProcessor:
    """Get appropriate file processor for file type."""
```
**Parameters**:
- `file_extension` (str): File extension (e.g., '.pdf', '.docx')

**Returns**:
- `FileProcessor`: Appropriate processor instance

**Raises**:
- `UnsupportedFileTypeError`: If file type not supported

##### `validate_file(file_path: str, config: FileUploadConfig) -> bool`
```python
def validate_file(file_path: str, config: FileUploadConfig) -> bool:
    """Validate uploaded file."""
```
**Parameters**:
- `file_path` (str): Path to file
- `config` (FileUploadConfig): File upload configuration

**Returns**:
- `bool`: True if valid, False otherwise

**Validation Checks**:
- File size within limits
- File extension allowed
- File is readable
- File is not corrupted

## 🔤 Text Processing (`utils/text_processing.py`)

### Classes

#### `TextChunker`
```python
class TextChunker:
    """Text chunking utility."""
    
    def __init__(self, config: ChunkingConfig):
        self.config = config
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks."""
```

**Parameters**:
- `text` (str): Input text to chunk

**Returns**:
- `List[str]`: List of text chunks

#### `RecursiveTextChunker(TextChunker)`
```python
class RecursiveTextChunker(TextChunker):
    """Recursive text chunking strategy."""
    
    def chunk_text(self, text: str) -> List[str]:
        """Recursively split text using multiple separators."""
```

### Functions

##### `clean_text(text: str) -> str`
```python
def clean_text(text: str) -> str:
    """Clean and normalize text."""
```
**Parameters**:
- `text` (str): Raw text input

**Returns**:
- `str`: Cleaned text

**Cleaning Operations**:
- Remove extra whitespace
- Normalize line endings
- Remove special characters
- Fix encoding issues

##### `extract_metadata(text: str) -> Dict[str, Any]`
```python
def extract_metadata(text: str) -> Dict[str, Any]:
    """Extract metadata from text."""
```
**Parameters**:
- `text` (str): Input text

**Returns**:
- `Dict[str, Any]`: Extracted metadata

**Metadata Fields**:
- `word_count`: Number of words
- `char_count`: Number of characters
- `language`: Detected language
- `topics`: Extracted topics

## 🧠 Embedding Management (`utils/embeddings.py`)

### Classes

#### `EmbeddingClient`
```python
class EmbeddingClient:
    """Base embedding client."""
    
    def __init__(self, config: EmbeddingConfig):
        self.config = config
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embedding for text."""
        raise NotImplementedError
    
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts."""
        raise NotImplementedError
```

#### `OpenAIEmbeddingClient(EmbeddingClient)`
```python
class OpenAIEmbeddingClient(EmbeddingClient):
    """OpenAI embedding client."""
    
    def embed_text(self, text: str) -> List[float]:
        """Generate OpenAI embedding for text."""
```

**Parameters**:
- `text` (str): Input text

**Returns**:
- `List[float]`: Embedding vector

**Raises**:
- `EmbeddingError`: If embedding generation fails
- `RateLimitError`: If rate limit exceeded

### Functions

##### `get_embedding_client(config: EmbeddingConfig) -> EmbeddingClient`
```python
def get_embedding_client(config: EmbeddingConfig) -> EmbeddingClient:
    """Get embedding client based on configuration."""
```
**Parameters**:
- `config` (EmbeddingConfig): Embedding configuration

**Returns**:
- `EmbeddingClient`: Appropriate embedding client

## 🗄️ Vector Database (`utils/pinecone_client.py`)

### Classes

#### `PineconeClient`
```python
class PineconeClient:
    """Pinecone vector database client."""
    
    def __init__(self, config: PineconeConfig):
        self.config = config
        self.index = None
    
    def connect(self) -> None:
        """Connect to Pinecone index."""
    
    def upsert_vectors(self, vectors: List[Dict]) -> None:
        """Insert or update vectors."""
    
    def query_vectors(self, query_vector: List[float], top_k: int = 5) -> List[Dict]:
        """Query similar vectors."""
```

### Methods

##### `connect()`
```python
def connect(self) -> None:
    """Establish connection to Pinecone index."""
```
**Raises**:
- `PineconeConnectionError`: If connection fails
- `IndexNotFoundError`: If index doesn't exist

##### `upsert_vectors(vectors: List[Dict]) -> None`
```python
def upsert_vectors(self, vectors: List[Dict]) -> None:
    """Insert or update vectors in the index."""
```
**Parameters**:
- `vectors` (List[Dict]): List of vector dictionaries

**Vector Format**:
```python
{
    "id": "unique_id",
    "values": [0.1, 0.2, ...],  # Embedding vector
    "metadata": {
        "text": "original text",
        "source": "document.pdf",
        "chunk_index": 0
    }
}
```

##### `query_vectors(query_vector: List[float], top_k: int = 5) -> List[Dict]`
```python
def query_vectors(self, query_vector: List[float], top_k: int = 5) -> List[Dict]:
    """Query for similar vectors."""
```
**Parameters**:
- `query_vector` (List[float]): Query embedding vector
- `top_k` (int): Number of results to return

**Returns**:
- `List[Dict]`: List of matching vectors with scores

##### `delete_vectors(ids: List[str]) -> None`
```python
def delete_vectors(self, ids: List[str]) -> None:
    """Delete vectors by IDs."""
```
**Parameters**:
- `ids` (List[str]): List of vector IDs to delete

##### `get_index_stats() -> Dict[str, Any]`
```python
def get_index_stats(self) -> Dict[str, Any]:
    """Get index statistics."""
```
**Returns**:
- `Dict[str, Any]`: Index statistics

**Statistics Include**:
- Total vector count
- Index dimensions
- Namespace information
- Storage usage

## 🤖 RAG Agent (`utils/rag_agent.py`)

### Classes

#### `RAGAgent`
```python
class RAGAgent:
    """Retrieval Augmented Generation agent."""
    
    def __init__(self, 
                 config: RAGConfig,
                 embedding_client: EmbeddingClient,
                 vector_client: PineconeClient,
                 llm_client: OpenAIClient):
        self.config = config
        self.embedding_client = embedding_client
        self.vector_client = vector_client
        self.llm_client = llm_client
    
    def query(self, question: str) -> str:
        """Process query and generate response."""
```

### Methods

##### `query(question: str) -> str`
```python
def query(self, question: str) -> str:
    """Process user query and generate response."""
```
**Parameters**:
- `question` (str): User's question

**Returns**:
- `str`: Generated response

**Process**:
1. Embed the question
2. Retrieve relevant documents
3. Construct context
4. Generate response

##### `add_document(text: str, metadata: Dict[str, Any]) -> None`
```python
def add_document(self, text: str, metadata: Dict[str, Any]) -> None:
    """Add document to knowledge base."""
```
**Parameters**:
- `text` (str): Document text
- `metadata` (Dict[str, Any]): Document metadata

**Process**:
1. Chunk the text
2. Generate embeddings
3. Store in vector database

##### `retrieve_documents(query: str, top_k: int = None) -> List[Dict]`
```python
def retrieve_documents(self, query: str, top_k: int = None) -> List[Dict]:
    """Retrieve relevant documents for query."""
```
**Parameters**:
- `query` (str): Search query
- `top_k` (int): Number of documents to retrieve

**Returns**:
- `List[Dict]`: Retrieved documents with scores

## 💬 Session Management (`utils/session_manager.py`)

### Classes

#### `SessionManager`
```python
class SessionManager:
    """Manage user sessions and chat history."""
    
    def __init__(self, config: SessionConfig):
        self.config = config
        self.sessions = {}
    
    def create_session(self) -> str:
        """Create new session."""
    
    def get_session(self, session_id: str) -> Dict[str, Any]:
        """Get session data."""
    
    def save_session(self, session_id: str, data: Dict[str, Any]) -> None:
        """Save session data."""
```

### Methods

##### `create_session() -> str`
```python
def create_session(self) -> str:
    """Create a new session."""
```
**Returns**:
- `str`: Unique session ID

##### `get_session(session_id: str) -> Dict[str, Any]`
```python
def get_session(self, session_id: str) -> Dict[str, Any]:
    """Retrieve session data."""
```
**Parameters**:
- `session_id` (str): Session identifier

**Returns**:
- `Dict[str, Any]`: Session data

**Session Data Structure**:
```python
{
    "id": "session_id",
    "created_at": "2024-01-01T00:00:00Z",
    "last_accessed": "2024-01-01T00:00:00Z",
    "messages": [
        {
            "role": "user",
            "content": "Hello",
            "timestamp": "2024-01-01T00:00:00Z"
        },
        {
            "role": "assistant",
            "content": "Hi there!",
            "timestamp": "2024-01-01T00:00:00Z"
        }
    ],
    "documents": [
        {
            "filename": "document.pdf",
            "upload_time": "2024-01-01T00:00:00Z",
            "chunk_count": 10
        }
    ]
}
```

## 🎯 Command Processing (`utils/commands.py`)

### Classes

#### `CommandProcessor`
```python
class CommandProcessor:
    """Process special commands."""
    
    def __init__(self, session_manager: SessionManager, rag_agent: RAGAgent):
        self.session_manager = session_manager
        self.rag_agent = rag_agent
        self.commands = self._register_commands()
    
    def process_command(self, command: str, session_id: str) -> str:
        """Process user command."""
```

### Available Commands

#### `/help`
```python
def help_command(self, args: List[str], session_id: str) -> str:
    """Display available commands."""
```
**Returns**: List of available commands and their descriptions

#### `/clear`
```python
def clear_command(self, args: List[str], session_id: str) -> str:
    """Clear session history."""
```
**Returns**: Confirmation message

#### `/sessions`
```python
def sessions_command(self, args: List[str], session_id: str) -> str:
    """List all sessions."""
```
**Returns**: List of session IDs and metadata

#### `/metrics`
```python
def metrics_command(self, args: List[str], session_id: str) -> str:
    """Show performance metrics."""
```
**Returns**: Performance statistics

#### `/config`
```python
def config_command(self, args: List[str], session_id: str) -> str:
    """Display current configuration."""
```
**Returns**: Current configuration settings (sanitized)

## 📊 Monitoring and Metrics (`utils/monitoring.py`)

### Classes

#### `MetricsCollector`
```python
class MetricsCollector:
    """Collect and track application metrics."""
    
    def __init__(self):
        self.metrics = defaultdict(list)
    
    def record_query_time(self, duration: float) -> None:
        """Record query processing time."""
    
    def record_token_usage(self, tokens: int) -> None:
        """Record token usage."""
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get metrics summary."""
```

### Decorators

#### `@timing_decorator`
```python
def timing_decorator(func):
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        # Record timing metric
        return result
    return wrapper
```

#### `@error_handler`
```python
def error_handler(func):
    """Decorator for error handling and logging."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Log error and handle gracefully
            logger.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper
```

## 🚨 Error Handling

### Custom Exceptions

#### `ChatbotError`
```python
class ChatbotError(Exception):
    """Base exception for chatbot errors."""
    pass
```

#### `ConfigurationError`
```python
class ConfigurationError(ChatbotError):
    """Configuration-related errors."""
    pass
```

#### `FileProcessingError`
```python
class FileProcessingError(ChatbotError):
    """File processing errors."""
    pass
```

#### `EmbeddingError`
```python
class EmbeddingError(ChatbotError):
    """Embedding generation errors."""
    pass
```

#### `VectorDatabaseError`
```python
class VectorDatabaseError(ChatbotError):
    """Vector database operation errors."""
    pass
```

## 🔧 Utility Functions

### General Utilities (`utils/helpers.py`)

#### `generate_unique_id() -> str`
```python
def generate_unique_id() -> str:
    """Generate unique identifier."""
```
**Returns**: Unique string identifier

#### `format_timestamp(timestamp: datetime) -> str`
```python
def format_timestamp(timestamp: datetime) -> str:
    """Format timestamp for display."""
```
**Parameters**:
- `timestamp` (datetime): Timestamp to format

**Returns**: Formatted timestamp string

#### `sanitize_filename(filename: str) -> str`
```python
def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe storage."""
```
**Parameters**:
- `filename` (str): Original filename

**Returns**: Sanitized filename

#### `calculate_file_hash(file_path: str) -> str`
```python
def calculate_file_hash(file_path: str) -> str:
    """Calculate file hash for deduplication."""
```
**Parameters**:
- `file_path` (str): Path to file

**Returns**: File hash string

## 📝 Type Definitions

### Common Types

```python
from typing import List, Dict, Any, Optional, Union, Callable
from datetime import datetime
from pathlib import Path

# Message types
Message = Dict[str, Union[str, datetime]]
MessageHistory = List[Message]

# Document types
Document = Dict[str, Any]
DocumentChunk = Dict[str, Union[str, int, float]]

# Vector types
EmbeddingVector = List[float]
VectorMatch = Dict[str, Union[str, float, Dict[str, Any]]]

# Configuration types
ConfigDict = Dict[str, Any]
EnvironmentVars = Dict[str, str]

# Response types
APIResponse = Dict[str, Any]
QueryResult = Dict[str, Union[str, float, List[VectorMatch]]]
```

## 🔍 Testing Utilities

### Test Helpers (`tests/helpers.py`)

#### `create_test_config() -> AppConfig`
```python
def create_test_config() -> AppConfig:
    """Create test configuration."""
```
**Returns**: Test configuration with mock values

#### `create_mock_document(content: str) -> Document`
```python
def create_mock_document(content: str) -> Document:
    """Create mock document for testing."""
```
**Parameters**:
- `content` (str): Document content

**Returns**: Mock document object

#### `assert_response_quality(response: str, expected_keywords: List[str]) -> bool`
```python
def assert_response_quality(response: str, expected_keywords: List[str]) -> bool:
    """Assert response contains expected keywords."""
```
**Parameters**:
- `response` (str): AI response
- `expected_keywords` (List[str]): Keywords that should be present

**Returns**: True if quality check passes

---

## 📖 Usage Examples

### Basic Usage

```python
from utils.config import load_config
from utils.rag_agent import RAGAgent
from utils.embeddings import get_embedding_client
from utils.pinecone_client import PineconeClient
from utils.openai_client import OpenAIClient

# Load configuration
config = load_config()

# Initialize clients
embedding_client = get_embedding_client(config.embedding)
vector_client = PineconeClient(config.pinecone)
llm_client = OpenAIClient(config.openai)

# Create RAG agent
rag_agent = RAGAgent(
    config.rag,
    embedding_client,
    vector_client,
    llm_client
)

# Add document
rag_agent.add_document(
    text="This is a sample document.",
    metadata={"source": "example.txt"}
)

# Query
response = rag_agent.query("What is this document about?")
print(response)
```

### Advanced Usage

```python
# Custom embedding processing
from utils.text_processing import TextChunker
from utils.file_processing import get_file_processor

# Process file
processor = get_file_processor(".pdf")
text = processor.process("document.pdf")

# Chunk text
chunker = TextChunker(config.chunking)
chunks = chunker.chunk_text(text)

# Generate embeddings
embeddings = embedding_client.embed_batch(chunks)

# Store in vector database
vectors = [
    {
        "id": f"doc_chunk_{i}",
        "values": embedding,
        "metadata": {
            "text": chunk,
            "source": "document.pdf",
            "chunk_index": i
        }
    }
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
]

vector_client.upsert_vectors(vectors)
```

---

**For more examples and detailed implementation guides, see the [Development Guide](./development.md) and [User Guide](./user-guide.md).**