# ⚙️ Configuration Guide

## Overview

The Document Chatbot uses a comprehensive configuration system that allows you to customize various aspects of the application. This guide covers all configuration options, environment variables, and advanced settings.

## 🔧 Configuration Architecture

The application uses a hierarchical configuration system:

1. **Environment Variables** - Primary configuration source
2. **Default Values** - Fallback when environment variables are not set
3. **Runtime Configuration** - Dynamic settings that can be modified during execution

## 📋 Environment Variables

### Required Configuration

These environment variables are essential for the application to function:

#### OpenAI Configuration
```bash
# OpenAI API Key (Required)
OPENAI_API_KEY=your_openai_api_key_here

# OpenAI Model Selection
OPENAI_MODEL=gpt-4  # Options: gpt-3.5-turbo, gpt-4, gpt-4-turbo

# OpenAI API Base URL (Optional - for custom endpoints)
OPENAI_API_BASE=https://api.openai.com/v1

# Temperature for response generation
OPENAI_TEMPERATURE=0.7  # Range: 0.0 to 2.0

# Maximum tokens for responses
OPENAI_MAX_TOKENS=1000  # Adjust based on needs
```

#### Pinecone Configuration
```bash
# Pinecone API Key (Required)
PINECONE_API_KEY=your_pinecone_api_key_here

# Pinecone Environment
PINECONE_ENVIRONMENT=us-west1-gcp  # Your Pinecone environment

# Pinecone Index Name
PINECONE_INDEX_NAME=document-chatbot  # Your index name

# Pinecone Namespace (Optional)
PINECONE_NAMESPACE=default  # For data isolation
```

#### Embedding Configuration
```bash
# Embedding Model Provider
EMBEDDING_PROVIDER=openai  # Options: openai, huggingface

# OpenAI Embedding Model
EMBEDDING_MODEL=text-embedding-ada-002

# Embedding Dimensions
EMBEDDING_DIMENSIONS=1536  # Must match your Pinecone index

# Batch Size for Embedding
EMBEDDING_BATCH_SIZE=100  # Number of texts to embed at once
```

### Optional Configuration

#### LangSmith Tracing (Optional)
```bash
# Enable LangSmith tracing
LANGCHAIN_TRACING_V2=true

# LangSmith API Key
LANGCHAIN_API_KEY=your_langsmith_api_key

# LangSmith Project Name
LANGCHAIN_PROJECT=document-chatbot

# LangSmith Endpoint
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

#### File Upload Settings
```bash
# Maximum file size (in MB)
MAX_FILE_SIZE_MB=100

# Allowed file extensions (comma-separated)
ALLOWED_EXTENSIONS=pdf,docx,txt,md

# Upload directory
UPLOAD_DIR=./uploads

# Temporary directory for processing
TEMP_DIR=./temp
```

#### Text Chunking Configuration
```bash
# Chunk size for text splitting
CHUNK_SIZE=1000  # Characters per chunk

# Chunk overlap
CHUNK_OVERLAP=200  # Overlap between chunks

# Chunking strategy
CHUNKING_STRATEGY=recursive  # Options: recursive, character, token

# Separators for text splitting
CHUNK_SEPARATORS="\n\n,\n, ,"  # Comma-separated list
```

#### RAG Configuration
```bash
# Number of documents to retrieve
RAG_TOP_K=5  # Top K similar documents

# Similarity threshold
RAG_SIMILARITY_THRESHOLD=0.7  # Minimum similarity score

# RAG strategy
RAG_STRATEGY=similarity  # Options: similarity, mmr, similarity_score_threshold

# Maximum context length
RAG_MAX_CONTEXT_LENGTH=4000  # Characters in context
```

#### Session Management
```bash
# Session storage directory
SESSION_DIR=./sessions

# Session timeout (in minutes)
SESSION_TIMEOUT=60

# Maximum sessions per user
MAX_SESSIONS=10

# Auto-save interval (in seconds)
AUTO_SAVE_INTERVAL=30
```

#### Application Settings
```bash
# Application title
APP_TITLE="Document Chatbot"

# Application description
APP_DESCRIPTION="AI-powered document analysis and Q&A"

# Debug mode
DEBUG=false

# Log level
LOG_LEVEL=INFO  # Options: DEBUG, INFO, WARNING, ERROR

# Log file path
LOG_FILE=./logs/app.log
```

## 📁 Configuration Files

### Environment File (.env)

Create a `.env` file in your project root:

```bash
# .env file example

# === REQUIRED SETTINGS ===
OPENAI_API_KEY=sk-your-openai-key-here
PINECONE_API_KEY=your-pinecone-key-here
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX_NAME=document-chatbot

# === OPTIONAL SETTINGS ===
# OpenAI Configuration
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=1000

# Embedding Configuration
EMBEDDING_MODEL=text-embedding-ada-002
EMBEDDING_DIMENSIONS=1536

# File Upload Settings
MAX_FILE_SIZE_MB=100
ALLOWED_EXTENSIONS=pdf,docx,txt,md

# Text Chunking
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# RAG Settings
RAG_TOP_K=5
RAG_SIMILARITY_THRESHOLD=0.7

# Application Settings
DEBUG=false
LOG_LEVEL=INFO
```

### Docker Environment

For Docker deployments, create a `docker.env` file:

```bash
# docker.env
OPENAI_API_KEY=sk-your-openai-key-here
PINECONE_API_KEY=your-pinecone-key-here
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX_NAME=document-chatbot

# Docker-specific settings
UPLOAD_DIR=/app/uploads
SESSION_DIR=/app/sessions
LOG_FILE=/app/logs/app.log
```

## 🔧 Advanced Configuration

### Model Configuration

#### OpenAI Model Options
```python
# Available OpenAI models
MODELS = {
    "gpt-3.5-turbo": {
        "max_tokens": 4096,
        "cost_per_1k_tokens": 0.002,
        "speed": "fast"
    },
    "gpt-4": {
        "max_tokens": 8192,
        "cost_per_1k_tokens": 0.03,
        "speed": "medium"
    },
    "gpt-4-turbo": {
        "max_tokens": 128000,
        "cost_per_1k_tokens": 0.01,
        "speed": "fast"
    }
}
```

#### Embedding Model Options
```python
# Available embedding models
EMBEDDING_MODELS = {
    "text-embedding-ada-002": {
        "dimensions": 1536,
        "max_input": 8191,
        "cost_per_1k_tokens": 0.0001
    },
    "text-embedding-3-small": {
        "dimensions": 1536,
        "max_input": 8191,
        "cost_per_1k_tokens": 0.00002
    },
    "text-embedding-3-large": {
        "dimensions": 3072,
        "max_input": 8191,
        "cost_per_1k_tokens": 0.00013
    }
}
```

### Chunking Strategies

#### Recursive Text Splitter
```bash
# Best for most documents
CHUNKING_STRATEGY=recursive
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
CHUNK_SEPARATORS="\n\n,\n, ,"
```

#### Character Text Splitter
```bash
# Simple character-based splitting
CHUNKING_STRATEGY=character
CHUNK_SIZE=1000
CHUNK_OVERLAP=100
```

#### Token-based Splitter
```bash
# Token-aware splitting
CHUNKING_STRATEGY=token
CHUNK_SIZE=500  # tokens, not characters
CHUNK_OVERLAP=50
```

### RAG Strategies

#### Similarity Search
```bash
# Standard similarity search
RAG_STRATEGY=similarity
RAG_TOP_K=5
```

#### Maximal Marginal Relevance (MMR)
```bash
# Diverse results with MMR
RAG_STRATEGY=mmr
RAG_TOP_K=10
RAG_LAMBDA_MULT=0.5  # Diversity vs relevance balance
```

#### Similarity Score Threshold
```bash
# Filter by similarity score
RAG_STRATEGY=similarity_score_threshold
RAG_SIMILARITY_THRESHOLD=0.8
RAG_TOP_K=20  # Maximum to consider
```

## 🎯 Configuration Profiles

### Development Profile
```bash
# Development settings
DEBUG=true
LOG_LEVEL=DEBUG
OPENAI_MODEL=gpt-3.5-turbo  # Faster and cheaper
RAG_TOP_K=3  # Fewer results for faster testing
CHUNK_SIZE=500  # Smaller chunks for testing
MAX_FILE_SIZE_MB=10  # Smaller files for testing
```

### Production Profile
```bash
# Production settings
DEBUG=false
LOG_LEVEL=INFO
OPENAI_MODEL=gpt-4  # Better quality
RAG_TOP_K=5  # Optimal balance
CHUNK_SIZE=1000  # Standard chunk size
MAX_FILE_SIZE_MB=100  # Full file size support
LANGCHAIN_TRACING_V2=true  # Enable monitoring
```

### High-Performance Profile
```bash
# High-performance settings
OPENAI_MODEL=gpt-4-turbo  # Fastest GPT-4 variant
EMBEDDING_BATCH_SIZE=200  # Larger batches
RAG_TOP_K=10  # More context
CHUNK_SIZE=1500  # Larger chunks
CHUNK_OVERLAP=300  # More overlap
```

## 🔒 Security Configuration

### API Key Management

#### Environment Variables (Recommended)
```bash
# Use environment variables
export OPENAI_API_KEY="sk-your-key-here"
export PINECONE_API_KEY="your-pinecone-key"
```

#### Secret Management Services
```bash
# AWS Secrets Manager
AWS_SECRET_NAME=document-chatbot-secrets
AWS_REGION=us-west-2

# Azure Key Vault
AZURE_KEY_VAULT_URL=https://your-vault.vault.azure.net/

# Google Secret Manager
GOOGLE_PROJECT_ID=your-project-id
```

### Access Control
```bash
# Enable authentication
ENABLE_AUTH=true
AUTH_METHOD=oauth  # Options: oauth, basic, api_key

# Session security
SESSION_ENCRYPTION=true
SESSION_SECRET_KEY=your-secret-key-here

# Rate limiting
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS=100  # Requests per hour
```

## 📊 Monitoring Configuration

### Logging Configuration
```bash
# Logging settings
LOG_LEVEL=INFO
LOG_FORMAT=json  # Options: json, text
LOG_FILE=./logs/app.log
LOG_ROTATION=daily  # Options: daily, weekly, size
LOG_MAX_SIZE=100MB
LOG_BACKUP_COUNT=7
```

### Metrics Configuration
```bash
# Enable metrics collection
METRICS_ENABLED=true
METRICS_PORT=9090
METRICS_PATH=/metrics

# Performance tracking
TRACK_RESPONSE_TIME=true
TRACK_TOKEN_USAGE=true
TRACK_ERROR_RATE=true
```

### Health Checks
```bash
# Health check configuration
HEALTH_CHECK_ENABLED=true
HEALTH_CHECK_PATH=/health
HEALTH_CHECK_INTERVAL=30  # seconds

# Dependency checks
CHECK_OPENAI_API=true
CHECK_PINECONE_API=true
CHECK_DATABASE_CONNECTION=true
```

## 🚀 Performance Tuning

### Memory Optimization
```bash
# Memory settings
MAX_MEMORY_USAGE=2GB
GARBAGE_COLLECTION_THRESHOLD=0.8
CACHE_SIZE=1000  # Number of cached embeddings
CACHE_TTL=3600  # Cache time-to-live in seconds
```

### Concurrency Settings
```bash
# Concurrent processing
MAX_CONCURRENT_REQUESTS=10
THREAD_POOL_SIZE=4
ASYNC_PROCESSING=true

# Batch processing
BATCH_SIZE=50
BATCH_TIMEOUT=30  # seconds
```

### Caching Configuration
```bash
# Enable caching
CACHE_ENABLED=true
CACHE_TYPE=redis  # Options: memory, redis, file

# Redis configuration (if using Redis)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=your-redis-password
```

## 🔧 Configuration Validation

### Required Settings Check

The application validates required settings on startup:

```python
# Required environment variables
REQUIRED_VARS = [
    "OPENAI_API_KEY",
    "PINECONE_API_KEY",
    "PINECONE_ENVIRONMENT",
    "PINECONE_INDEX_NAME"
]
```

### Configuration Testing

Test your configuration:

```bash
# Test OpenAI connection
python -c "from utils.config import load_config; config = load_config(); print('OpenAI configured:', bool(config.openai.api_key))"

# Test Pinecone connection
python -c "from utils.pinecone_client import test_connection; test_connection()"

# Validate all settings
python -c "from utils.config import validate_config; validate_config()"
```

## 🐳 Docker Configuration

### Docker Compose Environment

```yaml
# docker-compose.yml environment section
environment:
  - OPENAI_API_KEY=${OPENAI_API_KEY}
  - PINECONE_API_KEY=${PINECONE_API_KEY}
  - PINECONE_ENVIRONMENT=${PINECONE_ENVIRONMENT}
  - PINECONE_INDEX_NAME=${PINECONE_INDEX_NAME}
  - DEBUG=false
  - LOG_LEVEL=INFO
```

### Kubernetes Configuration

```yaml
# ConfigMap for non-sensitive data
apiVersion: v1
kind: ConfigMap
metadata:
  name: chatbot-config
data:
  OPENAI_MODEL: "gpt-4"
  CHUNK_SIZE: "1000"
  RAG_TOP_K: "5"
  DEBUG: "false"

---
# Secret for sensitive data
apiVersion: v1
kind: Secret
metadata:
  name: chatbot-secrets
type: Opaque
data:
  OPENAI_API_KEY: <base64-encoded-key>
  PINECONE_API_KEY: <base64-encoded-key>
```

## 🔍 Troubleshooting Configuration

### Common Issues

#### Missing API Keys
```bash
# Error: OpenAI API key not found
# Solution: Set the environment variable
export OPENAI_API_KEY="your-key-here"
```

#### Invalid Pinecone Configuration
```bash
# Error: Pinecone index not found
# Solution: Verify index name and environment
echo $PINECONE_INDEX_NAME
echo $PINECONE_ENVIRONMENT
```

#### Model Configuration Issues
```bash
# Error: Model not available
# Solution: Check model name and availability
OPENAI_MODEL=gpt-4  # Ensure correct model name
```

### Configuration Debugging

```bash
# Enable debug mode
DEBUG=true
LOG_LEVEL=DEBUG

# Check configuration loading
python -c "from utils.config import load_config; config = load_config(); print(config)"

# Validate environment variables
env | grep -E '(OPENAI|PINECONE|LANGCHAIN)'
```

## 📚 Configuration Reference

### Complete Environment Variable List

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `OPENAI_API_KEY` | string | required | OpenAI API key |
| `OPENAI_MODEL` | string | gpt-4 | OpenAI model name |
| `OPENAI_TEMPERATURE` | float | 0.7 | Response creativity |
| `OPENAI_MAX_TOKENS` | int | 1000 | Max response tokens |
| `PINECONE_API_KEY` | string | required | Pinecone API key |
| `PINECONE_ENVIRONMENT` | string | required | Pinecone environment |
| `PINECONE_INDEX_NAME` | string | required | Pinecone index name |
| `EMBEDDING_MODEL` | string | text-embedding-ada-002 | Embedding model |
| `CHUNK_SIZE` | int | 1000 | Text chunk size |
| `CHUNK_OVERLAP` | int | 200 | Chunk overlap |
| `RAG_TOP_K` | int | 5 | Retrieved documents |
| `MAX_FILE_SIZE_MB` | int | 100 | Max upload size |
| `DEBUG` | bool | false | Debug mode |
| `LOG_LEVEL` | string | INFO | Logging level |

---

**Next Steps**:
- [Troubleshooting Guide](./troubleshooting.md) for common issues
- [API Reference](./api-reference.md) for technical details
- [Development Guide](./development.md) for contributors