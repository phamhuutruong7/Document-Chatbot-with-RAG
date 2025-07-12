import os
from typing import List, Optional
from pathlib import Path
from pydantic import BaseModel, Field, validator

class OpenAIConfig(BaseModel):
    """Configuration for OpenAI API settings."""
    api_key: str = Field(..., description="OpenAI API key")
    model: str = Field(default="gpt-3.5-turbo", description="OpenAI model name")
    base_url: Optional[str] = Field(default=None, description="Custom OpenAI API base URL")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="Model temperature")
    max_tokens: Optional[int] = Field(default=None, gt=0, description="Maximum tokens for response")
    
    @validator('api_key')
    def validate_api_key(cls, v):
        if not v or v.startswith('your-'):
            raise ValueError('Valid OpenAI API key is required')
        return v

class EmbeddingConfig(BaseModel):
    """Configuration for embedding API settings."""
    api_key: str = Field(..., description="Embedding API key")
    model: str = Field(default="text-embedding-ada-002", description="Embedding model name")
    base_url: Optional[str] = Field(default=None, description="Custom embedding API base URL")
    batch_size: int = Field(default=100, gt=0, description="Batch size for embedding requests")
    
    @validator('api_key')
    def validate_api_key(cls, v):
        if not v or v.startswith('your-'):
            raise ValueError('Valid embedding API key is required')
        return v

class PineconeConfig(BaseModel):
    """Configuration for Pinecone vector database."""
    api_key: str = Field(..., description="Pinecone API key")
    index_name: str = Field(..., description="Pinecone index name")
    environment: Optional[str] = Field(default=None, description="Pinecone environment")
    dimension: int = Field(default=1536, gt=0, description="Vector dimension")
    metric: str = Field(default="cosine", description="Distance metric")
    
    @validator('api_key')
    def validate_api_key(cls, v):
        if not v or v.startswith('your-'):
            raise ValueError('Valid Pinecone API key is required')
        return v
    
    @validator('index_name')
    def validate_index_name(cls, v):
        if not v:
            raise ValueError('Pinecone index name is required')
        return v

class LangSmithConfig(BaseModel):
    """Configuration for LangSmith tracing (optional)."""
    api_key: Optional[str] = Field(default=None, description="LangSmith API key")
    project: Optional[str] = Field(default=None, description="LangSmith project name")
    tracing: bool = Field(default=False, description="Enable LangSmith tracing")
    endpoint: Optional[str] = Field(default=None, description="LangSmith endpoint URL")

class FileUploadConfig(BaseModel):
    """Configuration for file upload settings."""
    max_size_mb: int = Field(default=100, gt=0, description="Maximum file size in MB")
    allowed_extensions: List[str] = Field(
        default=['.pdf', '.txt', '.docx', '.md'],
        description="Allowed file extensions"
    )
    max_files_per_session: int = Field(default=100, gt=0, description="Maximum files per session")
    
    @validator('allowed_extensions')
    def validate_extensions(cls, v):
        if not v:
            raise ValueError('At least one file extension must be allowed')
        return [ext.lower() if not ext.startswith('.') else ext.lower() for ext in v]

class ChunkingConfig(BaseModel):
    """Configuration for text chunking."""
    chunk_size: int = Field(default=1000, gt=0, description="Size of text chunks")
    chunk_overlap: int = Field(default=200, ge=0, description="Overlap between chunks")
    separators: List[str] = Field(
        default=["\n\n", "\n", " ", ""],
        description="Text separators for chunking"
    )
    
    @validator('chunk_overlap')
    def validate_overlap(cls, v, values):
        chunk_size = values.get('chunk_size', 1000)
        if v >= chunk_size:
            raise ValueError('Chunk overlap must be less than chunk size')
        return v

class RAGConfig(BaseModel):
    """Configuration for RAG pipeline."""
    top_k: int = Field(default=5, gt=0, description="Number of top chunks to retrieve")
    similarity_threshold: float = Field(
        default=0.7, ge=0.0, le=1.0,
        description="Minimum similarity threshold for retrieval"
    )
    max_context_chunks: int = Field(
        default=5, gt=0,
        description="Maximum number of context chunks for generation"
    )
    enable_reranking: bool = Field(default=False, description="Enable result reranking")

class AppConfig(BaseModel):
    """Main application configuration."""
    # API configurations
    openai: OpenAIConfig
    embedding: EmbeddingConfig
    pinecone: PineconeConfig
    langsmith: LangSmithConfig = LangSmithConfig()
    
    # Feature configurations
    file_upload: FileUploadConfig = FileUploadConfig()
    chunking: ChunkingConfig = ChunkingConfig()
    rag: RAGConfig = RAGConfig()
    
    # App settings
    data_dir: str = Field(default="data", description="Data directory path")
    debug_mode: bool = Field(default=False, description="Enable debug mode")
    session_timeout_hours: int = Field(default=24, gt=0, description="Session timeout in hours")
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False

def load_config() -> AppConfig:
    """Load configuration from environment variables."""
    
    # OpenAI configuration
    openai_config = OpenAIConfig(
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        temperature=float(os.getenv("OPENAI_TEMPERATURE", "0.7")),
        max_tokens=int(os.getenv("OPENAI_MAX_TOKENS")) if os.getenv("OPENAI_MAX_TOKENS") else None
    )
    
    # Embedding configuration
    embedding_config = EmbeddingConfig(
        api_key=os.getenv("EMBEDDING_API_KEY", os.getenv("OPENAI_API_KEY", "")),
        model=os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002"),
        base_url=os.getenv("EMBEDDING_BASE_URL"),
        batch_size=int(os.getenv("EMBEDDING_BATCH_SIZE", "100"))
    )
    
    # Pinecone configuration
    pinecone_config = PineconeConfig(
        api_key=os.getenv("PINECONE_API_KEY", ""),
        index_name=os.getenv("PINECONE_INDEX_NAME", ""),
        environment=os.getenv("PINECONE_ENVIRONMENT"),
        dimension=int(os.getenv("PINECONE_DIMENSION", "1536")),
        metric=os.getenv("PINECONE_METRIC", "cosine")
    )
    
    # LangSmith configuration
    langsmith_config = LangSmithConfig(
        api_key=os.getenv("LANGCHAIN_API_KEY"),
        project=os.getenv("LANGCHAIN_PROJECT"),
        tracing=os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true",
        endpoint=os.getenv("LANGCHAIN_ENDPOINT")
    )
    
    # File upload configuration
    file_upload_config = FileUploadConfig(
        max_size_mb=int(os.getenv("MAX_FILE_SIZE_MB", "100")),
        allowed_extensions=os.getenv("ALLOWED_EXTENSIONS", ".pdf,.txt,.docx,.md").split(","),
        max_files_per_session=int(os.getenv("MAX_FILES_PER_SESSION", "100"))
    )
    
    # Chunking configuration
    chunking_config = ChunkingConfig(
        chunk_size=int(os.getenv("CHUNK_SIZE", "1000")),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "200")),
        separators=os.getenv("CHUNK_SEPARATORS", "\n\n,\n, ,").split(",")
    )
    
    # RAG configuration
    rag_config = RAGConfig(
        top_k=int(os.getenv("RAG_TOP_K", "5")),
        similarity_threshold=float(os.getenv("RAG_SIMILARITY_THRESHOLD", "0.7")),
        max_context_chunks=int(os.getenv("RAG_MAX_CONTEXT_CHUNKS", "5")),
        enable_reranking=os.getenv("RAG_ENABLE_RERANKING", "false").lower() == "true"
    )
    
    # Main app configuration
    config = AppConfig(
        openai=openai_config,
        embedding=embedding_config,
        pinecone=pinecone_config,
        langsmith=langsmith_config,
        file_upload=file_upload_config,
        chunking=chunking_config,
        rag=rag_config,
        data_dir=os.getenv("DATA_DIR", "data"),
        debug_mode=os.getenv("DEBUG_MODE", "false").lower() == "true",
        session_timeout_hours=int(os.getenv("SESSION_TIMEOUT_HOURS", "24"))
    )
    
    return config

def validate_config(config: AppConfig) -> List[str]:
    """Validate configuration and return list of issues."""
    issues = []
    
    # Check required API keys
    if not config.openai.api_key or config.openai.api_key.startswith('your-'):
        issues.append("OpenAI API key is missing or invalid")
    
    if not config.embedding.api_key or config.embedding.api_key.startswith('your-'):
        issues.append("Embedding API key is missing or invalid")
    
    if not config.pinecone.api_key or config.pinecone.api_key.startswith('your-'):
        issues.append("Pinecone API key is missing or invalid")
    
    if not config.pinecone.index_name:
        issues.append("Pinecone index name is missing")
    
    # Check data directory
    data_path = Path(config.data_dir)
    if not data_path.exists():
        try:
            data_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            issues.append(f"Cannot create data directory: {e}")
    
    return issues