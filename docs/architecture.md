# 🏗️ System Architecture

## Overview

The Document Chatbot with RAG system follows a layered architecture pattern with clear separation of concerns, enabling scalability, maintainability, and testability.

## 📊 Architecture Layers

### 1. Presentation Layer
- **Streamlit UI Components**: User interface for file upload, chat, and session management
- **Progress Indicators**: Real-time feedback for long-running operations
- **Error Handling**: User-friendly error messages and validation feedback

### 2. Application Layer
- **Main Application Logic**: Core application orchestration and flow control
- **Session Management**: User session handling and context preservation
- **Command Router**: Special command processing and routing
- **RAG Agent Integration**: LangChain-based agent coordination

### 3. Processing Layer
- **File Processing**: Document parsing and text extraction (PDF, DOCX, TXT)
- **Text Chunking**: Intelligent text splitting with configurable overlap
- **Embedding Generation**: Batch embedding processing with OpenAI
- **RAG Pipeline**: Retrieval-augmented generation workflow

### 4. Data Access Layer
- **Pinecone Client**: Vector database operations and index management
- **Session Storage**: JSON-based session persistence
- **RAG Tracing**: Performance monitoring and metrics collection
- **Configuration Management**: Pydantic-based settings management

### 5. Infrastructure Layer
- **External APIs**: OpenAI (LLM and embeddings), Pinecone, LangSmith
- **Error Handling**: Centralized error management with decorators
- **Performance Monitoring**: Execution time tracking and logging
- **Environment Configuration**: Secure credential and settings management

## 🔄 Data Flow

### Document Processing Flow
```
User Upload → File Validation → Text Extraction → Chunking → 
Embedding Generation → Vector Storage → Index Update
```

### Query Processing Flow
```
User Query → Query Embedding → Similarity Search → Context Retrieval → 
LLM Generation → Response Formatting → UI Display
```

## 🧩 Core Components

### Main Application (`main.py`)
- **Entry Point**: Streamlit application initialization
- **Component Orchestration**: Coordinates all system components
- **Session State Management**: Maintains application state
- **UI Layout**: Defines user interface structure

### Configuration System (`utils/config.py`)
- **Type-Safe Configuration**: Pydantic-based configuration models
- **Environment Integration**: Automatic environment variable loading
- **Validation**: Configuration validation and error reporting
- **Modular Settings**: Separate configs for different components

### RAG Agent (`utils/langchain_agents.py`)
- **Document RAG Agent**: Core RAG implementation using LangChain
- **Context Management**: Maintains conversation context
- **Retrieval Logic**: Implements similarity search and ranking
- **Generation Pipeline**: Orchestrates LLM response generation

### File Processing (`utils/file_parser.py`)
- **Multi-Format Support**: PDF, DOCX, TXT parsing
- **Text Extraction**: Clean text extraction from various formats
- **Error Handling**: Robust error handling for corrupted files
- **Section Detection**: Basic section header extraction

### Text Chunking (`utils/chunker.py`)
- **Intelligent Splitting**: Context-aware text chunking
- **Overlap Management**: Configurable chunk overlap
- **Separator Handling**: Multiple separator support
- **Size Optimization**: Optimal chunk size for embeddings

### Embedding Service (`utils/embeddings.py`)
- **Batch Processing**: Efficient batch embedding generation
- **API Integration**: OpenAI embedding API client
- **Caching**: Embedding result caching
- **Error Recovery**: Retry logic for API failures

### Vector Database (`utils/pinecone_client.py`)
- **Index Management**: Pinecone index operations
- **Vector Operations**: Upsert, query, delete operations
- **Metadata Handling**: Rich metadata storage and filtering
- **Connection Management**: Robust connection handling

### Session Management (`utils/session_manager.py`)
- **Session Lifecycle**: Create, load, save, delete sessions
- **Data Persistence**: JSON-based session storage
- **Context Preservation**: Maintains conversation history
- **Cleanup**: Automatic session cleanup and timeout handling

### Command System (`utils/commands.py`)
- **Command Router**: Routes special commands to handlers
- **Built-in Commands**: System commands for debugging and management
- **Extensible Design**: Easy addition of new commands
- **Permission System**: Command access control

### Monitoring & Tracing (`utils/rag_tracer.py`)
- **Performance Metrics**: RAG pipeline performance tracking
- **Error Tracking**: Error logging and analysis
- **Usage Analytics**: User interaction analytics
- **LangSmith Integration**: Optional advanced tracing

### Decorators (`utils/decorators.py`)
- **Error Handling**: Centralized error handling
- **Performance Monitoring**: Execution time tracking
- **Input Validation**: Type and constraint validation
- **User Action Logging**: User interaction logging

## 🔐 Security Architecture

### Authentication & Authorization
- **API Key Management**: Secure API key storage and validation
- **Environment Variables**: Credential isolation from code
- **Session Isolation**: User data separation

### Input Validation
- **File Type Validation**: Allowed file extension checking
- **Size Limits**: File size restrictions
- **Content Sanitization**: Input sanitization and validation
- **Rate Limiting**: API rate limit handling

### Data Protection
- **Temporary Storage**: Secure temporary file handling
- **Memory Management**: Efficient memory usage and cleanup
- **Error Masking**: Sensitive information protection in errors

## 📈 Scalability Considerations

### Performance Optimization
- **Batch Processing**: Efficient batch operations for embeddings
- **Caching Strategy**: Multi-level caching implementation
- **Lazy Loading**: On-demand component initialization
- **Resource Management**: Efficient resource utilization

### Horizontal Scaling
- **Stateless Design**: Stateless component architecture
- **External Storage**: Externalized state management
- **API Abstraction**: Clean API boundaries for scaling

### Monitoring & Observability
- **Metrics Collection**: Performance and usage metrics
- **Error Tracking**: Comprehensive error monitoring
- **Tracing**: Request tracing and debugging
- **Health Checks**: System health monitoring

## 🔧 Configuration Architecture

### Environment-Based Configuration
- **Development**: Local development settings
- **Production**: Production-optimized settings
- **Testing**: Test environment configuration

### Configuration Categories
- **API Configuration**: External service settings
- **Feature Flags**: Feature enable/disable flags
- **Performance Tuning**: Performance-related parameters
- **Security Settings**: Security-related configurations

## 🚀 Deployment Architecture

### Local Deployment
- **Virtual Environment**: Isolated Python environment
- **Environment Files**: Local configuration management
- **Development Server**: Streamlit development server

### Production Deployment
- **Container Support**: Docker containerization ready
- **Cloud Deployment**: Cloud platform compatibility
- **Load Balancing**: Multi-instance deployment support
- **Monitoring Integration**: Production monitoring setup

## 📊 Data Architecture

### Vector Storage
- **Pinecone Index**: High-performance vector storage
- **Metadata Schema**: Rich metadata structure
- **Namespace Management**: Multi-tenant data isolation

### Session Storage
- **JSON Files**: Simple session persistence
- **Chat History**: Conversation history storage
- **User Preferences**: User setting persistence

### Temporary Storage
- **File Cache**: Uploaded file temporary storage
- **Processing Cache**: Intermediate processing results
- **Memory Management**: Efficient memory usage

---

**Next**: Check out the [Installation Guide](./installation.md) to set up the system or view the [Diagrams](./diagrams/) for visual representations.