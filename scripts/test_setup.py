"""
Test script to verify the downloader setup
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
os.chdir(project_root)

def test_imports():
    """Test if all imports work correctly."""
    print("🧪 Testing imports...")
    
    try:
        import requests
        print("✅ requests imported successfully")
    except ImportError as e:
        print(f"❌ requests import failed: {e}")
        return False
    
    try:
        from bs4 import BeautifulSoup
        print("✅ beautifulsoup4 imported successfully")
    except ImportError as e:
        print(f"❌ beautifulsoup4 import failed: {e}")
        return False
    
    try:
        from scripts.pdf_downloader import PDFDownloader
        print("✅ PDFDownloader imported successfully")
    except ImportError as e:
        print(f"❌ PDFDownloader import failed: {e}")
        return False
    
    try:
        from scripts.download_configs import DOWNLOAD_CONFIGS
        print("✅ DOWNLOAD_CONFIGS imported successfully")
        print(f"   Found {len(DOWNLOAD_CONFIGS)} download configurations")
    except ImportError as e:
        print(f"❌ DOWNLOAD_CONFIGS import failed: {e}")
        return False
    
    return True

def test_directories():
    """Test if directories exist."""
    print("\n📁 Testing directories...")
    
    required_dirs = [
        "logs",
        "data/documents",
        "data/vectorstore"
    ]
    
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✅ {dir_path} exists")
        else:
            print(f"❌ {dir_path} missing")
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            print(f"✅ Created {dir_path}")

def test_downloader():
    """Test the downloader initialization."""
    print("\n🤖 Testing downloader initialization...")
    
    try:
        from scripts.pdf_downloader import PDFDownloader
        downloader = PDFDownloader()
        print("✅ PDFDownloader initialized successfully")
        print(f"   Base directory: {downloader.base_dir}")
        return True
    except Exception as e:
        print(f"❌ PDFDownloader initialization failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 PDF Downloader Test Suite")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        return
    
    # Test directories
    test_directories()
    
    # Test downloader
    if not test_downloader():
        print("\n❌ Downloader test failed!")
        return
    
    print("\n✅ All tests passed!")
    print("🎉 The downloader is ready to use!")
    print("\n🔧 To run the downloader:")
    print("   python scripts/setup_and_run.py")
    print("   or")
    print("   python scripts/run_downloader.py")

if __name__ == "__main__":
    main()
