"""
Simple execution script for downloading PC documentation
Run this script to download and organize PC manuals and guides
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

def main():
    """Main execution function."""
    
    print("🤖 PC Documentation Downloader")
    print("=" * 50)
    
    # Create logs directory first
    os.makedirs('logs', exist_ok=True)
    
    # Check if required packages are installed
    missing_packages = check_requirements()
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n🔧 Install missing packages with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return
    
    # Import after checking requirements
    try:
        from scripts.pdf_downloader import PDFDownloader
        from scripts.download_configs import DOWNLOAD_CONFIGS
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're running this script from the project root directory:")
        print("   cd d:\\Projects\\Document-Chatbot-with-RAG")
        print("   python scripts/run_downloader.py")
        return
    
    print("✅ All requirements satisfied")
    print("\n📋 Available download categories:")
    
    # Show available categories
    categories = {}
    for i, config in enumerate(DOWNLOAD_CONFIGS, 1):
        category = config['category']
        manufacturer = config.get('manufacturer', 'general')
        description = config.get('description', 'No description')
        
        print(f"   {i:2d}. {category}/{manufacturer}")
        print(f"       {description}")
        categories[i] = config
    
    print(f"\n🎯 Select download options:")
    print("   a) Download all categories")
    print("   b) Select specific categories")
    print("   c) Download only PC manuals")
    print("   d) Download only troubleshooting guides")
    print("   q) Quit")
    
    choice = input("\nEnter your choice (a/b/c/d/q): ").lower().strip()
    
    if choice == 'q':
        print("👋 Goodbye!")
        return
    
    selected_configs = []
    
    if choice == 'a':
        selected_configs = DOWNLOAD_CONFIGS
        print("📥 Downloading all categories...")
    
    elif choice == 'b':
        print("\nEnter category numbers (comma-separated, e.g., 1,3,5):")
        try:
            numbers = [int(x.strip()) for x in input().split(',')]
            selected_configs = [categories[n] for n in numbers if n in categories]
            if not selected_configs:
                print("❌ No valid categories selected")
                return
        except ValueError:
            print("❌ Invalid input format")
            return
    
    elif choice == 'c':
        selected_configs = [c for c in DOWNLOAD_CONFIGS if c['category'] == 'pc-manuals']
        print("📥 Downloading PC manuals only...")
    
    elif choice == 'd':
        selected_configs = [c for c in DOWNLOAD_CONFIGS if c['category'] == 'troubleshooting']
        print("📥 Downloading troubleshooting guides only...")
    
    else:
        print("❌ Invalid choice")
        return
    
    if not selected_configs:
        print("❌ No configurations selected")
        return
    
    # Create necessary directories
    create_directories()
    
    # Initialize downloader
    downloader = PDFDownloader()
    
    print(f"\n🚀 Starting downloads for {len(selected_configs)} configurations...")
    
    total_downloaded = 0
    total_failed = 0
    
    # Process each configuration
    for i, config in enumerate(selected_configs, 1):
        category = config['category']
        manufacturer = config.get('manufacturer', 'general')
        
        print(f"\n📁 [{i}/{len(selected_configs)}] Processing: {category}/{manufacturer}")
        
        try:
            results = downloader.download_from_config(config)
            
            downloaded = len(results['downloaded'])
            failed = len(results['failed'])
            
            total_downloaded += downloaded
            total_failed += failed
            
            print(f"   ✅ Downloaded: {downloaded}")
            print(f"   ❌ Failed: {failed}")
            
            # Show downloaded files
            if results['downloaded']:
                print("   📄 Files:")
                for file_path in results['downloaded'][:3]:  # Show first 3
                    print(f"      - {Path(file_path).name}")
                if len(results['downloaded']) > 3:
                    print(f"      ... and {len(results['downloaded']) - 3} more")
        
        except Exception as e:
            print(f"   ❌ Error: {e}")
            total_failed += 1
    
    # Final summary
    print(f"\n📊 Download Complete!")
    print(f"   Total Downloaded: {total_downloaded}")
    print(f"   Total Failed: {total_failed}")
    
    if total_downloaded > 0:
        print(f"\n📁 Files saved to: data/documents/")
        print(f"🔄 Next steps:")
        print(f"   1. Review downloaded files in data/documents/")
        print(f"   2. Run your main application: streamlit run main.py")
        print(f"   3. Upload documents through the web interface")
        print(f"   4. Start chatting with your PC knowledge base!")
    
    # Show folder structure
    show_folder_structure()

def check_requirements():
    """Check if required packages are installed."""
    required_packages = ['requests', 'beautifulsoup4', 'pathlib']
    missing = []
    
    for package in required_packages:
        try:
            if package == 'beautifulsoup4':
                import bs4
            else:
                __import__(package)
        except ImportError:
            missing.append(package)
    
    return missing

def create_directories():
    """Create necessary directory structure."""
    directories = [
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
        "data/vectorstore",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("📁 Directory structure created")

def show_folder_structure():
    """Show the current folder structure."""
    print(f"\n📂 Current folder structure:")
    
    base_path = Path("data/documents")
    if base_path.exists():
        for root, dirs, files in os.walk(base_path):
            level = root.replace(str(base_path), '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            
            # Show first few files in each directory
            subindent = ' ' * 2 * (level + 1)
            for file in files[:3]:
                print(f"{subindent}{file}")
            if len(files) > 3:
                print(f"{subindent}... and {len(files) - 3} more files")

if __name__ == "__main__":
    main()
