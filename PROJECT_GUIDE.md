# Document Chatbot with RAG - Complete Project Guide

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Using the Chatbot](#using-the-chatbot)
- [Document Management](#document-management)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [API Reference](#api-reference)
- [Contributing](#contributing)

## 🎯 Project Overview

This is a **Retrieval-Augmented Generation (RAG) chatbot** designed for PC customer support. The system combines:

- **Document Knowledge Base**: Pre-loaded with comprehensive PC support documentation
- **Vector Database**: Pinecone for efficient document retrieval
- **LLM Integration**: OpenAI GPT models for intelligent responses
- **Web Interface**: Streamlit-based user-friendly chat interface
- **Session Management**: Multiple conversation sessions with document tracking

### Key Features
- ✅ **Intelligent Q&A**: Ask questions about PC troubleshooting, building, and support
- ✅ **Document Upload**: Add new manuals, guides, and documentation
- ✅ **Session Tracking**: Maintain conversation history and context
- ✅ **Source Attribution**: See which documents were used for each answer
- ✅ **Advanced Analytics**: Monitor RAG performance and retrieval quality
- ✅ **Command System**: Special commands for system operations

---

## 🔧 Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 2GB free space for documents and cache
- **Internet**: Stable connection for API calls

### Required API Keys
1. **OpenAI API Key**: For GPT models
   - Get from: https://platform.openai.com/api-keys
   - Or use compatible API (like Azure OpenAI)

2. **Pinecone API Key**: For vector database
   - Get from: https://www.pinecone.io/
   - Create a free account and index

3. **Embedding API Key**: For text embeddings
   - Can use OpenAI embeddings or compatible service

---

## 🚀 Installation & Setup

### Step 1: Clone and Navigate
```bash
# Clone the repository (if from git)
git clone <repository-url>
cd Document-Chatbot-with-RAG

# Or navigate to your project folder
cd d:\Projects\Document-Chatbot-with-RAG
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Verify key packages are installed
pip list | grep -E "streamlit|openai|langchain|pinecone"
```

### Step 4: Verify Installation
```bash
# Check Python version
python --version

# Check Streamlit installation
streamlit --version

# Test imports
python -c "import streamlit, openai, langchain, pinecone; print('✅ All packages imported successfully')"
```

---

## ⚙️ Configuration

### Step 1: Environment Variables
Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` with your API keys:
```env
# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_BASE_URL=https://api.openai.com/v1

# Pinecone Configuration
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_ENVIRONMENT=us-east-1-aws
PINECONE_INDEX_NAME=document-chat

# Embedding Configuration
EMBEDDING_API_KEY=your-embedding-api-key-here
EMBEDDING_MODEL=text-embedding-ada-002
EMBEDDING_BASE_URL=https://api.openai.com/v1

# Application Settings
APP_DEBUG=false
LOG_LEVEL=INFO
```

### Step 2: Verify Configuration
```bash
# Test configuration loading
python -c "from utils.config import load_config; print('✅ Configuration loaded successfully')"
```

### Step 3: Initialize Pinecone Index
If you haven't created a Pinecone index yet:

1. Log into [Pinecone Console](https://app.pinecone.io/)
2. Create a new index:
   - **Name**: `document-chat`
   - **Dimensions**: `1536` (for OpenAI embeddings)
   - **Metric**: `cosine`
   - **Environment**: Choose your preferred region

---

## 🏃‍♂️ Running the Application

### Step 1: Upload Documents to Knowledge Base
First, ensure your knowledge base is populated:

```bash
# Upload all documents to Pinecone (one-time setup)
python scripts/simple_upload_to_pinecone.py
```

Expected output:
```
🚀 UPLOADING KNOWLEDGE BASE TO PINECONE
✅ Pinecone client initialized successfully!
📄 Found 20 text documents
📊 UPLOAD COMPLETE!
📁 Files Processed: 20/20
📄 Total Chunks Created: 37
☁️ Chunks Uploaded: 37
🎉 SUCCESS! Your knowledge base is now in Pinecone!
```

### Step 2: Start the Streamlit Application
```bash
# Run the main application
streamlit run main.py
```

### Step 3: Access the Web Interface
Open your browser and navigate to:
- **Local URL**: http://localhost:8501
- **Network URL**: http://[your-ip]:8501

### Alternative: Custom Port
If port 8501 is busy:
```bash
streamlit run main.py --server.port 8502
```

---

## 💬 Using the Chatbot

### Getting Started

1. **Open the Application**: Navigate to http://localhost:8501
2. **Start New Session**: Click "New Session" in the sidebar
3. **Ask Your First Question**: Type a question in the chat input

### Sample Questions for PC Support

#### 🔧 Hardware Troubleshooting
```
• "How do I diagnose PSU voltage issues?"
• "What are the steps for systematic PC troubleshooting?"
• "My computer won't turn on, what should I check first?"
• "How to test memory with MemTest86?"
• "CPU temperature monitoring best practices"
```

#### 🖥️ PC Building & Compatibility
```
• "What components do I need for a gaming PC under $1500?"
• "How do I check motherboard compatibility with my CPU?"
• "Best practices for CPU installation"
• "RAM compatibility and timing considerations"
• "GPU clearance and power requirements"
```

#### 🛠️ Customer Support Scenarios
```
• "Customer's computer is running slow, troubleshooting steps?"
• "How do I handle warranty claims for defective components?"
• "Network connectivity troubleshooting guide"
• "BIOS update procedures and risks"
• "Data recovery options for failed drives"
```

### Understanding Responses

Each chatbot response includes:
- **Main Answer**: Comprehensive response to your question
- **Source Documents**: Which knowledge base documents were referenced
- **Confidence Score**: How confident the system is in the answer
- **Related Topics**: Suggestions for follow-up questions

### Chat Interface Features

#### Sidebar Navigation
- **New Session**: Start fresh conversation
- **Session History**: View and resume previous chats
- **Document Manager**: Upload and manage documents
- **Settings**: Adjust response parameters
- **Analytics**: View usage statistics

#### Chat Commands
Use special commands for advanced operations:
```
/help          - Show available commands
/status        - System status and statistics
/clear         - Clear current conversation
/export        - Export conversation history
/upload        - Quick file upload dialog
/search [term] - Search knowledge base directly
```

---

## 📁 Document Management

### Uploading New Documents

#### Via Web Interface
1. Click "📄 Upload Document" in the sidebar
2. Select your file (PDF, TXT, DOCX, MD)
3. Wait for processing confirmation
4. Document is automatically chunked and indexed

#### Via Script (Bulk Upload)
```bash
# Upload multiple documents
python scripts/upload_to_pinecone.py

# Upload specific directory
python scripts/upload_to_pinecone.py --directory "path/to/docs"
```

### Supported File Types
- **PDF**: `.pdf` - Manuals, datasheets, guides
- **Text**: `.txt` - Plain text documentation
- **Word**: `.docx` - Microsoft Word documents
- **Markdown**: `.md` - Technical documentation

### Document Processing Pipeline
1. **File Parsing**: Extract text content
2. **Text Chunking**: Split into manageable pieces
3. **Embedding Generation**: Convert to vector representations
4. **Pinecone Upload**: Store in vector database
5. **Metadata Indexing**: Add searchable metadata

### Managing Knowledge Base
```bash
# View uploaded documents
python scripts/list_documents.py

# Remove documents by session
python scripts/cleanup_session.py --session-id <session_id>

# Backup knowledge base
python scripts/backup_pinecone.py
```

---

## 🎛️ Advanced Features

### Session Management

#### Creating Sessions
- **Auto Session**: System creates session automatically
- **Named Session**: Provide custom session name
- **Session Types**: Support, Training, Development

#### Session Analytics
View detailed metrics:
- **Message Count**: Total questions and responses
- **Response Time**: Average processing time
- **Document Usage**: Most referenced sources
- **User Satisfaction**: Feedback ratings

### RAG Performance Monitoring

#### Retrieval Quality
- **Relevance Score**: How well retrieved documents match query
- **Coverage**: Percentage of query topics covered
- **Source Diversity**: Number of different documents used

#### Generation Quality
- **Coherence**: Response clarity and structure
- **Accuracy**: Factual correctness verification
- **Completeness**: Whether all query aspects addressed

### Command System

#### Available Commands
```bash
/help                    # Show all available commands
/status                  # System health and statistics
/clear                   # Clear current conversation
/export [format]         # Export chat (json, csv, txt)
/upload                  # Quick file upload
/search [query]          # Direct knowledge base search
/stats                   # Detailed session statistics
/feedback [rating]       # Provide response rating
/debug                   # Enable debug mode
/config                  # Show current configuration
```

#### Example Usage
```
User: /search motherboard compatibility
System: Found 5 relevant documents about motherboard compatibility...

User: /stats
System: Session Statistics:
- Messages: 15
- Avg Response Time: 2.3s
- Documents Used: 8
- Satisfaction: 4.2/5
```

### Integration Options

#### API Access
The system provides REST API endpoints:
```python
# Example API usage
import requests

response = requests.post("http://localhost:8501/api/chat", {
    "message": "How to troubleshoot RAM issues?",
    "session_id": "support_session_001"
})
```

#### Webhook Integration
Configure webhooks for external systems:
```json
{
  "webhook_url": "https://your-system.com/webhook",
  "events": ["new_message", "session_end", "document_upload"],
  "auth_token": "your-webhook-token"
}
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Application Won't Start
**Error**: `ModuleNotFoundError: No module named 'streamlit'`
```bash
# Solution: Install dependencies
pip install -r requirements.txt

# Or install specific package
pip install streamlit
```

#### 2. API Key Issues
**Error**: `Invalid API key` or `Authentication failed`
```bash
# Check .env file exists and has correct keys
cat .env

# Verify API key format
echo $OPENAI_API_KEY

# Test API connectivity
python -c "import openai; print('API key valid')"
```

#### 3. Pinecone Connection Issues
**Error**: `Failed to connect to Pinecone`
```bash
# Check Pinecone configuration
python scripts/test_pinecone.py

# Verify index exists
python -c "from utils.pinecone_client import PineconeClient; pc = PineconeClient(); print('Connected successfully')"
```

#### 4. Memory Issues
**Error**: `Out of memory` or slow performance
```bash
# Monitor memory usage
python scripts/memory_monitor.py

# Reduce batch size in config
# Edit utils/config.py: batch_size = 50 (instead of 100)

# Clear cache
rm -rf __pycache__/ .streamlit/
```

#### 5. Port Already in Use
**Error**: `Port 8501 is already in use`
```bash
# Use different port
streamlit run main.py --server.port 8502

# Or find and kill process using port
netstat -ano | findstr :8501
taskkill /PID <process_id> /F
```

### Debug Mode

Enable debug logging:
```bash
# Set environment variable
export LOG_LEVEL=DEBUG

# Or modify .env file
echo "LOG_LEVEL=DEBUG" >> .env

# Run with verbose output
streamlit run main.py --logger.level=debug
```

### Log Files

Check log files for detailed error information:
```bash
# Application logs
tail -f logs/application.log

# Pinecone upload logs
tail -f logs/pinecone_upload.log

# Session logs
ls -la logs/sessions/
```

### Performance Optimization

#### For Large Document Sets
```python
# In utils/config.py, adjust these settings:
chunk_size = 800          # Smaller chunks for better retrieval
batch_size = 50           # Smaller batches for memory efficiency
max_retrieval_docs = 5    # Fewer documents per query
```

#### For Slow Responses
```python
# In utils/config.py:
embedding_cache = True    # Enable embedding cache
response_timeout = 30     # Increase timeout
parallel_processing = True # Enable parallel document processing
```

### Getting Help

#### System Status Check
```bash
# Run comprehensive system check
python scripts/system_check.py
```

#### Generate Support Report
```bash
# Create detailed report for troubleshooting
python scripts/generate_support_report.py
```

Output includes:
- System configuration
- Installed packages
- API connectivity status
- Recent error logs
- Performance metrics

---

## 🔌 API Reference

### REST Endpoints

#### Chat API
```http
POST /api/chat
Content-Type: application/json

{
  "message": "How to troubleshoot RAM issues?",
  "session_id": "optional_session_id",
  "stream": false
}
```

Response:
```json
{
  "response": "To troubleshoot RAM issues...",
  "sources": [
    {"document": "ram_troubleshooting.pdf", "relevance": 0.95},
    {"document": "hardware_diagnostics.txt", "relevance": 0.87}
  ],
  "session_id": "session_12345",
  "processing_time": 2.3
}
```

#### Document Upload API
```http
POST /api/upload
Content-Type: multipart/form-data

file: [binary file data]
session_id: optional_session_id
```

#### Session Management API
```http
GET /api/sessions                    # List all sessions
GET /api/sessions/{session_id}       # Get specific session
POST /api/sessions                   # Create new session
DELETE /api/sessions/{session_id}    # Delete session
```

### Python SDK

```python
from utils.rag_client import RAGClient

# Initialize client
client = RAGClient(base_url="http://localhost:8501")

# Send message
response = client.chat("How to build a gaming PC?")
print(response.text)

# Upload document
client.upload_document("path/to/manual.pdf")

# List sessions
sessions = client.list_sessions()
```

---

## 🤝 Contributing

### Development Setup

```bash
# Clone for development
git clone <repository-url>
cd Document-Chatbot-with-RAG

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
python -m pytest tests/
```

### Project Structure
```
Document-Chatbot-with-RAG/
├── main.py                 # Streamlit application entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── PROJECT_GUIDE.md       # This guide
├── utils/                 # Core utilities
│   ├── config.py          # Configuration management
│   ├── pinecone_client.py # Vector database client
│   ├── embeddings.py      # Embedding generation
│   ├── chunker.py         # Text chunking
│   ├── langchain_agents.py # RAG agent
│   └── session_manager.py # Session handling
├── scripts/               # Utility scripts
│   ├── simple_upload_to_pinecone.py
│   ├── upload_to_pinecone.py
│   └── test_pinecone.py
├── data/                  # Data directory
│   └── documents/         # Knowledge base documents
├── logs/                  # Application logs
└── tests/                 # Unit tests
```

### Adding New Features

#### 1. New Document Parser
```python
# In utils/file_parser.py
def parse_new_format(file_path: str) -> str:
    """Parse new document format"""
    # Implementation here
    pass
```

#### 2. Custom RAG Strategy
```python
# In utils/rag_strategies.py
class CustomRAGStrategy:
    def retrieve_and_generate(self, query: str) -> str:
        # Custom RAG implementation
        pass
```

#### 3. New Command
```python
# In utils/commands.py
@command("mycommand")
def handle_my_command(args: str) -> str:
    """Handle custom command"""
    return f"Executed: {args}"
```

### Testing

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_rag_agent.py

# Run with coverage
python -m pytest --cov=utils tests/
```

### Code Quality

```bash
# Format code
black utils/ scripts/ tests/

# Check style
flake8 utils/ scripts/ tests/

# Type checking
mypy utils/
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- **Issues**: Create an issue on GitHub
- **Documentation**: Check this guide and inline documentation
- **Community**: Join our discussion forum

---

## 🎉 Quick Start Summary

1. **Install**: `pip install -r requirements.txt`
2. **Configure**: Edit `.env` with your API keys
3. **Upload Docs**: `python scripts/simple_upload_to_pinecone.py`
4. **Run**: `streamlit run main.py`
5. **Use**: Open http://localhost:8501 and start chatting!

**Happy Chatting!** 🤖💬
