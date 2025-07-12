#!/usr/bin/env python3
"""
Simple script to upload text documents from your knowledge base to Pinecone.
Focuses on the generated .txt files in your document collection.
"""

import os
import sys
import time
import logging
from pathlib import Path
from typing import List, Dict, Any
import uuid
import json

# Add the parent directory to the Python path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.pinecone_client import PineconeClient
from utils.embeddings import get_embeddings

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def chunk_text_simple(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """Simple text chunking function."""
    if not text:
        return []
    
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk_words = words[i:i + chunk_size]
        chunk_text = ' '.join(chunk_words)
        if chunk_text.strip():
            chunks.append(chunk_text)
    
    return chunks

def extract_metadata_from_path(file_path: str) -> Dict[str, Any]:
    """Extract metadata from file path."""
    path_obj = Path(file_path)
    parts = path_obj.parts
    
    # Extract category from directory structure
    category = 'general'
    if 'documents' in parts:
        doc_index = parts.index('documents')
        if doc_index + 1 < len(parts):
            category = parts[doc_index + 1]
    
    # Determine document type from filename
    filename = path_obj.stem.lower()
    doc_type = 'general'
    
    if 'manual' in filename or 'guide' in filename:
        doc_type = 'manual'
    elif 'troubleshoot' in filename:
        doc_type = 'troubleshooting'
    elif 'scenario' in filename or 'training' in filename:
        doc_type = 'training'
    elif 'compatibility' in filename or 'technical' in filename:
        doc_type = 'technical'
    elif 'faq' in filename:
        doc_type = 'faq'
    elif 'policy' in filename:
        doc_type = 'policy'
    
    # Extract manufacturer
    manufacturer = 'general'
    for brand in ['hp', 'dell', 'lenovo', 'asus', 'amd', 'nvidia', 'intel']:
        if brand in filename:
            manufacturer = brand
            break
    
    return {
        'filename': path_obj.name,
        'category': category,
        'doc_type': doc_type,
        'manufacturer': manufacturer,
        'file_path': str(file_path)
    }

def main():
    """Main function to upload documents to Pinecone."""
    
    print("🚀 UPLOADING KNOWLEDGE BASE TO PINECONE")
    print("=" * 50)
    
    # Initialize clients
    try:
        print("🔧 Initializing Pinecone client...")
        pinecone_client = PineconeClient()
        print("✅ Pinecone client initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing Pinecone client: {str(e)}")
        print("💡 Make sure your .env file has valid API keys")
        return
    
    # Find all text files
    doc_directory = "data/documents"
    text_files = []
    
    print(f"📁 Scanning for documents in: {doc_directory}")
    
    for root, dirs, files in os.walk(doc_directory):
        for file in files:
            if file.endswith('.txt'):
                text_files.append(os.path.join(root, file))
    
    print(f"📄 Found {len(text_files)} text documents")
    
    if not text_files:
        print("❌ No text files found to process")
        return
    
    # Session ID for this upload
    session_id = f"knowledge_base_{int(time.time())}"
    print(f"🏷️ Using session ID: {session_id}")
    
    # Process each file
    total_chunks = 0
    uploaded_chunks = 0
    processed_files = 0
    
    for idx, file_path in enumerate(text_files, 1):
        try:
            print(f"\n📝 Processing ({idx}/{len(text_files)}): {os.path.basename(file_path)}")
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                print(f"   ⚠️ Skipping empty file")
                continue
            
            # Extract metadata
            metadata = extract_metadata_from_path(file_path)
            
            # Chunk the content
            chunks = chunk_text_simple(content, chunk_size=800, overlap=100)
            total_chunks += len(chunks)
            
            print(f"   📄 Created {len(chunks)} chunks")
            
            # Process chunks in batches
            batch_size = 50
            file_uploaded = 0
            
            for i in range(0, len(chunks), batch_size):
                batch_chunks = chunks[i:i + batch_size]
                vectors = []
                
                for chunk_idx, chunk_text in enumerate(batch_chunks):
                    try:
                        # Generate embedding
                        embedding = get_embeddings(chunk_text)
                        
                        # Create unique ID
                        chunk_id = f"{metadata['filename']}_{uuid.uuid4().hex[:8]}_{i + chunk_idx}"
                        
                        # Prepare metadata
                        chunk_metadata = metadata.copy()
                        chunk_metadata.update({
                            'chunk_id': chunk_id,
                            'chunk_index': i + chunk_idx,
                            'chunk_text': chunk_text[:300],  # First 300 chars for preview
                            'text_length': len(chunk_text),
                            'session_id': session_id,
                            'upload_timestamp': time.time()
                        })
                        
                        vectors.append({
                            'id': chunk_id,
                            'values': embedding,
                            'metadata': chunk_metadata
                        })
                        
                    except Exception as e:
                        print(f"   ❌ Error processing chunk {chunk_idx}: {str(e)}")
                        continue
                
                # Upload batch to Pinecone
                if vectors:
                    try:
                        pinecone_client.upsert_batch(vectors, namespace=session_id)
                        file_uploaded += len(vectors)
                        uploaded_chunks += len(vectors)
                        print(f"   ✅ Uploaded batch of {len(vectors)} chunks")
                    except Exception as e:
                        print(f"   ❌ Error uploading batch: {str(e)}")
                
                # Small delay to avoid rate limits
                time.sleep(0.2)
            
            if file_uploaded > 0:
                processed_files += 1
                print(f"   🎉 Successfully uploaded {file_uploaded} chunks from file")
            
        except Exception as e:
            print(f"   ❌ Error processing file: {str(e)}")
            continue
    
    # Final summary
    print(f"\n📊 UPLOAD COMPLETE!")
    print(f"=" * 30)
    print(f"📁 Files Processed: {processed_files}/{len(text_files)}")
    print(f"📄 Total Chunks Created: {total_chunks}")
    print(f"☁️ Chunks Uploaded: {uploaded_chunks}")
    print(f"🏷️ Session ID: {session_id}")
    
    # Save session info
    session_info = {
        'session_id': session_id,
        'upload_time': time.time(),
        'files_processed': processed_files,
        'chunks_uploaded': uploaded_chunks,
        'total_files': len(text_files)
    }
    
    os.makedirs('logs', exist_ok=True)
    with open('logs/pinecone_upload_session.json', 'w') as f:
        json.dump(session_info, f, indent=2)
    
    if uploaded_chunks > 0:
        print(f"\n🎉 SUCCESS! Your knowledge base is now in Pinecone!")
        print(f"🚀 Start your chatbot with: streamlit run main.py")
        print(f"💾 Session info saved to: logs/pinecone_upload_session.json")
    else:
        print(f"\n⚠️ No chunks were uploaded. Check for errors above.")

if __name__ == "__main__":
    main()
