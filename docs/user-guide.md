# 👤 User Guide

## Getting Started

Welcome to the Document Chatbot! This guide will help you understand how to use all the features of the application effectively.

## 🚀 First Steps

### 1. Starting the Application

1. **Launch the application**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The application should load with a clean interface

3. **Initial Setup**
   - The app will automatically create a new session
   - You'll see the main chat interface
   - The sidebar contains upload and session management options

### 2. Understanding the Interface

#### Main Chat Area
- **Chat History**: Displays your conversation with the AI
- **Input Box**: Type your questions here
- **Send Button**: Submit your questions

#### Sidebar
- **File Upload**: Upload documents for analysis
- **Session Management**: View and manage chat sessions
- **Settings**: Configure application preferences
- **Help**: Access help and command information

## 📁 Document Upload and Processing

### Supported File Formats

The application supports multiple document formats:
- **PDF files** (.pdf) - Most common format
- **Word documents** (.docx) - Microsoft Word files
- **Text files** (.txt) - Plain text documents
- **Markdown files** (.md) - Markdown formatted text

### Uploading Documents

1. **Click the file upload area** in the sidebar
2. **Select your document** from your computer
3. **Wait for processing** - you'll see a progress indicator
4. **Confirmation** - success message when processing is complete

### File Size Limits
- **Maximum file size**: 100MB (configurable)
- **Processing time**: Varies based on document size
- **Multiple files**: Upload one at a time

### What Happens During Processing

1. **Text Extraction**: Content is extracted from your document
2. **Chunking**: Text is split into manageable segments
3. **Embedding**: Each chunk is converted to vector embeddings
4. **Storage**: Embeddings are stored in the vector database
5. **Indexing**: Document becomes searchable

## 💬 Asking Questions

### Basic Queries

Once you've uploaded a document, you can ask questions about its content:

**Examples:**
- "What is the main topic of this document?"
- "Summarize the key points"
- "What does the document say about [specific topic]?"
- "Find information about [keyword]"

### Advanced Query Techniques

#### Specific Information Requests
- "List all the requirements mentioned"
- "What are the steps in the process?"
- "Find all dates and deadlines"
- "Extract contact information"

#### Analytical Questions
- "What are the pros and cons discussed?"
- "Compare the different approaches mentioned"
- "What are the risks identified?"
- "Analyze the financial implications"

#### Contextual Queries
- "Based on section 3, what should I do next?"
- "How does this relate to the previous chapter?"
- "What's the connection between X and Y?"

### Query Best Practices

1. **Be Specific**: More specific questions yield better answers
2. **Use Keywords**: Include relevant terms from your document
3. **Ask Follow-ups**: Build on previous answers for deeper insights
4. **Context Matters**: Reference specific sections when needed

## ⚡ Special Commands

The application supports special commands for advanced functionality:

### Available Commands

#### `/help`
- **Purpose**: Display available commands and usage
- **Usage**: Type `/help` in the chat
- **Output**: List of all available commands

#### `/clear`
- **Purpose**: Clear current session history
- **Usage**: Type `/clear` in the chat
- **Effect**: Removes all chat history and uploaded documents

#### `/sessions`
- **Purpose**: List all available sessions
- **Usage**: Type `/sessions` in the chat
- **Output**: Session IDs and creation dates

#### `/metrics`
- **Purpose**: Show performance metrics
- **Usage**: Type `/metrics` in the chat
- **Output**: RAG pipeline performance statistics

#### `/config`
- **Purpose**: Display current configuration
- **Usage**: Type `/config` in the chat
- **Output**: Current application settings

### Command Examples

```
User: /help
Bot: Available commands:
- /help: Show this help message
- /clear: Clear session history
- /sessions: List all sessions
- /metrics: Show performance metrics
- /config: Display configuration

User: /clear
Bot: Session cleared successfully. All chat history and documents have been removed.

User: /metrics
Bot: RAG Performance Metrics:
- Total queries: 15
- Average response time: 2.3s
- Average relevance score: 0.85
```

## 👤 Session Management

### Understanding Sessions

- **Session**: A conversation context with uploaded documents
- **Persistence**: Sessions are saved automatically
- **Isolation**: Each session has its own document collection
- **History**: Chat history is maintained per session

### Session Operations

#### Creating New Sessions
1. **Automatic**: New session created when app starts
2. **Manual**: Use session management in sidebar
3. **Command**: Use `/clear` to reset current session

#### Loading Existing Sessions
1. **Sidebar**: Select from session dropdown
2. **Command**: Use `/sessions` to list available sessions
3. **Automatic**: Last session loads on app restart

#### Session Data
Each session contains:
- **Chat History**: All questions and answers
- **Document Collection**: Uploaded documents and embeddings
- **Metadata**: Session creation time, document count
- **Settings**: Session-specific configurations

## 📊 Understanding Responses

### Response Components

#### AI Answer
- **Main Response**: Direct answer to your question
- **Source Attribution**: References to document sections
- **Confidence Indicators**: Relevance scores when available

#### Response Quality Indicators
- **High Relevance**: Answer directly from document content
- **Medium Relevance**: Inferred from related content
- **Low Relevance**: General knowledge or uncertain

### Interpreting Results

#### Good Responses
- Specific and detailed answers
- Clear source references
- Consistent with document content
- Addresses the exact question asked

#### When to Ask Follow-ups
- Response seems incomplete
- Need more specific information
- Want to explore related topics
- Clarification needed

## 🎯 Use Case Examples

### Legal Document Analysis

**Scenario**: Analyzing a contract

```
1. Upload: contract.pdf
2. Ask: "What are the key terms and conditions?"
3. Follow-up: "What are the termination clauses?"
4. Specific: "Find all dates and deadlines mentioned"
5. Analysis: "What are the penalties for breach?"
```

### Research Paper Review

**Scenario**: Understanding a research paper

```
1. Upload: research_paper.pdf
2. Ask: "What is the main hypothesis?"
3. Follow-up: "What methodology was used?"
4. Results: "What were the key findings?"
5. Implications: "What are the practical applications?"
```

### Technical Documentation

**Scenario**: API documentation review

```
1. Upload: api_docs.pdf
2. Ask: "How do I authenticate with this API?"
3. Follow-up: "What are the available endpoints?"
4. Specific: "Show me the rate limiting rules"
5. Examples: "Provide example API calls"
```

### Study Material

**Scenario**: Textbook chapter analysis

```
1. Upload: textbook_chapter.pdf
2. Ask: "Summarize the main concepts"
3. Follow-up: "What are the key formulas?"
4. Practice: "Give me practice questions"
5. Review: "What should I focus on for the exam?"
```

## 🔧 Customization Options

### Response Preferences

#### Detail Level
- **Concise**: Brief, to-the-point answers
- **Detailed**: Comprehensive explanations
- **Bullet Points**: Structured, easy-to-scan format

#### Response Style
- **Professional**: Formal, business-appropriate
- **Casual**: Conversational, friendly tone
- **Technical**: Precise, technical language

### Query Optimization

#### For Better Results
1. **Include Context**: "In the financial section, what..."
2. **Specify Format**: "List the top 5..."
3. **Set Scope**: "Based on chapter 3..."
4. **Request Examples**: "Give me examples of..."

## 📈 Performance Tips

### Optimizing Upload Speed
- **File Size**: Smaller files process faster
- **Format**: PDF and TXT files are fastest
- **Content**: Text-heavy documents work best
- **Quality**: Clear, well-formatted documents yield better results

### Improving Query Results
- **Specific Keywords**: Use terms from the document
- **Clear Questions**: Avoid ambiguous phrasing
- **Context**: Reference specific sections
- **Follow-up**: Build on previous answers

### Managing Sessions
- **Regular Cleanup**: Clear old sessions periodically
- **Focused Sessions**: Keep related documents together
- **Descriptive Names**: Use meaningful session identifiers

## 🚨 Limitations and Considerations

### Current Limitations

#### File Processing
- **Image Text**: Limited OCR capabilities
- **Complex Layouts**: Tables and charts may not parse perfectly
- **Scanned Documents**: Quality affects text extraction
- **Large Files**: Processing time increases with size

#### Response Accuracy
- **Context Dependency**: Answers based on document content only
- **Ambiguity**: May struggle with unclear questions
- **Technical Content**: Complex technical material may need clarification
- **Language**: Optimized for English content

### Best Practices

#### Document Preparation
- **Clean Text**: Ensure documents are text-searchable
- **Good Quality**: High-resolution scans if using PDFs
- **Organized Content**: Well-structured documents work better
- **Relevant Content**: Focus on documents related to your questions

#### Query Strategy
- **Start Broad**: Begin with general questions
- **Narrow Down**: Use follow-ups for specifics
- **Verify Information**: Cross-reference important details
- **Multiple Angles**: Ask the same question differently if needed

## 🆘 Getting Help

### In-App Help
- **Command Help**: Type `/help` for command list
- **Error Messages**: Read error messages carefully
- **Status Indicators**: Watch for processing status

### Troubleshooting
- **Upload Issues**: Check file format and size
- **Slow Responses**: Wait for processing to complete
- **Poor Results**: Try rephrasing your question
- **Session Problems**: Use `/clear` to reset

### Support Resources
- **Documentation**: Check other documentation files
- **FAQ**: Common questions and solutions
- **GitHub Issues**: Report bugs and request features

---

**Next Steps**: 
- [Configuration Guide](./configuration.md) for advanced settings
- [Troubleshooting](./troubleshooting.md) for common issues
- [API Reference](./api-reference.md) for technical details