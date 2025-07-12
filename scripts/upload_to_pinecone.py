#!/usr/bin/env python3
"""
Comprehensive document processing and Pinecone upload script.
Processes all documents in the knowledge base and uploads them to vector database.
"""

import os
import sys
import time
import logging
from pathlib import Path
from typing import List, Dict, Any
import uuid

# Add the parent directory to the Python path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.pinecone_client import PineconeClient
from utils.embeddings import EmbeddingClient
from utils.chunker import ChunkingStrategy
from utils.config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/document_upload.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DocumentProcessor:
    """Process and upload documents to Pinecone vector database."""
    
    def __init__(self):
        """Initialize the document processor."""
        self.config = Config()
        self.pinecone_client = PineconeClient()
        self.embedding_client = EmbeddingClient()
        self.chunking_strategy = ChunkingStrategy()
        
        # Document processing statistics
        self.stats = {
            'total_files': 0,
            'processed_files': 0,
            'failed_files': 0,
            'total_chunks': 0,
            'uploaded_chunks': 0,
            'failed_chunks': 0
        }
        
        # Create logs directory
        os.makedirs('logs', exist_ok=True)
    
    def parse_local_file(self, file_path: str) -> str:
        """
        Parse a local file and extract text content.
        
        Args:
            file_path: Path to the file
            
        Returns:
            str: Extracted text content
        """
        try:
            file_extension = file_path.lower().split('.')[-1]
            
            if file_extension == 'txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            elif file_extension == 'md':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            elif file_extension == 'pdf':
                return self._parse_pdf_file(file_path)
            else:
                logger.warning(f"Unsupported file type: {file_extension} for {file_path}")
                return ""
                
        except Exception as e:
            logger.error(f"Error parsing file {file_path}: {str(e)}")
            raise
    
    def _parse_pdf_file(self, file_path: str) -> str:
        """Parse PDF file using PyMuPDF."""
        try:
            import fitz  # PyMuPDF
            
            pdf_document = fitz.open(file_path)
            text_content = ""
            
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text_content += page.get_text()
                text_content += "\n\n"
            
            pdf_document.close()
            return text_content.strip()
            
        except ImportError:
            logger.error("PyMuPDF not installed. Install with: pip install PyMuPDF")
            return ""
        except Exception as e:
            logger.error(f"Error parsing PDF {file_path}: {str(e)}")
            return ""
    
    def get_document_metadata(self, file_path: str) -> Dict[str, Any]:
        """
        Extract metadata from file path and content.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dict containing metadata
        """
        path_obj = Path(file_path)
        
        # Extract category from directory structure
        parts = path_obj.parts
        if 'documents' in parts:
            doc_index = parts.index('documents')
            if doc_index + 1 < len(parts):
                category = parts[doc_index + 1]
            else:
                category = 'general'
        else:
            category = 'general'
        
        # Extract subcategory if exists
        subcategory = 'general'
        if len(parts) > 2:
            subcategory = parts[-2] if parts[-2] != category else 'general'
        
        # Determine document type based on filename patterns
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
        
        # Extract manufacturer if present in filename
        manufacturer = 'general'
        for brand in ['hp', 'dell', 'lenovo', 'asus', 'amd', 'nvidia', 'intel']:
            if brand in filename:
                manufacturer = brand
                break
        
        return {
            'filename': path_obj.name,
            'category': category,
            'subcategory': subcategory,
            'doc_type': doc_type,
            'manufacturer': manufacturer,
            'file_path': str(file_path),
            'file_size': path_obj.stat().st_size if path_obj.exists() else 0
        }
    
    def process_document(self, file_path: str, session_id: str = "bulk_upload") -> bool:
        """
        Process a single document and upload to Pinecone.
        
        Args:
            file_path: Path to the document
            session_id: Session ID for namespacing
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            logger.info(f"Processing document: {file_path}")
            
            # Parse document content
            content = self.parse_local_file(file_path)
            if not content:
                logger.warning(f"No content extracted from {file_path}")
                return False
            
            # Get document metadata
            metadata = self.get_document_metadata(file_path)
            
            # Chunk the document
            chunks = self.chunking_strategy.chunk_text(
                content, 
                chunk_size=self.config.chunk_size,
                chunk_overlap=self.config.chunk_overlap
            )
            
            if not chunks:
                logger.warning(f"No chunks created from {file_path}")
                return False
            
            logger.info(f"Created {len(chunks)} chunks from {file_path}")
            self.stats['total_chunks'] += len(chunks)
            
            # Process chunks in batches
            batch_size = 100
            for i in range(0, len(chunks), batch_size):
                batch_chunks = chunks[i:i + batch_size]
                success = self._upload_chunk_batch(batch_chunks, metadata, session_id)
                if success:
                    self.stats['uploaded_chunks'] += len(batch_chunks)
                else:
                    self.stats['failed_chunks'] += len(batch_chunks)
                
                # Small delay to avoid rate limits
                time.sleep(0.1)
            
            return True
            
        except Exception as e:
            logger.error(f"Error processing document {file_path}: {str(e)}")
            return False
    
    def _upload_chunk_batch(self, chunks: List[str], base_metadata: Dict[str, Any], session_id: str) -> bool:
        """
        Upload a batch of chunks to Pinecone.
        
        Args:
            chunks: List of text chunks
            base_metadata: Base metadata for all chunks
            session_id: Session ID for namespacing
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Prepare vectors for batch upload
            vectors = []
            
            for chunk_idx, chunk_text in enumerate(chunks):
                # Generate embedding
                embedding = self.embedding_client.get_embedding(chunk_text)
                
                # Create unique ID for this chunk
                chunk_id = f"{base_metadata['filename']}_{uuid.uuid4().hex[:8]}_{chunk_idx}"
                
                # Prepare metadata for this chunk
                chunk_metadata = base_metadata.copy()
                chunk_metadata.update({
                    'chunk_id': chunk_id,
                    'chunk_index': chunk_idx,
                    'chunk_text': chunk_text[:500],  # Store first 500 chars in metadata
                    'text_length': len(chunk_text),
                    'session_id': session_id,
                    'upload_timestamp': time.time()
                })
                
                vectors.append({
                    'id': chunk_id,
                    'values': embedding,
                    'metadata': chunk_metadata
                })
            
            # Upload to Pinecone
            success = self.pinecone_client.upsert_vectors(vectors, namespace=session_id)
            
            if success:
                logger.debug(f"Successfully uploaded batch of {len(vectors)} vectors")
                return True
            else:
                logger.error(f"Failed to upload batch of {len(vectors)} vectors")
                return False
                
        except Exception as e:
            logger.error(f"Error uploading chunk batch: {str(e)}")
            return False
    
    def process_directory(self, directory_path: str, session_id: str = "knowledge_base") -> Dict[str, Any]:
        """
        Process all documents in a directory and subdirectories.
        
        Args:
            directory_path: Path to the directory
            session_id: Session ID for namespacing
            
        Returns:
            Dict containing processing statistics
        """
        logger.info(f"Starting bulk document processing from: {directory_path}")
        
        # Find all supported files
        supported_extensions = ['.txt', '.pdf', '.md']
        all_files = []
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if any(file.lower().endswith(ext) for ext in supported_extensions):
                    all_files.append(os.path.join(root, file))
        
        self.stats['total_files'] = len(all_files)
        logger.info(f"Found {len(all_files)} documents to process")
        
        # Process each file
        for idx, file_path in enumerate(all_files, 1):
            logger.info(f"Processing file {idx}/{len(all_files)}: {os.path.basename(file_path)}")
            
            try:
                success = self.process_document(file_path, session_id)
                if success:
                    self.stats['processed_files'] += 1
                else:
                    self.stats['failed_files'] += 1
                    
            except Exception as e:
                logger.error(f"Failed to process {file_path}: {str(e)}")
                self.stats['failed_files'] += 1
            
            # Progress update
            if idx % 5 == 0 or idx == len(all_files):
                progress = (idx / len(all_files)) * 100
                logger.info(f"Progress: {progress:.1f}% ({idx}/{len(all_files)} files)")
        
        return self.stats
    
    def print_final_report(self):
        """Print a final processing report."""
        print(f"\n📊 DOCUMENT PROCESSING COMPLETE")
        print(f"=" * 50)
        print(f"📁 Total Files Found: {self.stats['total_files']}")
        print(f"✅ Successfully Processed: {self.stats['processed_files']}")
        print(f"❌ Failed to Process: {self.stats['failed_files']}")
        print(f"📄 Total Chunks Created: {self.stats['total_chunks']}")
        print(f"☁️ Chunks Uploaded to Pinecone: {self.stats['uploaded_chunks']}")
        print(f"💥 Failed Chunk Uploads: {self.stats['failed_chunks']}")
        
        success_rate = (self.stats['processed_files'] / self.stats['total_files'] * 100) if self.stats['total_files'] > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        
        if self.stats['uploaded_chunks'] > 0:
            print(f"\n🎉 Your knowledge base is now available in Pinecone!")
            print(f"🚀 Ready to start your chatbot: streamlit run main.py")
        else:
            print(f"\n⚠️ No chunks were uploaded. Check the logs for errors.")

def main():
    """Main function to run the document processing."""
    
    print("🚀 STARTING COMPREHENSIVE DOCUMENT UPLOAD TO PINECONE")
    print("=" * 60)
    
    # Initialize processor
    try:
        processor = DocumentProcessor()
    except Exception as e:
        logger.error(f"Failed to initialize document processor: {str(e)}")
        print("❌ Failed to initialize. Check your .env file and API keys.")
        return
    
    # Set document directory
    doc_directory = os.path.join("data", "documents")
    
    if not os.path.exists(doc_directory):
        logger.error(f"Document directory not found: {doc_directory}")
        print(f"❌ Document directory not found: {doc_directory}")
        return
    
    # Process all documents
    session_id = f"knowledge_base_{int(time.time())}"
    print(f"📁 Processing documents from: {doc_directory}")
    print(f"🏷️ Using session ID: {session_id}")
    
    try:
        stats = processor.process_directory(doc_directory, session_id)
        processor.print_final_report()
        
        # Save session info for later reference
        session_info = {
            'session_id': session_id,
            'upload_time': time.time(),
            'stats': stats
        }
        
        import json
        with open('logs/last_upload_session.json', 'w') as f:
            json.dump(session_info, f, indent=2)
        
        print(f"\n📝 Session info saved to: logs/last_upload_session.json")
        
    except Exception as e:
        logger.error(f"Error during bulk processing: {str(e)}")
        print(f"❌ Error during processing: {str(e)}")

if __name__ == "__main__":
    main()
