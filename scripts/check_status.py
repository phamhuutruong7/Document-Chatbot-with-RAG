"""
Check the status of downloaded and created documents
"""

import os
from pathlib import Path

def check_document_status():
    """Check what documents are available."""
    
    print("📊 Document Collection Status")
    print("=" * 50)
    
    base_dir = Path("data/documents")
    
    if not base_dir.exists():
        print("❌ Documents directory doesn't exist")
        return
    
    # Count files by category
    categories = {}
    total_files = 0
    total_size = 0
    
    for root, dirs, files in os.walk(base_dir):
        if files:
            rel_path = Path(root).relative_to(base_dir)
            category = str(rel_path).split(os.sep)[0] if rel_path != Path('.') else 'root'
            
            if category not in categories:
                categories[category] = {'count': 0, 'files': [], 'size': 0}
            
            for file in files:
                if not file.startswith('.'):  # Skip hidden files
                    file_path = Path(root) / file
                    file_size = file_path.stat().st_size if file_path.exists() else 0
                    
                    categories[category]['count'] += 1
                    categories[category]['files'].append(file)
                    categories[category]['size'] += file_size
                    
                    total_files += 1
                    total_size += file_size
    
    # Display summary
    print(f"📁 Total Documents: {total_files}")
    print(f"💾 Total Size: {total_size / 1024:.1f} KB")
    print()
    
    # Display by category
    for category, info in categories.items():
        if info['count'] > 0:
            print(f"📂 {category.upper()}: {info['count']} files ({info['size'] / 1024:.1f} KB)")
            for file in info['files'][:3]:  # Show first 3 files
                print(f"   📄 {file}")
            if len(info['files']) > 3:
                print(f"   ... and {len(info['files']) - 3} more")
            print()
    
    # Show what we have for PC customer support
    print("🛠️  Customer Support Coverage:")
    support_areas = {
        'PC Setup': ['pc-manuals'],
        'Hardware Issues': ['troubleshooting', 'hardware'],
        'Software Problems': ['troubleshooting', 'software'],
        'Common Questions': ['faqs'],
        'Store Policies': ['policies']
    }
    
    for area, keywords in support_areas.items():
        found = False
        for category in categories:
            if any(keyword in category.lower() for keyword in keywords):
                if categories[category]['count'] > 0:
                    found = True
                    break
        
        status = "✅" if found else "❌"
        print(f"   {status} {area}")
    
    print(f"\n🎯 Ready for Customer Support: {'✅ YES' if total_files >= 5 else '❌ Need more documents'}")

def suggest_next_steps():
    """Suggest what to do next."""
    
    print(f"\n🚀 Next Steps:")
    print(f"   1. Run your RAG application:")
    print(f"      streamlit run main.py")
    print(f"   ")
    print(f"   2. Upload documents via the web interface")
    print(f"   ")
    print(f"   3. Test with customer support questions:")
    print(f"      • 'How do I set up my new Dell computer?'")
    print(f"      • 'My PC is overheating, what should I do?'")
    print(f"      • 'Windows is running slowly, how can I fix it?'")
    print(f"      • 'What is your return policy?'")
    print(f"      • 'Do you offer warranty on PC repairs?'")
    print(f"   ")
    print(f"   4. Add more documents:")
    print(f"      • Download manufacturer manuals manually")
    print(f"      • Create product-specific guides")
    print(f"      • Add your store's actual policies")

if __name__ == "__main__":
    check_document_status()
    suggest_next_steps()
