# 👨‍💻 Development Guide

## Overview

This guide is for developers who want to contribute to, extend, or customize the Document Chatbot. It covers development setup, coding standards, architecture patterns, and contribution guidelines.

## 🚀 Development Setup

### Prerequisites

- **Python 3.8+** (3.9+ recommended)
- **Git** for version control
- **Virtual environment** (venv, conda, or poetry)
- **Code editor** (VS Code, PyCharm, etc.)

### Environment Setup

#### 1. Clone Repository
```bash
git clone <repository-url>
cd document-chatbot
```

#### 2. Create Virtual Environment
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Using conda
conda create -n chatbot python=3.9
conda activate chatbot
```

#### 3. Install Dependencies
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Or install in editable mode
pip install -e .
```

#### 4. Setup Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

#### 5. Environment Configuration
```bash
# Copy example environment file
cp .env.example .env

# Edit with your API keys
vim .env
```

### Development Dependencies

#### Core Development Tools
```txt
# requirements-dev.txt

# Testing
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
pytest-asyncio>=0.21.0

# Code Quality
black>=23.0.0
isort>=5.12.0
flake8>=6.0.0
mypy>=1.0.0
pylint>=2.17.0

# Documentation
sphinx>=6.0.0
sphinx-rtd-theme>=1.2.0
mkdocs>=1.4.0
mkdocs-material>=9.0.0

# Development Tools
ipython>=8.0.0
jupyter>=1.0.0
notebook>=6.5.0

# Debugging
ipdb>=0.13.0
pdb++>=0.10.0

# Performance
memory-profiler>=0.60.0
line-profiler>=4.0.0

# Security
bandit>=1.7.0
safety>=2.3.0
```

## 🏗️ Project Structure

### Directory Layout
```
document-chatbot/
├── main.py                 # Streamlit application entry point
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # Project overview
├── pyproject.toml         # Project configuration
├── setup.py               # Package setup
│
├── utils/                 # Core utilities
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── file_processing.py # File processing utilities
│   ├── text_processing.py # Text processing utilities
│   ├── embeddings.py      # Embedding generation
│   ├── pinecone_client.py # Vector database client
│   ├── openai_client.py   # OpenAI API client
│   ├── rag_agent.py       # RAG implementation
│   ├── session_manager.py # Session management
│   ├── commands.py        # Command processing
│   ├── monitoring.py      # Metrics and monitoring
│   └── helpers.py         # General utilities
│
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py        # Pytest configuration
│   ├── test_config.py     # Configuration tests
│   ├── test_file_processing.py
│   ├── test_embeddings.py
│   ├── test_rag_agent.py
│   ├── test_integration.py
│   └── fixtures/          # Test data
│       ├── sample.pdf
│       ├── sample.docx
│       └── sample.txt
│
├── docs/                  # Documentation
│   ├── README.md
│   ├── installation.md
│   ├── user-guide.md
│   ├── configuration.md
│   ├── api-reference.md
│   ├── troubleshooting.md
│   ├── development.md
│   └── diagrams/
│
├── scripts/               # Utility scripts
│   ├── setup_dev.sh       # Development setup
│   ├── run_tests.sh       # Test runner
│   ├── format_code.sh     # Code formatting
│   └── deploy.sh          # Deployment script
│
├── docker/                # Docker configuration
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── docker-compose.dev.yml
│
└── .github/               # GitHub workflows
    └── workflows/
        ├── ci.yml
        ├── cd.yml
        └── security.yml
```

## 🎯 Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

#### Code Formatting
```python
# Use Black for automatic formatting
black --line-length 88 --target-version py38 .

# Use isort for import sorting
isort --profile black .
```

#### Naming Conventions
```python
# Variables and functions: snake_case
user_input = "Hello"
def process_document():
    pass

# Classes: PascalCase
class DocumentProcessor:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_FILE_SIZE = 100
DEFAULT_MODEL = "gpt-4"

# Private methods: _leading_underscore
def _internal_method():
    pass
```

#### Type Hints
```python
from typing import List, Dict, Optional, Union

def process_text(text: str, max_length: Optional[int] = None) -> List[str]:
    """Process text and return chunks.
    
    Args:
        text: Input text to process
        max_length: Maximum length per chunk
        
    Returns:
        List of text chunks
        
    Raises:
        ValueError: If text is empty
    """
    if not text:
        raise ValueError("Text cannot be empty")
    
    # Implementation here
    return chunks
```

#### Docstring Format
```python
def complex_function(param1: str, param2: int, param3: Optional[bool] = None) -> Dict[str, Any]:
    """Brief description of the function.
    
    Longer description if needed. Explain the purpose,
    behavior, and any important details.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        param3: Optional parameter description
        
    Returns:
        Dictionary containing results with keys:
        - 'status': Operation status
        - 'data': Processed data
        - 'metadata': Additional information
        
    Raises:
        ValueError: When param1 is invalid
        ConnectionError: When external service is unavailable
        
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result['status'])
        'success'
    """
    pass
```

### Code Quality Tools

#### Linting Configuration

**`.flake8`**
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = 
    .git,
    __pycache__,
    venv,
    .venv,
    build,
    dist
```

**`pyproject.toml`**
```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
(
  /(
      \.eggs
    | \.git
    | \.venv
    | build
    | dist
  )/
)
'''

[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

## 🧪 Testing

### Testing Framework

We use **pytest** for testing with the following structure:

#### Test Configuration (`conftest.py`)
```python
import pytest
from unittest.mock import Mock
from utils.config import AppConfig, OpenAIConfig, PineconeConfig

@pytest.fixture
def mock_config():
    """Create mock configuration for testing."""
    return AppConfig(
        openai=OpenAIConfig(
            api_key="test-key",
            model="gpt-3.5-turbo",
            temperature=0.7
        ),
        pinecone=PineconeConfig(
            api_key="test-key",
            environment="test",
            index_name="test-index"
        )
        # ... other config
    )

@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client."""
    client = Mock()
    client.chat.completions.create.return_value = Mock(
        choices=[Mock(message=Mock(content="Test response"))]
    )
    return client

@pytest.fixture
def sample_document():
    """Sample document for testing."""
    return {
        "text": "This is a sample document for testing.",
        "metadata": {
            "source": "test.txt",
            "created_at": "2024-01-01T00:00:00Z"
        }
    }
```

#### Unit Tests Example
```python
# test_text_processing.py
import pytest
from utils.text_processing import TextChunker, clean_text
from utils.config import ChunkingConfig

class TestTextChunker:
    """Test text chunking functionality."""
    
    def test_chunk_text_basic(self):
        """Test basic text chunking."""
        config = ChunkingConfig(chunk_size=10, chunk_overlap=2)
        chunker = TextChunker(config)
        
        text = "This is a test document with some content."
        chunks = chunker.chunk_text(text)
        
        assert len(chunks) > 1
        assert all(len(chunk) <= 12 for chunk in chunks)  # size + overlap
    
    def test_chunk_text_empty(self):
        """Test chunking empty text."""
        config = ChunkingConfig()
        chunker = TextChunker(config)
        
        chunks = chunker.chunk_text("")
        assert chunks == []
    
    @pytest.mark.parametrize("chunk_size,expected_chunks", [
        (5, 9),
        (10, 5),
        (20, 3),
    ])
    def test_chunk_sizes(self, chunk_size, expected_chunks):
        """Test different chunk sizes."""
        config = ChunkingConfig(chunk_size=chunk_size, chunk_overlap=0)
        chunker = TextChunker(config)
        
        text = "A" * 50  # 50 character string
        chunks = chunker.chunk_text(text)
        
        assert len(chunks) == expected_chunks

def test_clean_text():
    """Test text cleaning function."""
    dirty_text = "  This   has\n\nextra   whitespace  \n"
    clean = clean_text(dirty_text)
    
    assert clean == "This has extra whitespace"
    assert "\n\n" not in clean
    assert "   " not in clean
```

#### Integration Tests
```python
# test_integration.py
import pytest
from unittest.mock import patch, Mock
from utils.rag_agent import RAGAgent

class TestRAGIntegration:
    """Integration tests for RAG functionality."""
    
    @patch('utils.openai_client.OpenAI')
    @patch('utils.pinecone_client.pinecone')
    def test_end_to_end_query(self, mock_pinecone, mock_openai, mock_config):
        """Test complete query flow."""
        # Setup mocks
        mock_openai.return_value.embeddings.create.return_value = Mock(
            data=[Mock(embedding=[0.1] * 1536)]
        )
        mock_openai.return_value.chat.completions.create.return_value = Mock(
            choices=[Mock(message=Mock(content="Test response"))]
        )
        
        mock_index = Mock()
        mock_index.query.return_value = {
            'matches': [
                {
                    'id': 'test-1',
                    'score': 0.9,
                    'metadata': {'text': 'Relevant content'}
                }
            ]
        }
        mock_pinecone.Index.return_value = mock_index
        
        # Create RAG agent
        rag_agent = RAGAgent(mock_config)
        
        # Test query
        response = rag_agent.query("What is this about?")
        
        assert response == "Test response"
        mock_index.query.assert_called_once()
        mock_openai.return_value.chat.completions.create.assert_called_once()
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=utils --cov-report=html

# Run specific test file
pytest tests/test_config.py

# Run specific test
pytest tests/test_config.py::test_load_config

# Run with verbose output
pytest -v

# Run tests matching pattern
pytest -k "test_chunk"
```

## 🔧 Development Workflow

### Git Workflow

We use **Git Flow** with the following branches:

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Feature development
- `hotfix/*`: Critical bug fixes
- `release/*`: Release preparation

#### Feature Development
```bash
# Create feature branch
git checkout develop
git pull origin develop
git checkout -b feature/new-embedding-model

# Make changes and commit
git add .
git commit -m "feat: add support for new embedding model"

# Push and create PR
git push origin feature/new-embedding-model
```

#### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(rag): add support for custom embedding models
fix(config): handle missing environment variables gracefully
docs(api): update API reference for new endpoints
test(embeddings): add unit tests for embedding client
```

### Code Review Process

#### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

#### Review Checklist
- **Functionality**: Does the code work as intended?
- **Tests**: Are there adequate tests?
- **Documentation**: Is documentation updated?
- **Performance**: Any performance implications?
- **Security**: Any security concerns?
- **Style**: Follows coding standards?

## 🏛️ Architecture Patterns

### Dependency Injection

```python
# Good: Dependency injection
class RAGAgent:
    def __init__(self, 
                 embedding_client: EmbeddingClient,
                 vector_client: VectorClient,
                 llm_client: LLMClient):
        self.embedding_client = embedding_client
        self.vector_client = vector_client
        self.llm_client = llm_client

# Usage
embedding_client = OpenAIEmbeddingClient(config.embedding)
vector_client = PineconeClient(config.pinecone)
llm_client = OpenAIClient(config.openai)

rag_agent = RAGAgent(embedding_client, vector_client, llm_client)
```

### Factory Pattern

```python
# Factory for file processors
class FileProcessorFactory:
    _processors = {
        '.pdf': PDFProcessor,
        '.docx': DocxProcessor,
        '.txt': TextProcessor,
        '.md': MarkdownProcessor
    }
    
    @classmethod
    def create_processor(cls, file_extension: str) -> FileProcessor:
        processor_class = cls._processors.get(file_extension)
        if not processor_class:
            raise UnsupportedFileTypeError(f"Unsupported file type: {file_extension}")
        return processor_class()
```

### Strategy Pattern

```python
# Strategy for different chunking methods
class ChunkingStrategy(ABC):
    @abstractmethod
    def chunk_text(self, text: str, config: ChunkingConfig) -> List[str]:
        pass

class RecursiveChunkingStrategy(ChunkingStrategy):
    def chunk_text(self, text: str, config: ChunkingConfig) -> List[str]:
        # Implementation
        pass

class TokenChunkingStrategy(ChunkingStrategy):
    def chunk_text(self, text: str, config: ChunkingConfig) -> List[str]:
        # Implementation
        pass

# Usage
strategy_map = {
    'recursive': RecursiveChunkingStrategy(),
    'token': TokenChunkingStrategy()
}

strategy = strategy_map[config.chunking.strategy]
chunks = strategy.chunk_text(text, config.chunking)
```

### Observer Pattern

```python
# Event system for monitoring
class EventObserver(ABC):
    @abstractmethod
    def handle_event(self, event: Event) -> None:
        pass

class MetricsObserver(EventObserver):
    def handle_event(self, event: Event) -> None:
        if event.type == 'query_completed':
            self.record_query_time(event.data['duration'])

class LoggingObserver(EventObserver):
    def handle_event(self, event: Event) -> None:
        logger.info(f"Event: {event.type}, Data: {event.data}")

# Event emitter
class EventEmitter:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer: EventObserver):
        self.observers.append(observer)
    
    def emit_event(self, event: Event):
        for observer in self.observers:
            observer.handle_event(event)
```

## 🔌 Adding New Features

### Adding a New File Processor

1. **Create Processor Class**
```python
# utils/file_processing.py
class PowerPointProcessor(FileProcessor):
    """Process PowerPoint files."""
    
    def process(self, file_path: str) -> str:
        """Extract text from PowerPoint file."""
        try:
            from pptx import Presentation
            
            prs = Presentation(file_path)
            text_content = []
            
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        text_content.append(shape.text)
            
            return "\n".join(text_content)
            
        except Exception as e:
            raise FileProcessingError(f"Error processing PowerPoint file: {e}")
```

2. **Register in Factory**
```python
# Update FileProcessorFactory
class FileProcessorFactory:
    _processors = {
        '.pdf': PDFProcessor,
        '.docx': DocxProcessor,
        '.txt': TextProcessor,
        '.md': MarkdownProcessor,
        '.pptx': PowerPointProcessor,  # Add new processor
    }
```

3. **Add Tests**
```python
# tests/test_file_processing.py
class TestPowerPointProcessor:
    def test_process_pptx(self):
        processor = PowerPointProcessor()
        # Test implementation
```

4. **Update Configuration**
```python
# Update allowed extensions
ALLOWED_EXTENSIONS = "pdf,docx,txt,md,pptx"
```

### Adding a New Embedding Provider

1. **Create Client Class**
```python
# utils/embeddings.py
class HuggingFaceEmbeddingClient(EmbeddingClient):
    """HuggingFace embedding client."""
    
    def __init__(self, config: EmbeddingConfig):
        super().__init__(config)
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(config.model)
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embedding using HuggingFace model."""
        embedding = self.model.encode(text)
        return embedding.tolist()
    
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts."""
        embeddings = self.model.encode(texts)
        return embeddings.tolist()
```

2. **Update Factory**
```python
# utils/embeddings.py
def get_embedding_client(config: EmbeddingConfig) -> EmbeddingClient:
    """Get embedding client based on provider."""
    if config.provider == "openai":
        return OpenAIEmbeddingClient(config)
    elif config.provider == "huggingface":
        return HuggingFaceEmbeddingClient(config)
    else:
        raise ValueError(f"Unsupported embedding provider: {config.provider}")
```

3. **Update Configuration**
```python
# utils/config.py
class EmbeddingConfig(BaseModel):
    provider: str = "openai"  # openai, huggingface
    model: str = "text-embedding-ada-002"
    # Add provider-specific settings
```

## 🚀 Performance Optimization

### Profiling

```python
# Performance profiling
import cProfile
import pstats
from functools import wraps

def profile_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Top 10 functions
        
        return result
    return wrapper

# Usage
@profile_function
def slow_function():
    # Function to profile
    pass
```

### Memory Optimization

```python
# Memory monitoring
import tracemalloc
from memory_profiler import profile

@profile
def memory_intensive_function():
    # Function to monitor memory usage
    pass

# Track memory usage
tracemalloc.start()
# ... code to monitor ...
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.1f} MB")
tracemalloc.stop()
```

### Caching

```python
# Implement caching for expensive operations
from functools import lru_cache
import redis

class EmbeddingCache:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    def get_embedding(self, text: str) -> Optional[List[float]]:
        """Get cached embedding."""
        key = f"embedding:{hash(text)}"
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    def set_embedding(self, text: str, embedding: List[float]) -> None:
        """Cache embedding."""
        key = f"embedding:{hash(text)}"
        self.redis.setex(key, 3600, json.dumps(embedding))  # 1 hour TTL

# Usage in embedding client
class CachedEmbeddingClient(EmbeddingClient):
    def __init__(self, base_client: EmbeddingClient, cache: EmbeddingCache):
        self.base_client = base_client
        self.cache = cache
    
    def embed_text(self, text: str) -> List[float]:
        # Check cache first
        cached = self.cache.get_embedding(text)
        if cached:
            return cached
        
        # Generate and cache
        embedding = self.base_client.embed_text(text)
        self.cache.set_embedding(text, embedding)
        return embedding
```

## 🔒 Security Considerations

### API Key Management

```python
# Secure API key handling
import os
from cryptography.fernet import Fernet

class SecureConfig:
    def __init__(self):
        self.cipher = Fernet(os.environ.get('ENCRYPTION_KEY'))
    
    def encrypt_api_key(self, api_key: str) -> str:
        """Encrypt API key for storage."""
        return self.cipher.encrypt(api_key.encode()).decode()
    
    def decrypt_api_key(self, encrypted_key: str) -> str:
        """Decrypt API key for use."""
        return self.cipher.decrypt(encrypted_key.encode()).decode()
```

### Input Validation

```python
# Input sanitization
import re
from typing import Any

def sanitize_user_input(user_input: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    # Remove potentially dangerous characters
    sanitized = re.sub(r'[<>"\';]', '', user_input)
    
    # Limit length
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000]
    
    return sanitized.strip()

def validate_file_upload(file_data: Any) -> bool:
    """Validate uploaded file for security."""
    # Check file size
    if len(file_data) > 100 * 1024 * 1024:  # 100MB
        return False
    
    # Check file type by content, not just extension
    # Implementation depends on file type
    
    return True
```

## 📊 Monitoring and Logging

### Structured Logging

```python
# logging_config.py
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        if hasattr(record, 'user_id'):
            log_entry['user_id'] = record.user_id
        
        if hasattr(record, 'session_id'):
            log_entry['session_id'] = record.session_id
        
        return json.dumps(log_entry)

# Setup logging
def setup_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
```

### Metrics Collection

```python
# metrics.py
from prometheus_client import Counter, Histogram, Gauge
import time

# Define metrics
query_counter = Counter('chatbot_queries_total', 'Total number of queries')
response_time = Histogram('chatbot_response_time_seconds', 'Response time')
active_sessions = Gauge('chatbot_active_sessions', 'Number of active sessions')

class MetricsMiddleware:
    def __init__(self):
        self.start_time = None
    
    def before_query(self, query: str, session_id: str):
        self.start_time = time.time()
        query_counter.inc()
    
    def after_query(self, response: str, session_id: str):
        if self.start_time:
            duration = time.time() - self.start_time
            response_time.observe(duration)
```

## 🚀 Deployment

### Docker Development

```dockerfile
# Dockerfile.dev
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# Copy source code
COPY . .

# Install in development mode
RUN pip install -e .

# Expose port
EXPOSE 8501

# Development command
CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
```

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  chatbot-dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8501:8501"
    volumes:
      - .:/app
      - /app/.venv  # Exclude virtual environment
    environment:
      - DEBUG=true
      - LOG_LEVEL=DEBUG
    env_file:
      - .env.dev
    command: >
      sh -c "pip install -e . &&
             streamlit run main.py --server.address 0.0.0.0"
```

### CI/CD Pipeline

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10']
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
    
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
    
    - name: Type check with mypy
      run: mypy utils/
    
    - name: Test with pytest
      run: |
        pytest --cov=utils --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

## 📚 Documentation

### API Documentation

Use **Sphinx** for API documentation:

```python
# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme'
]

html_theme = 'sphinx_rtd_theme'
```

```bash
# Generate documentation
sphinx-apidoc -o docs/ utils/
sphinx-build -b html docs/ docs/_build/html
```

### User Documentation

Use **MkDocs** for user-facing documentation:

```yaml
# mkdocs.yml
site_name: Document Chatbot
theme:
  name: material
  palette:
    primary: blue
    accent: blue

nav:
  - Home: index.md
  - Installation: installation.md
  - User Guide: user-guide.md
  - Configuration: configuration.md
  - API Reference: api-reference.md
  - Development: development.md
  - Troubleshooting: troubleshooting.md

markdown_extensions:
  - codehilite
  - admonition
  - toc:
      permalink: true
```

## 🤝 Contributing

### Contribution Process

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests**
5. **Update documentation**
6. **Submit a pull request**

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the coding standards
- Write clear commit messages

### Getting Help

- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: General questions and ideas
- **Discord/Slack**: Real-time chat (if available)
- **Email**: Direct contact for sensitive issues

---

**Happy coding! 🚀**

For more information, see the [API Reference](./api-reference.md) and [User Guide](./user-guide.md).