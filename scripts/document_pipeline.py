"""
Document Processing Pipeline
Integrates PDF downloading with the existing RAG system
"""

import os
import sys
import asyncio
from pathlib import Path
from typing import List, Dict, Optional
import logging

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from scripts.pdf_downloader import PDFDownloader
from scripts.download_configs import DOWNLOAD_CONFIGS
from utils.file_parser import parse_file
from utils.chunker import chunk_text
from utils.pinecone_client import PineconeClient
from utils.embeddings import get_embeddings, get_batch_embeddings
from utils.session_manager import SessionManager
import streamlit as st

class AutoDocumentPipeline:
    """Automated document download and processing pipeline."""
    
    def __init__(self, session_id: str = "auto_knowledge_base"):
        self.session_id = session_id
        self.downloader = PDFDownloader()
        self.base_dir = Path("data/documents")
        self.processed_files = []
        self.failed_files = []
        
        # Initialize Pinecone client
        try:
            self.pinecone_client = PineconeClient()
        except Exception as e:
            logging.error(f"Failed to initialize Pinecone client: {e}")
            self.pinecone_client = None
    
    async def run_full_pipeline(self, categories: List[str] = None, manufacturers: List[str] = None):
        """Run the complete download and processing pipeline."""
        
        print("🚀 Starting Full Document Pipeline...")
        
        # Step 1: Download documents
        download_results = await self.download_documents(categories, manufacturers)
        
        # Step 2: Process downloaded documents
        if download_results['downloaded']:
            processing_results = await self.process_documents(download_results['downloaded'])
            
            # Step 3: Add to vector database
            if self.pinecone_client and processing_results:
                vector_results = await self.add_to_vector_database(processing_results)
                
                print(f"\n✅ Pipeline Complete!")
                print(f"   📥 Downloaded: {len(download_results['downloaded'])} files")
                print(f"   🔄 Processed: {len(processing_results)} files")
                print(f"   📊 Added to Vector DB: {vector_results.get('success_count', 0)} files")
                
                return {
                    'downloaded': download_results,
                    'processed': processing_results,
                    'vectorized': vector_results
                }
        
        return {'error': 'No documents were successfully downloaded'}
    
    async def download_documents(self, categories: List[str] = None, manufacturers: List[str] = None):
        """Download documents based on configuration."""
        
        print("📥 Starting document downloads...")
        
        # Filter configurations
        filtered_configs = []
        for config in DOWNLOAD_CONFIGS:
            include_config = True
            
            if categories and config['category'] not in categories:
                include_config = False
            
            if manufacturers and config.get('manufacturer') not in manufacturers:
                include_config = False
            
            if include_config:
                filtered_configs.append(config)
        
        print(f"   Processing {len(filtered_configs)} configurations...")
        
        total_results = {
            'downloaded': [],
            'failed': [],
            'skipped': []
        }
        
        for config in filtered_configs:
            print(f"   📁 {config['category']}/{config.get('manufacturer', 'general')}")
            
            results = self.downloader.download_from_config(config)
            
            # Merge results
            for key in total_results:
                total_results[key].extend(results[key])
        
        return total_results
    
    async def process_documents(self, file_paths: List[str]):
        """Process downloaded documents into chunks."""
        
        print(f"🔄 Processing {len(file_paths)} documents...")
        
        processed_results = []
        
        for file_path in file_paths:
            try:
                print(f"   📄 Processing: {Path(file_path).name}")
                
                # Parse the file
                parsed_content = parse_file(file_path)
                
                if not parsed_content:
                    print(f"   ⚠️  No content extracted from: {Path(file_path).name}")
                    self.failed_files.append(file_path)
                    continue
                
                # Chunk the content
                chunks = chunk_text(
                    text=parsed_content,
                    chunk_size=1000,
                    chunk_overlap=200
                )
                
                # Create metadata
                file_info = self._extract_file_metadata(file_path)
                
                # Add metadata to chunks
                chunk_documents = []
                for i, chunk in enumerate(chunks):
                    chunk_metadata = {
                        **file_info,
                        'chunk_index': i,
                        'chunk_count': len(chunks),
                        'text': chunk,
                        'session_id': self.session_id
                    }
                    chunk_documents.append(chunk_metadata)
                
                processed_results.append({
                    'file_path': file_path,
                    'chunks': chunk_documents,
                    'metadata': file_info
                })
                
                self.processed_files.append(file_path)
                print(f"   ✅ Processed: {len(chunks)} chunks")
                
            except Exception as e:
                print(f"   ❌ Error processing {Path(file_path).name}: {e}")
                self.failed_files.append(file_path)
        
        return processed_results
    
    async def add_to_vector_database(self, processed_documents: List[Dict]):
        """Add processed documents to vector database."""
        
        if not self.pinecone_client:
            print("❌ Pinecone client not available")
            return {'error': 'Pinecone client not initialized'}
        
        print(f"📊 Adding {len(processed_documents)} documents to vector database...")
        
        success_count = 0
        failed_count = 0
        
        for doc_info in processed_documents:
            try:
                chunks = doc_info['chunks']
                
                # Generate embeddings for all chunks
                chunk_texts = [chunk['text'] for chunk in chunks]
                embeddings = get_batch_embeddings(chunk_texts)
                
                # Prepare vectors for Pinecone
                vectors = []
                for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                    vector_id = f"{self.session_id}_{Path(doc_info['file_path']).stem}_{i}"
                    vectors.append({
                        'id': vector_id,
                        'values': embedding,
                        'metadata': chunk
                    })
                
                # Upsert to Pinecone
                self.pinecone_client.upsert_vectors(
                    vectors=vectors,
                    namespace=self.session_id
                )
                
                success_count += 1
                print(f"   ✅ Added: {Path(doc_info['file_path']).name} ({len(vectors)} vectors)")
                
            except Exception as e:
                failed_count += 1
                print(f"   ❌ Failed to add: {Path(doc_info['file_path']).name} - {e}")
        
        return {
            'success_count': success_count,
            'failed_count': failed_count,
            'total_vectors': sum(len(doc['chunks']) for doc in processed_documents)
        }
    
    def _extract_file_metadata(self, file_path: str) -> Dict:
        """Extract metadata from file path and name."""
        
        path = Path(file_path)
        
        # Extract category and manufacturer from path
        parts = path.parts
        category = 'general'
        manufacturer = 'general'
        
        if 'documents' in parts:
            doc_index = parts.index('documents')
            if len(parts) > doc_index + 1:
                category = parts[doc_index + 1]
            if len(parts) > doc_index + 2:
                manufacturer = parts[doc_index + 2]
        
        return {
            'document_name': path.name,
            'file_path': str(path),
            'category': category,
            'manufacturer': manufacturer,
            'file_size': path.stat().st_size if path.exists() else 0,
            'file_extension': path.suffix,
            'source_type': 'auto_downloaded'
        }
    
    def get_pipeline_summary(self) -> Dict:
        """Get summary of pipeline execution."""
        return {
            'session_id': self.session_id,
            'processed_files': len(self.processed_files),
            'failed_files': len(self.failed_files),
            'processed_file_list': self.processed_files,
            'failed_file_list': self.failed_files
        }


# Streamlit integration functions
def setup_auto_pipeline_ui():
    """Streamlit UI for the auto pipeline."""
    
    st.sidebar.header("🤖 Auto Knowledge Base")
    
    # Category selection
    available_categories = list(set(config['category'] for config in DOWNLOAD_CONFIGS))
    selected_categories = st.sidebar.multiselect(
        "Select document categories:",
        available_categories,
        default=['pc-manuals', 'troubleshooting'],
        help="Choose which types of documents to download and process"
    )
    
    # Manufacturer selection
    available_manufacturers = list(set(
        config.get('manufacturer', 'general') 
        for config in DOWNLOAD_CONFIGS 
        if config['category'] in (selected_categories or available_categories)
    ))
    selected_manufacturers = st.sidebar.multiselect(
        "Select manufacturers:",
        available_manufacturers,
        default=['dell', 'hp', 'general'],
        help="Choose which manufacturers' documentation to include"
    )
    
    # Pipeline controls
    if st.sidebar.button("🚀 Run Auto Pipeline"):
        if selected_categories:
            run_pipeline_async(selected_categories, selected_manufacturers)
        else:
            st.sidebar.error("Please select at least one category")
    
    # Manual download only
    if st.sidebar.button("📥 Download Only"):
        if selected_categories:
            run_download_only(selected_categories, selected_manufacturers)
        else:
            st.sidebar.error("Please select at least one category")

def run_pipeline_async(categories: List[str], manufacturers: List[str]):
    """Run the pipeline asynchronously with Streamlit updates."""
    
    with st.spinner("Running auto knowledge base pipeline..."):
        pipeline = AutoDocumentPipeline()
        
        # Create progress placeholder
        progress_placeholder = st.empty()
        
        try:
            # Run pipeline
            results = asyncio.run(pipeline.run_full_pipeline(categories, manufacturers))
            
            if 'error' not in results:
                st.success("✅ Auto pipeline completed successfully!")
                
                # Show results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "Downloaded", 
                        len(results['downloaded']['downloaded']),
                        help="Number of files downloaded"
                    )
                
                with col2:
                    st.metric(
                        "Processed", 
                        len(results['processed']),
                        help="Number of files processed into chunks"
                    )
                
                with col3:
                    st.metric(
                        "Vectorized", 
                        results['vectorized'].get('success_count', 0),
                        help="Number of files added to vector database"
                    )
                
                # Show summary
                summary = pipeline.get_pipeline_summary()
                st.json(summary)
            else:
                st.error(f"❌ Pipeline failed: {results['error']}")
                
        except Exception as e:
            st.error(f"❌ Pipeline error: {e}")

def run_download_only(categories: List[str], manufacturers: List[str]):
    """Run download only without processing."""
    
    with st.spinner("Downloading documents..."):
        try:
            pipeline = AutoDocumentPipeline()
            results = asyncio.run(pipeline.download_documents(categories, manufacturers))
            
            st.success("✅ Download completed!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Downloaded", len(results['downloaded']))
            
            with col2:
                st.metric("Failed", len(results['failed']))
            
            # Show file list
            if results['downloaded']:
                st.subheader("📁 Downloaded Files")
                for file_path in results['downloaded']:
                    st.text(f"✅ {Path(file_path).name}")
            
            if results['failed']:
                st.subheader("❌ Failed Downloads")
                for failed_url in results['failed']:
                    st.text(f"❌ {failed_url}")
                    
        except Exception as e:
            st.error(f"❌ Download error: {e}")


# Main execution
if __name__ == "__main__":
    # Command line execution
    import argparse
    
    parser = argparse.ArgumentParser(description="Document Pipeline")
    parser.add_argument("--categories", nargs="+", help="Categories to process")
    parser.add_argument("--manufacturers", nargs="+", help="Manufacturers to include")
    parser.add_argument("--download-only", action="store_true", help="Download only, don't process")
    
    args = parser.parse_args()
    
    pipeline = AutoDocumentPipeline()
    
    if args.download_only:
        results = asyncio.run(pipeline.download_documents(args.categories, args.manufacturers))
        print(f"Download results: {results}")
    else:
        results = asyncio.run(pipeline.run_full_pipeline(args.categories, args.manufacturers))
        print(f"Pipeline results: {results}")
