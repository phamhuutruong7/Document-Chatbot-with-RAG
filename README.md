# 📄 Document Chatbot with RAG + Pinecone + Streamlit

A powerful web-based chatbot application that allows users to upload documents (PDF, DOCX, TXT) and ask questions about their contents using Retrieval-Augmented Generation (RAG) with Pinecone vector database and OpenAI GPT-4.

## 📚 Documentation

For comprehensive documentation, visit the **[docs/](./docs/)** folder:

- **[📋 Project Overview](./docs/project-overview.md)** - High-level project description and goals
- **[🏗️ System Architecture](./docs/architecture.md)** - Technical architecture and component details
- **[⚙️ Installation Guide](./docs/installation.md)** - Complete setup instructions for all platforms
- **[👤 User Guide](./docs/user-guide.md)** - How to use the application effectively
- **[🔧 Configuration](./docs/configuration.md)** - Environment variables and settings
- **[🛠️ Development Guide](./docs/development.md)** - For developers and contributors
- **[📊 System Diagrams](./docs/diagrams/)** - Visual architecture diagrams (Mermaid format)
- **[🔍 API Reference](./docs/api-reference.md)** - Detailed code documentation
- **[🚨 Troubleshooting](./docs/troubleshooting.md)** - Common issues and solutions

## 🚀 Quick Start

1. **📖 Read the [Project Overview](./docs/project-overview.md)** to understand the application
2. **⚙️ Follow the [Installation Guide](./docs/installation.md)** to set up your environment
3. **👤 Check the [User Guide](./docs/user-guide.md)** to learn how to use the features
4. **🔧 Configure using the [Configuration Guide](./docs/configuration.md)** for customization

> **Need Help?** Check the [Troubleshooting Guide](./docs/troubleshooting.md) or browse the [System Diagrams](./docs/diagrams/) for visual understanding.

## 🚀 Features

- **Multi-format Document Support**: Upload PDF, DOCX, and TXT files
- **Intelligent Q&A**: Ask questions about your documents using natural language
- **Vector Search**: Powered by Pinecone for fast and accurate document retrieval
- **Chat History**: Persistent conversation history across sessions
- **Special Commands**: Built-in commands for document analysis
- **Modern UI**: Clean and intuitive Streamlit interface

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: OpenAI GPT-4
- **Embeddings**: OpenAI text-embedding-ada-002
- **Vector Database**: Pinecone
- **Document Processing**: PyMuPDF, python-docx
- **Framework**: LangChain

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Pinecone API key and environment

## 🔧 Installation

### Option 1: Quick Setup (Windows)

1. **Run the setup script**
   ```bash
   setup.bat
   ```
   This will create a virtual environment and install all dependencies.

2. **Configure your API keys** (see step 3 below)

3. **Start the application**
   ```bash
   run.bat
   ```

### Option 2: Manual Setup

1. **Clone or download the project**
   ```bash
   cd document-chatbot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root and add your API keys:
   ```env
   # OpenAI API Configuration for Chat
   OPENAI_API_KEY=sk-your-openai-api-key-here
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_MODEL=gpt-4
   
   # Text Embedding API Configuration
   EMBEDDING_API_KEY=sk-your-embedding-api-key-here
   EMBEDDING_BASE_URL=https://api.openai.com/v1
   EMBEDDING_MODEL=text-embedding-ada-002
   
   # Pinecone Configuration
   PINECONE_API_KEY=your-pinecone-api-key-here
   PINECONE_INDEX_NAME=document-chat
   
   # LangSmith Configuration (Optional - for tracing)
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_API_KEY=your-langsmith-api-key-here
   LANGCHAIN_PROJECT=document-chatbot
   ```

5. **Get API Keys**
   
   **OpenAI API Keys:**
   - Visit [OpenAI API](https://platform.openai.com/api-keys)
   - Create an account and generate API keys
   - You can use the same key for both `OPENAI_API_KEY` and `EMBEDDING_API_KEY`
   - Or use different keys if you have separate accounts/billing
   - Customize `OPENAI_BASE_URL` and `EMBEDDING_BASE_URL` for custom endpoints
   
   **Pinecone API Key:**
   - Visit [Pinecone](https://www.pinecone.io/)
   - Create an account and get your API key
   
   **LangSmith API Key (Optional):**
   - Visit [LangSmith](https://smith.langchain.com/)
   - Create an account and get your API key
   - Used for tracing and monitoring LLM calls
   - Set `LANGCHAIN_TRACING_V2=false` to disable tracing

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

3. **Upload documents**
   
   - Use the sidebar to upload PDF, DOCX, or TXT files
   - Click "Process [filename]" to analyze and store the document

4. **Start chatting**
   
   - Ask questions about your uploaded documents
   - Use special commands for advanced features

## 🔧 Special Commands

| Command | Description | Example |
|---------|-------------|----------|
| `/summarize` | Generate a summary of all uploaded documents | `/summarize` |
| `/list-sections` | List section headers from documents | `/list-sections` |
| `/translate [lang]` | Translate content to specified language | `/translate vi` |
| `/clear` | Clear chat history | `/clear` |
| `/help` | Show available commands | `/help` |

### Supported Languages for Translation
- `vi` (Vietnamese)
- `en` (English)
- `es` (Spanish)
- `fr` (French)
- `de` (German)
- `zh` (Chinese)
- `ja` (Japanese)
- `ko` (Korean)

## 📁 Project Structure

```
document-chatbot/
├── main.py                     # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── README.md                   # This file
├── utils/                      # Utility modules
│   ├── __init__.py
│   ├── config.py              # Pydantic configuration management
│   ├── file_parser.py         # Document parsing (PDF, DOCX, TXT)
│   ├── chunker.py             # Text chunking utilities
│   ├── embeddings.py          # OpenAI embeddings integration
│   ├── pinecone_client.py     # Pinecone vector database client
│   ├── langchain_agents.py    # LangChain RAG agent implementation
│   ├── session_manager.py     # Session management and persistence
│   ├── rag_tracer.py          # RAG performance tracing
│   ├── commands.py            # Special command handlers
│   └── decorators.py          # Error handling and performance decorators
├── docs/                       # Documentation
│   ├── diagrams/              # System diagrams (.mmd files)
│   └── *.md                   # Various documentation files
└── data/                       # Session and chat data
    └── sessions/              # Individual session files
```

## 🔍 How It Works

1. **Document Upload**: Users upload documents through the Streamlit interface
2. **Text Extraction**: Documents are parsed and text content is extracted
3. **Chunking**: Text is split into manageable chunks with overlap
4. **Embedding**: Each chunk is converted to vector embeddings using OpenAI
5. **Storage**: Embeddings are stored in Pinecone with metadata
6. **Query Processing**: User questions are embedded and used to search similar chunks
7. **Response Generation**: Retrieved chunks provide context for GPT-4 to generate answers

## 🎯 Example Use Cases

- **Legal Document Review**: Upload contracts and ask specific questions
- **Research Analysis**: Upload research papers and get summaries
- **Knowledge Management**: Create a searchable knowledge base
- **Study Assistant**: Upload textbooks and ask study questions

## 🔒 Security Notes

- This version uses a global session (no user authentication)
- All uploaded documents are shared among users
- Suitable for personal use or trusted internal environments
- For production use, implement proper user authentication and data isolation

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'fitz'" error**
   ```bash
   pip install PyMuPDF
   ```

2. **Pinecone connection errors**
   - Verify your API key and environment in `.env`
   - Check if your Pinecone plan supports the required features

3. **OpenAI API errors**
   - Ensure you have sufficient API credits
   - Verify your API key is correct

4. **Large file processing issues**
   - Files are chunked automatically, but very large files may take time
   - Consider splitting extremely large documents

### Performance Tips

- **Optimal chunk size**: Default 1000 tokens works well for most documents
- **Batch processing**: Upload multiple related documents for better context
- **Query specificity**: More specific questions yield better results

## 📈 Future Enhancements

- User authentication and multi-tenancy
- Support for more file formats (Excel, PowerPoint)
- Advanced filtering and search options
- Document versioning and updates
- Export conversation history
- Custom embedding models

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## 📄 License

This project is open source and available under the MIT License.

## 📖 Additional Resources

### 🎯 For Users
- Start with the **[User Guide](./docs/user-guide.md)** for step-by-step instructions
- Check **[Configuration](./docs/configuration.md)** for customization options
- Visit **[Troubleshooting](./docs/troubleshooting.md)** if you encounter issues

### 🛠️ For Developers
- Review the **[System Architecture](./docs/architecture.md)** for technical details
- Follow the **[Development Guide](./docs/development.md)** for contribution guidelines
- Explore **[API Reference](./docs/api-reference.md)** for code documentation
- View **[System Diagrams](./docs/diagrams/)** for visual architecture understanding

### 📊 Visual Documentation
All system diagrams are available in **[Mermaid format](./docs/diagrams/)** for easy viewing and editing:
- System Architecture
- Component Dependencies
- Data Flow
- Sequence Diagrams

---

**Happy chatting with your documents! 🎉**

*For the complete documentation experience, visit the [docs/](./docs/) folder.*