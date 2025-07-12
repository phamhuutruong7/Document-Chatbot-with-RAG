"""
Simple startup script for the PDF downloader
This script handles setup and runs the downloader with better error handling
"""

import os
import sys
from pathlib import Path

def setup_environment():
    """Set up the environment for running the downloader."""
    
    # Get project root directory
    current_dir = Path(__file__).parent.parent
    project_root = current_dir.resolve()
    
    print(f"🔧 Project root: {project_root}")
    
    # Add project root to Python path
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    # Change to project root directory
    os.chdir(project_root)
    
    # Create necessary directories
    directories = [
        "logs",
        "data/documents/pc-manuals/dell",
        "data/documents/pc-manuals/hp", 
        "data/documents/pc-manuals/lenovo",
        "data/documents/pc-manuals/asus",
        "data/documents/pc-manuals/graphics",
        "data/documents/pc-manuals/motherboards",
        "data/documents/troubleshooting/hardware",
        "data/documents/troubleshooting/software",
        "data/documents/troubleshooting/networking",
        "data/documents/policies/general",
        "data/documents/faqs/general",
        "data/documents/faqs/gaming",
        "data/vectorstore"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Environment setup complete")

def check_packages():
    """Check if required packages are installed."""
    required = ['requests', 'beautifulsoup4']
    missing = []
    
    for package in required:
        try:
            if package == 'beautifulsoup4':
                import bs4
            else:
                __import__(package)
        except ImportError:
            missing.append(package)
    
    return missing

def main():
    """Main function."""
    print("🚀 PDF Downloader Setup")
    print("=" * 40)
    
    # Setup environment
    try:
        setup_environment()
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return
    
    # Check packages
    missing = check_packages()
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print(f"🔧 Install with: pip install {' '.join(missing)}")
        return
    
    print("✅ All packages available")
    
    # Import and run the main downloader
    try:
        from scripts.run_downloader import main as run_main
        print("\n🤖 Starting downloader...")
        print("=" * 40)
        run_main()
    except Exception as e:
        print(f"❌ Downloader failed: {e}")
        print(f"🐛 Error details: {type(e).__name__}")
        
        # Provide troubleshooting info
        print(f"\n🔍 Troubleshooting:")
        print(f"   - Current directory: {os.getcwd()}")
        print(f"   - Python path: {sys.path[:3]}...")
        print(f"   - Error location: {e}")

if __name__ == "__main__":
    main()
