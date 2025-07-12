# 📚 Document Download Scripts

This folder contains automated scripts for downloading and processing PC documentation for your RAG-based customer support system.

## 📁 Files Overview

### Core Scripts
- **`pdf_downloader.py`** - Main PDF downloading engine with retry logic
- **`download_configs.py`** - Configuration file with all download URLs and settings
- **`document_pipeline.py`** - Full pipeline for download + processing + vector storage
- **`run_downloader.py`** - Simple command-line interface for running downloads

## 🚀 Quick Start

### 1. Install Required Packages
First, install the additional packages needed for web scraping:

```bash
pip install requests beautifulsoup4 lxml
```

### 2. Run the Simple Downloader
For an easy interactive experience:

```bash
python scripts/run_downloader.py
```

This will:
- Check if required packages are installed
- Show available download categories
- Let you choose what to download
- Create the proper folder structure
- Download and organize files

### 3. Run the Full Pipeline (Advanced)
To download AND process into your vector database:

```bash
python scripts/document_pipeline.py --categories pc-manuals troubleshooting
```

## 📋 Available Document Categories

### 🖥️ PC Manuals
- **Dell**: OptiPlex, Inspiron, XPS series
- **HP**: Pavilion, EliteBook series
- **Lenovo**: ThinkPad, ThinkCentre series
- **ASUS**: VivoBook, ROG series
- **Graphics Cards**: NVIDIA RTX, AMD Radeon guides
- **Motherboards**: Installation and setup guides

### 🛠️ Troubleshooting Guides
- **Hardware**: CPU, memory, storage troubleshooting
- **Software**: Windows, drivers, applications
- **Networking**: Wi-Fi, Ethernet, connectivity issues

### 📄 Policies & FAQs
- **General**: Common PC support questions
- **Gaming**: Gaming PC optimization guides
- **Policies**: Template warranty and return policies

## 🔧 Configuration

### Adding New Sources
Edit `download_configs.py` to add new manufacturers or document sources:

```python
{
    'category': 'pc-manuals',
    'manufacturer': 'your_brand',
    'description': 'Your Brand PC Manuals',
    'direct_pdfs': [
        {
            'url': 'https://example.com/manual.pdf',
            'filename': 'your_brand_manual.pdf'
        }
    ]
}
```

### Customizing Download Behavior
In `pdf_downloader.py`, you can modify:
- Download timeout settings
- Retry logic
- File naming conventions
- Directory structure

## 📂 Output Structure

Downloaded files are organized as:

```
data/documents/
├── pc-manuals/
│   ├── dell/
│   ├── hp/
│   ├── lenovo/
│   ├── asus/
│   ├── graphics/
│   └── motherboards/
├── troubleshooting/
│   ├── hardware/
│   ├── software/
│   └── networking/
├── policies/
│   └── general/
└── faqs/
    ├── general/
    └── gaming/
```

## 🔄 Integration with Main App

### Manual Upload
After downloading, you can:
1. Run your main app: `streamlit run main.py`
2. Use the file upload interface to process documents
3. Documents will be chunked and added to your vector database

### Automated Processing
Use the full pipeline to automatically:
1. Download documents
2. Parse and chunk content
3. Generate embeddings
4. Store in Pinecone vector database

```python
from scripts.document_pipeline import AutoDocumentPipeline

pipeline = AutoDocumentPipeline(session_id="knowledge_base")
results = await pipeline.run_full_pipeline(
    categories=['pc-manuals', 'troubleshooting'],
    manufacturers=['dell', 'hp']
)
```

## ⚠️ Important Notes

### Legal Considerations
- Only download publicly available documentation
- Respect robots.txt and website terms of service
- Add delays between requests to be respectful to servers
- Some URLs may require updating as websites change

### Error Handling
- The scripts include retry logic for failed downloads
- Failed downloads are logged in `logs/pdf_downloader.log`
- Check the logs if downloads fail

### Performance
- Downloads are sequential to avoid overwhelming servers
- Large files may take time to download
- Vector processing requires significant memory for large document sets

## 🛠️ Troubleshooting

### Common Issues

1. **Import errors**: Install missing packages with `pip install requests beautifulsoup4`
2. **Download failures**: Check internet connection and URL validity
3. **Permission errors**: Ensure write permissions in the data directory
4. **Memory issues**: Process documents in smaller batches

### Checking Downloads
```bash
# View download summary
cat logs/download_summary.json

# Check folder structure
python -c "from scripts.run_downloader import show_folder_structure; show_folder_structure()"
```

## 🔮 Future Enhancements

- [ ] Support for more file formats (Word docs, web pages)
- [ ] Intelligent duplicate detection
- [ ] Automatic URL validation and updates
- [ ] Parallel downloads with rate limiting
- [ ] Integration with manufacturer APIs
- [ ] Automated document updates and versioning

## 📞 Support

If you encounter issues:
1. Check the logs in `logs/pdf_downloader.log`
2. Verify your internet connection
3. Ensure all required packages are installed
4. Check that target URLs are still valid

---

**Ready to build your PC support knowledge base!** 🚀
