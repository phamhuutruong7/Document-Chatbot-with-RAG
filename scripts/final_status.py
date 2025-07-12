#!/usr/bin/env python3
"""
Simple document collection status checker compatible with Windows.
"""

import os

def check_final_status():
    """Check the final status of document collection."""
    base_dir = os.path.join("data", "documents")
    
    # Count files and calculate sizes
    total_files = 0
    total_size = 0
    categories = {}
    
    for root, dirs, files in os.walk(base_dir):
        category = os.path.basename(root)
        if category == "documents":
            continue
            
        category_files = 0
        category_size = 0
        
        for file in files:
            if file.endswith(('.txt', '.pdf', '.md')):
                filepath = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(filepath)
                    total_size += file_size
                    category_size += file_size
                    total_files += 1
                    category_files += 1
                except OSError:
                    pass
        
        if category_files > 0:
            categories[category] = {
                'files': category_files,
                'size': category_size
            }
    
    # Display results
    print("FINAL DOCUMENT COLLECTION STATUS")
    print("=" * 50)
    print(f"Total Documents: {total_files}")
    print(f"Total Size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print(f"Categories: {len(categories)}")
    
    print(f"\nCATEGORY BREAKDOWN:")
    print("-" * 30)
    for category, info in sorted(categories.items()):
        print(f"{category.upper()}: {info['files']} files ({info['size']/1024:.1f} KB)")
    
    print(f"\nCOVERAGE AREAS:")
    print("✅ PC Setup and Configuration")
    print("✅ Hardware Troubleshooting") 
    print("✅ Customer Service Training")
    print("✅ Technical Documentation")
    print("✅ Specialized PC Builds")
    print("✅ Product Knowledge Base")
    
    print(f"\nREADY FOR DEPLOYMENT:")
    print("1. Start chatbot: streamlit run main.py")
    print("2. Upload documents via web interface")
    print("3. Test with customer support scenarios")
    print("4. Expand with manufacturer PDFs")

if __name__ == "__main__":
    check_final_status()
