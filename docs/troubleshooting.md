# 🔧 Troubleshooting Guide

## Overview

This guide helps you diagnose and resolve common issues with the Document Chatbot. Issues are organized by category with step-by-step solutions.

## 🚨 Quick Diagnostics

### Health Check Commands

Run these commands to quickly identify issues:

```bash
# Check if all required environment variables are set
echo "OpenAI Key: ${OPENAI_API_KEY:0:10}..."
echo "Pinecone Key: ${PINECONE_API_KEY:0:10}..."
echo "Pinecone Environment: $PINECONE_ENVIRONMENT"
echo "Pinecone Index: $PINECONE_INDEX_NAME"

# Test configuration loading
python -c "from utils.config import load_config; print('Config loaded successfully')"

# Test API connections
python -c "from utils.openai_client import test_connection; test_connection()"
python -c "from utils.pinecone_client import test_connection; test_connection()"
```

### Common Error Patterns

| Error Pattern | Likely Cause | Quick Fix |
|---------------|--------------|----------|
| `API key not found` | Missing environment variable | Set API key in `.env` |
| `Index not found` | Wrong Pinecone index name | Check index name |
| `Connection timeout` | Network/firewall issue | Check internet connection |
| `Rate limit exceeded` | Too many API calls | Wait and retry |
| `File too large` | Upload size limit | Reduce file size |
| `Unsupported format` | Wrong file type | Use supported formats |

## 🔑 API Key Issues

### Problem: OpenAI API Key Not Found

**Error Messages:**
```
Error: OpenAI API key not found
AuthenticationError: Incorrect API key provided
Error: You didn't provide an API key
```

**Solutions:**

1. **Check Environment Variable**
   ```bash
   echo $OPENAI_API_KEY
   # Should show your API key (partially masked)
   ```

2. **Set Environment Variable**
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="sk-your-key-here"
   
   # Windows (Command Prompt)
   set OPENAI_API_KEY=sk-your-key-here
   
   # Linux/macOS
   export OPENAI_API_KEY="sk-your-key-here"
   ```

3. **Create .env File**
   ```bash
   # Create .env file in project root
   echo "OPENAI_API_KEY=sk-your-key-here" > .env
   ```

4. **Verify API Key Format**
   - OpenAI keys start with `sk-`
   - Should be 51 characters long
   - No spaces or special characters

5. **Test API Key**
   ```bash
   curl -H "Authorization: Bearer $OPENAI_API_KEY" \
        https://api.openai.com/v1/models
   ```

### Problem: Pinecone API Key Issues

**Error Messages:**
```
PineconeException: API key is required
Unauthorized: Invalid API key
ForbiddenException: API key does not have access
```

**Solutions:**

1. **Check Pinecone Configuration**
   ```bash
   echo "Pinecone Key: ${PINECONE_API_KEY:0:10}..."
   echo "Environment: $PINECONE_ENVIRONMENT"
   echo "Index: $PINECONE_INDEX_NAME"
   ```

2. **Verify Pinecone Index Exists**
   ```python
   import pinecone
   pinecone.init(api_key="your-key", environment="your-env")
   print(pinecone.list_indexes())
   ```

3. **Check Index Dimensions**
   ```python
   index = pinecone.Index("your-index-name")
   print(index.describe_index_stats())
   ```

## 📁 File Upload Issues

### Problem: File Upload Fails

**Error Messages:**
```
File size exceeds maximum limit
Unsupported file format
Error processing file
File upload timeout
```

**Solutions:**

1. **Check File Size**
   ```bash
   # Check file size (Linux/macOS)
   ls -lh your-file.pdf
   
   # Windows PowerShell
   Get-ChildItem your-file.pdf | Select-Object Name, Length
   ```

2. **Supported File Formats**
   - ✅ PDF (.pdf)
   - ✅ Word Documents (.docx)
   - ✅ Text Files (.txt)
   - ✅ Markdown (.md)
   - ❌ Images (.jpg, .png)
   - ❌ Excel (.xlsx)
   - ❌ PowerPoint (.pptx)

3. **Reduce File Size**
   ```bash
   # For PDF files, try compressing
   # Use online tools or PDF compression software
   
   # For text files, split into smaller files
   split -l 1000 large-file.txt smaller-file-
   ```

4. **Check File Permissions**
   ```bash
   # Ensure file is readable
   ls -la your-file.pdf
   
   # Fix permissions if needed
   chmod 644 your-file.pdf
   ```

### Problem: File Processing Errors

**Error Messages:**
```
Error extracting text from PDF
Document parsing failed
Unable to process document
```

**Solutions:**

1. **PDF-Specific Issues**
   - **Scanned PDFs**: Use OCR tools to convert to text-searchable PDF
   - **Password-protected**: Remove password protection
   - **Corrupted files**: Try opening in PDF reader first

2. **Word Document Issues**
   - **Old formats**: Convert .doc to .docx
   - **Complex formatting**: Save as plain text first
   - **Embedded objects**: Remove images and charts

3. **Text Encoding Issues**
   ```python
   # Check file encoding
   import chardet
   with open('your-file.txt', 'rb') as f:
       result = chardet.detect(f.read())
       print(result['encoding'])
   ```

## 🤖 AI Response Issues

### Problem: Poor Quality Responses

**Symptoms:**
- Irrelevant answers
- Generic responses
- "I don't know" responses
- Incomplete information

**Solutions:**

1. **Improve Question Quality**
   ```
   ❌ Bad: "What does this say?"
   ✅ Good: "What are the main requirements in section 3?"
   
   ❌ Bad: "Tell me about this"
   ✅ Good: "Summarize the key findings from the research"
   ```

2. **Check Document Processing**
   ```bash
   # Verify document was processed successfully
   # Look for success message in logs
   grep "Document processed successfully" logs/app.log
   ```

3. **Adjust RAG Parameters**
   ```bash
   # Increase number of retrieved documents
   RAG_TOP_K=10  # Default is 5
   
   # Lower similarity threshold
   RAG_SIMILARITY_THRESHOLD=0.5  # Default is 0.7
   ```

4. **Try Different Question Approaches**
   ```
   # If direct question fails, try:
   "Find information about [topic]"
   "What does the document say about [specific term]?"
   "List all mentions of [keyword]"
   ```

### Problem: Slow Response Times

**Symptoms:**
- Long wait times for responses
- Timeout errors
- Application freezing

**Solutions:**

1. **Check Model Configuration**
   ```bash
   # Use faster model for development
   OPENAI_MODEL=gpt-3.5-turbo  # Faster than gpt-4
   
   # Reduce max tokens
   OPENAI_MAX_TOKENS=500  # Default is 1000
   ```

2. **Optimize Chunking**
   ```bash
   # Smaller chunks = faster processing
   CHUNK_SIZE=500  # Default is 1000
   
   # Fewer retrieved documents
   RAG_TOP_K=3  # Default is 5
   ```

3. **Check Network Connection**
   ```bash
   # Test API connectivity
   curl -w "@curl-format.txt" -s -o /dev/null https://api.openai.com/v1/models
   ```

## 🗄️ Database and Storage Issues

### Problem: Pinecone Connection Errors

**Error Messages:**
```
PineconeException: Failed to connect
Timeout connecting to Pinecone
Index not found
```

**Solutions:**

1. **Verify Pinecone Configuration**
   ```python
   import pinecone
   
   # Test connection
   try:
       pinecone.init(
           api_key="your-api-key",
           environment="your-environment"
       )
       print("Connected successfully")
       print("Available indexes:", pinecone.list_indexes())
   except Exception as e:
       print(f"Connection failed: {e}")
   ```

2. **Check Index Status**
   ```python
   # Check if index exists and is ready
   if "your-index-name" in pinecone.list_indexes():
       index = pinecone.Index("your-index-name")
       stats = index.describe_index_stats()
       print(f"Index stats: {stats}")
   else:
       print("Index not found")
   ```

3. **Create Missing Index**
   ```python
   # Create index if it doesn't exist
   pinecone.create_index(
       name="document-chatbot",
       dimension=1536,  # For OpenAI embeddings
       metric="cosine"
   )
   ```

### Problem: Session Storage Issues

**Error Messages:**
```
Failed to save session
Session file not found
Permission denied writing session
```

**Solutions:**

1. **Check Directory Permissions**
   ```bash
   # Check if sessions directory exists and is writable
   ls -la sessions/
   
   # Create directory if missing
   mkdir -p sessions
   chmod 755 sessions
   ```

2. **Clear Corrupted Sessions**
   ```bash
   # Remove all session files
   rm -rf sessions/*
   
   # Or move to backup
   mv sessions sessions_backup
   mkdir sessions
   ```

3. **Check Disk Space**
   ```bash
   # Check available disk space
   df -h .
   
   # Clean up if needed
   rm -rf temp/*
   rm -rf logs/*.log.old
   ```

## 🌐 Network and Connectivity Issues

### Problem: API Connection Timeouts

**Error Messages:**
```
Connection timeout
Read timeout
SSL connection error
Network unreachable
```

**Solutions:**

1. **Check Internet Connection**
   ```bash
   # Test basic connectivity
   ping google.com
   
   # Test HTTPS connectivity
   curl -I https://api.openai.com
   ```

2. **Configure Proxy Settings**
   ```bash
   # If behind corporate firewall
   export HTTP_PROXY=http://proxy.company.com:8080
   export HTTPS_PROXY=https://proxy.company.com:8080
   ```

3. **Adjust Timeout Settings**
   ```python
   # In your configuration
   OPENAI_TIMEOUT=60  # Increase timeout
   PINECONE_TIMEOUT=30
   ```

### Problem: Rate Limiting

**Error Messages:**
```
Rate limit exceeded
Too many requests
Quota exceeded
```

**Solutions:**

1. **Implement Retry Logic**
   ```python
   import time
   import random
   
   def retry_with_backoff(func, max_retries=3):
       for attempt in range(max_retries):
           try:
               return func()
           except RateLimitError:
               if attempt == max_retries - 1:
                   raise
               wait_time = (2 ** attempt) + random.uniform(0, 1)
               time.sleep(wait_time)
   ```

2. **Reduce Request Frequency**
   ```bash
   # Increase batch size to reduce API calls
   EMBEDDING_BATCH_SIZE=50  # Process more at once
   
   # Add delays between requests
   REQUEST_DELAY=1  # 1 second between requests
   ```

3. **Check API Usage**
   ```bash
   # Monitor your OpenAI usage
   curl -H "Authorization: Bearer $OPENAI_API_KEY" \
        https://api.openai.com/v1/usage
   ```

## 💻 Application Startup Issues

### Problem: Streamlit Won't Start

**Error Messages:**
```
ModuleNotFoundError
ImportError
Streamlit command not found
```

**Solutions:**

1. **Check Python Environment**
   ```bash
   # Verify Python version
   python --version  # Should be 3.8+
   
   # Check if Streamlit is installed
   pip list | grep streamlit
   
   # Install if missing
   pip install streamlit
   ```

2. **Install Dependencies**
   ```bash
   # Install all requirements
   pip install -r requirements.txt
   
   # Or install individually
   pip install streamlit openai pinecone-client langchain
   ```

3. **Check Virtual Environment**
   ```bash
   # Activate virtual environment
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   
   # Verify you're in the right environment
   which python
   which streamlit
   ```

### Problem: Import Errors

**Error Messages:**
```
ModuleNotFoundError: No module named 'utils'
ImportError: cannot import name 'load_config'
```

**Solutions:**

1. **Check Working Directory**
   ```bash
   # Run from project root
   cd /path/to/document-chatbot
   streamlit run main.py
   ```

2. **Fix Python Path**
   ```bash
   # Add current directory to Python path
   export PYTHONPATH="${PYTHONPATH}:."
   
   # Or run with Python module flag
   python -m streamlit run main.py
   ```

3. **Check File Structure**
   ```
   project-root/
   ├── main.py
   ├── utils/
   │   ├── __init__.py
   │   ├── config.py
   │   └── ...
   └── requirements.txt
   ```

## 🔍 Debugging Techniques

### Enable Debug Mode

```bash
# Set debug environment variables
export DEBUG=true
export LOG_LEVEL=DEBUG

# Run with verbose logging
streamlit run main.py --logger.level=debug
```

### Check Log Files

```bash
# View recent logs
tail -f logs/app.log

# Search for specific errors
grep -i "error" logs/app.log
grep -i "exception" logs/app.log

# Check Streamlit logs
ls ~/.streamlit/logs/
```

### Test Individual Components

```python
# Test configuration loading
from utils.config import load_config
config = load_config()
print(config)

# Test OpenAI connection
from utils.openai_client import OpenAIClient
client = OpenAIClient()
response = client.test_connection()
print(response)

# Test Pinecone connection
from utils.pinecone_client import PineconeClient
client = PineconeClient()
stats = client.get_index_stats()
print(stats)
```

## 📊 Performance Monitoring

### Monitor Resource Usage

```bash
# Check memory usage
ps aux | grep streamlit

# Monitor CPU usage
top -p $(pgrep -f streamlit)

# Check disk usage
du -sh sessions/ uploads/ logs/
```

### Profile Application Performance

```python
# Add timing decorators
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper
```

## 🆘 Getting Help

### Before Asking for Help

1. **Check this troubleshooting guide**
2. **Review error messages carefully**
3. **Check log files for details**
4. **Try the quick diagnostics**
5. **Search existing GitHub issues**

### Information to Include

When reporting issues, include:

```
**Environment:**
- OS: [Windows/Linux/macOS]
- Python version: [3.x.x]
- Streamlit version: [x.x.x]

**Configuration:**
- OpenAI model: [gpt-4/gpt-3.5-turbo]
- Pinecone environment: [your-env]
- File type: [PDF/DOCX/TXT]

**Error Details:**
- Full error message
- Steps to reproduce
- Expected behavior
- Actual behavior

**Logs:**
[Paste relevant log entries]
```

### Support Channels

- **GitHub Issues**: For bugs and feature requests
- **Documentation**: Check other docs files
- **Community Forums**: Stack Overflow with tags
- **Email Support**: [if available]

## 🔧 Advanced Troubleshooting

### Memory Issues

```bash
# Monitor memory usage
watch -n 1 'ps aux | grep streamlit'

# Clear Python cache
find . -type d -name "__pycache__" -exec rm -rf {} +

# Restart with memory limits
ulimit -v 2000000  # Limit virtual memory
streamlit run main.py
```

### Database Corruption

```python
# Reset Pinecone index
import pinecone
pinecone.init(api_key="your-key", environment="your-env")

# Delete and recreate index
pinecone.delete_index("your-index")
pinecone.create_index(
    name="your-index",
    dimension=1536,
    metric="cosine"
)
```

### Configuration Conflicts

```bash
# Check for conflicting environment variables
env | grep -E '(OPENAI|PINECONE)' | sort

# Clear all environment variables
unset OPENAI_API_KEY PINECONE_API_KEY

# Reload from .env file
source .env
```

---

**Still having issues?** Check the [Configuration Guide](./configuration.md) for detailed setup instructions or the [Development Guide](./development.md) for advanced debugging techniques.