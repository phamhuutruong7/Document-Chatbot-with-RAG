# 🚀 Quick Reference Card

## Essential Commands

```bash
# Install and Setup
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys

# Upload Knowledge Base
python scripts/simple_upload_to_pinecone.py

# Run Application
streamlit run main.py
# Access: http://localhost:8501

# Alternative Port
streamlit run main.py --server.port 8502
```

## 🔑 Required API Keys

Add to `.env` file:
```env
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
EMBEDDING_API_KEY=your-embedding-api-key
```

## 💬 Sample Questions

**Hardware:**
- "How do I diagnose PSU voltage issues?"
- "My computer won't turn on, what should I check?"
- "How to test memory with MemTest86?"

**PC Building:**
- "What components do I need for a gaming PC?"
- "How do I check motherboard compatibility?"
- "Best practices for CPU installation"

**Support:**
- "Customer's computer is running slow, troubleshooting steps?"
- "How do I handle warranty claims?"
- "Network connectivity troubleshooting guide"

## 🎮 Chat Commands

```
/help          - Show available commands
/status        - System status and statistics
/clear         - Clear current conversation
/export        - Export conversation history
/upload        - Quick file upload dialog
/search [term] - Search knowledge base directly
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port busy | `streamlit run main.py --server.port 8502` |
| Module not found | `pip install -r requirements.txt` |
| API key error | Check `.env` file format |
| Pinecone error | Verify index name and region |
| Memory issues | Reduce batch_size in config |

## 📁 File Structure

```
├── main.py                    # App entry point
├── PROJECT_GUIDE.md          # Complete guide
├── requirements.txt          # Dependencies
├── .env.example             # Environment template
├── utils/                   # Core modules
├── scripts/                # Upload scripts
├── data/documents/         # Knowledge base
└── logs/                   # Application logs
```

## 🆘 Need Help?

1. **Complete Guide**: [PROJECT_GUIDE.md](PROJECT_GUIDE.md)
2. **Technical Docs**: [docs/](docs/) folder
3. **System Check**: `python scripts/system_check.py`
4. **Debug Mode**: Set `LOG_LEVEL=DEBUG` in `.env`

---
**For full documentation, see [PROJECT_GUIDE.md](PROJECT_GUIDE.md)**
