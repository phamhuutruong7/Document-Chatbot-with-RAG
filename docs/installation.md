# 🔧 Installation Guide

## Prerequisites

Before installing the Document Chatbot application, ensure you have the following:

### System Requirements
- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: At least 2GB free space
- **Internet**: Stable internet connection for API calls

### Required API Keys
- **OpenAI API Key**: For LLM and embedding services
- **Pinecone API Key**: For vector database operations
- **LangSmith API Key**: (Optional) For advanced tracing

## 🚀 Quick Installation (Windows)

### Option 1: Automated Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd workshop
   ```

2. **Run the setup script**
   ```bash
   setup.bat
   ```
   This script will:
   - Create a Python virtual environment
   - Install all required dependencies
   - Set up the basic directory structure

3. **Configure environment variables** (see [Configuration](#configuration) section)

4. **Start the application**
   ```bash
   streamlit run main.py
   ```

### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd workshop
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create data directory**
   ```bash
   mkdir data
   ```

## 🐧 Linux/macOS Installation

### Using pip

1. **Clone and navigate**
   ```bash
   git clone <repository-url>
   cd workshop
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up directories**
   ```bash
   mkdir -p data
   ```

### Using conda

1. **Create conda environment**
   ```bash
   conda create -n document-chatbot python=3.9
   conda activate document-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🐳 Docker Installation

### Using Docker Compose (Recommended)

1. **Create docker-compose.yml**
   ```yaml
   version: '3.8'
   services:
     document-chatbot:
       build: .
       ports:
         - "8501:8501"
       environment:
         - OPENAI_API_KEY=${OPENAI_API_KEY}
         - PINECONE_API_KEY=${PINECONE_API_KEY}
         - PINECONE_INDEX_NAME=${PINECONE_INDEX_NAME}
       volumes:
         - ./data:/app/data
         - ./.env:/app/.env
   ```

2. **Build and run**
   ```bash
   docker-compose up --build
   ```

### Using Docker directly

1. **Build the image**
   ```bash
   docker build -t document-chatbot .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 \
     -e OPENAI_API_KEY=your_key \
     -e PINECONE_API_KEY=your_key \
     -e PINECONE_INDEX_NAME=your_index \
     -v $(pwd)/data:/app/data \
     document-chatbot
   ```

## ⚙️ Configuration

### Environment Variables Setup

1. **Create .env file**
   ```bash
   cp .env.example .env
   ```

2. **Edit .env file with your credentials**
   ```env
   # OpenAI Configuration
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-3.5-turbo
   OPENAI_TEMPERATURE=0.7
   OPENAI_MAX_TOKENS=1000
   
   # Pinecone Configuration
   PINECONE_API_KEY=your_pinecone_api_key_here
   PINECONE_INDEX_NAME=your_index_name_here
   PINECONE_ENVIRONMENT=your_environment_here
   
   # Embedding Configuration
   EMBEDDING_MODEL=text-embedding-ada-002
   EMBEDDING_BATCH_SIZE=100
   
   # Application Settings
   MAX_FILE_SIZE_MB=100
   CHUNK_SIZE=1000
   CHUNK_OVERLAP=200
   RAG_TOP_K=5
   
   # Optional: LangSmith Tracing
   LANGCHAIN_TRACING_V2=false
   LANGCHAIN_API_KEY=your_langsmith_key_here
   LANGCHAIN_PROJECT=document-chatbot
   ```

### API Key Setup Guide

#### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

#### Pinecone API Key
1. Visit [Pinecone Console](https://app.pinecone.io/)
2. Sign up or log in to your account
3. Create a new project or use existing
4. Create a new index with:
   - **Dimension**: 1536 (for OpenAI embeddings)
   - **Metric**: cosine
   - **Pod Type**: s1.x1 (starter)
5. Copy API key and index details to `.env` file

#### LangSmith Setup (Optional)
1. Visit [LangSmith](https://smith.langchain.com/)
2. Sign up for an account
3. Create a new project
4. Generate API key
5. Add to `.env` file

## 📦 Dependencies

### Core Dependencies
```
streamlit>=1.28.0
langchain>=0.0.350
langchain-openai>=0.0.2
openai>=1.0.0
pinecone-client>=2.2.4
pydantic>=2.0.0
python-dotenv>=1.0.0
```

### Document Processing
```
PyMuPDF>=1.23.0
python-docx>=0.8.11
```

### Data Visualization
```
plotly>=5.17.0
pandas>=2.0.0
```

### Development Dependencies
```
pytest>=7.4.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.5.0
```

## 🔍 Verification

### Test Installation

1. **Check Python version**
   ```bash
   python --version
   # Should show Python 3.8+
   ```

2. **Verify dependencies**
   ```bash
   pip list | grep streamlit
   pip list | grep langchain
   pip list | grep openai
   pip list | grep pinecone
   ```

3. **Test configuration**
   ```bash
   python -c "from utils.config import load_config; print('Config loaded successfully')"
   ```

4. **Run application**
   ```bash
   streamlit run main.py
   ```
   - Application should start on `http://localhost:8501`
   - No configuration errors should appear

### Health Check

Once the application is running:

1. **UI Loading**: Verify the Streamlit interface loads properly
2. **API Connectivity**: Upload a small test document
3. **Vector Storage**: Confirm document processing completes
4. **Query Testing**: Ask a simple question about the document
5. **Response Generation**: Verify AI response is generated

## 🐛 Troubleshooting

### Common Installation Issues

#### Python Version Issues
```bash
# Check Python version
python --version

# If using Python 3.8+, ensure pip is updated
python -m pip install --upgrade pip
```

#### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf venv  # or rmdir /s venv on Windows
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### Dependency Conflicts
```bash
# Clear pip cache
pip cache purge

# Install with no cache
pip install --no-cache-dir -r requirements.txt

# Force reinstall
pip install --force-reinstall -r requirements.txt
```

#### PyMuPDF Installation Issues
```bash
# On some systems, you might need:
pip install --upgrade pymupdf

# Or install system dependencies first (Linux)
sudo apt-get install python3-dev
```

### Configuration Issues

#### Missing API Keys
- Verify `.env` file exists and contains all required keys
- Check for typos in environment variable names
- Ensure no extra spaces around the `=` sign

#### Pinecone Connection Issues
- Verify index name and environment are correct
- Check if index dimension matches embedding model (1536 for OpenAI)
- Ensure Pinecone plan supports required features

#### OpenAI API Issues
- Verify API key is valid and has sufficient credits
- Check rate limits and usage quotas
- Ensure model names are correct

## 🚀 Next Steps

After successful installation:

1. **Read the [User Guide](./user-guide.md)** to learn how to use the application
2. **Check [Configuration](./configuration.md)** for advanced settings
3. **Review [Architecture](./architecture.md)** to understand the system
4. **See [Development Guide](./development.md)** if you plan to contribute

## 📞 Support

If you encounter issues during installation:

1. Check the [Troubleshooting Guide](./troubleshooting.md)
2. Review the [FAQ section](./troubleshooting.md#faq)
3. Search existing GitHub issues
4. Create a new issue with:
   - Operating system and Python version
   - Complete error message
   - Steps to reproduce the issue

---

**Next**: [User Guide](./user-guide.md) | [Configuration](./configuration.md)