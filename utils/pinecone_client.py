from pinecone import Pinecone, ServerlessSpec
import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
import time
import uuid

# Load environment variables
load_dotenv()

class PineconeClient:
    """
    Client for interacting with Pinecone vector database with session-based namespaces
    """
    
    def __init__(self):
        """
        Initialize Pinecone client
        """
        self.api_key = os.getenv("PINECONE_API_KEY")
        self.index_name = os.getenv("PINECONE_INDEX_NAME", "document-chat")
        
        if not self.api_key:
            raise ValueError("PINECONE_API_KEY not found in environment variables")
        
        # Initialize Pinecone
        self.pc = Pinecone(api_key=self.api_key)
        
        # Connect to or create index
        self.index = self._get_or_create_index()
    
    def _get_or_create_index(self):
        """
        Get existing index or create new one
        
        Returns:
            pinecone.Index: Pinecone index object
        """
        try:
            # Check if index exists
            existing_indexes = [index.name for index in self.pc.list_indexes()]
            
            if self.index_name in existing_indexes:
                print(f"Connecting to existing index: {self.index_name}")
                return self.pc.Index(self.index_name)
            else:
                print(f"Creating new index: {self.index_name}")
                # Create new index with appropriate dimension
                self.pc.create_index(
                    name=self.index_name,
                    dimension=1536,  # text-embedding-3-small dimension
                    metric="cosine",
                    spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1"
                    )
                )
                
                # Wait for index to be ready
                time.sleep(10)
                return self.pc.Index(self.index_name)
                
        except Exception as e:
            raise Exception(f"Error connecting to Pinecone index: {str(e)}")
    
    def upsert_vector(self, vector_id: str, embedding: List[float], metadata: Dict[str, Any], namespace: Optional[str] = None):
        """
        Insert or update a vector in the index
        
        Args:
            vector_id (str): Unique identifier for the vector
            embedding (List[float]): Vector embedding
            metadata (Dict[str, Any]): Associated metadata
            namespace (Optional[str]): Optional namespace for the vector
        """
        try:
            upsert_params = {
                "vectors": [
                    {
                        "id": vector_id,
                        "values": embedding,
                        "metadata": metadata
                    }
                ]
            }
            if namespace:
                upsert_params["namespace"] = namespace
            
            self.index.upsert(**upsert_params)
        except Exception as e:
            raise Exception(f"Error upserting vector: {str(e)}")
    
    def upsert_batch(self, vectors: List[Dict[str, Any]], namespace: Optional[str] = None):
        """
        Insert or update multiple vectors in batch
        
        Args:
            vectors (List[Dict]): List of vector dictionaries with id, values, and metadata
            namespace (Optional[str]): Optional namespace for the vectors
        """
        try:
            # Pinecone recommends batches of 100 vectors
            batch_size = 100
            
            for i in range(0, len(vectors), batch_size):
                batch = vectors[i:i + batch_size]
                upsert_params = {"vectors": batch}
                if namespace:
                    upsert_params["namespace"] = namespace
                self.index.upsert(**upsert_params)
                
        except Exception as e:
            raise Exception(f"Error upserting batch vectors: {str(e)}")    
    
    def create_session_vectors(self, texts: List[str], embeddings: List[List[float]], session_id: str, document_name: str = None):
        """
        Create vectors with session-specific metadata and namespace
        
        Args:
            texts (List[str]): List of text chunks
            embeddings (List[List[float]]): List of embeddings for each text
            session_id (str): Session identifier for namespace
            document_name (str): Optional document name
            
        Returns:
            bool: Success status
        """
        try:
            vectors = []
            for i, (text, embedding) in enumerate(zip(texts, embeddings)):
                vector_id = f"{session_id}_{uuid.uuid4()}"
                metadata = {
                    "text": text,
                    "session_id": session_id,
                    "chunk_index": i,
                    "document_name": document_name or "unknown",
                    "created_at": str(uuid.uuid1().time)
                }
                vectors.append({
                    "id": vector_id,
                    "values": embedding,
                    "metadata": metadata
                })
            
            self.upsert_batch(vectors, namespace=session_id)
            return True
        except Exception as e:
            raise Exception(f"Error creating session vectors: {str(e)}")
    
    def query_vectors(self, query_embedding: List[float], top_k: int = 5, 
                     filter_dict: Dict[str, Any] = None, namespace: Optional[str] = None) -> Dict[str, Any]:
        """
        Query the index for similar vectors
        
        Args:
            query_embedding (List[float]): Query vector
            top_k (int): Number of top results to return
            filter_dict (Dict[str, Any]): Optional metadata filter
            namespace (Optional[str]): Optional namespace to query
            
        Returns:
            Dict[str, Any]: Query results
        """
        try:
            query_params = {
                "vector": query_embedding,
                "top_k": top_k,
                "include_metadata": True,
                "include_values": False
            }
            
            if filter_dict:
                query_params["filter"] = filter_dict
            if namespace:
                query_params["namespace"] = namespace
            
            results = self.index.query(**query_params)
            return results
            
        except Exception as e:
            raise Exception(f"Error querying vectors: {str(e)}")    
    
    def query_session_vectors(self, query_embedding: List[float], session_id: str, top_k: int = 5, 
                             filter_dict: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Query vectors within a specific session namespace
        
        Args:
            query_embedding (List[float]): Query vector
            session_id (str): Session identifier
            top_k (int): Number of top results to return
            filter_dict (Dict[str, Any]): Optional metadata filter
            
        Returns:
            Dict[str, Any]: Query results
        """
        return self.query_vectors(query_embedding, top_k, filter_dict, namespace=session_id)
    
    def delete_vector(self, vector_id: str, namespace: Optional[str] = None):
        """
        Delete a vector from the index
        
        Args:
            vector_id (str): ID of vector to delete
            namespace (Optional[str]): Optional namespace
        """
        try:
            delete_params = {"ids": [vector_id]}
            if namespace:
                delete_params["namespace"] = namespace
            self.index.delete(**delete_params)
        except Exception as e:
            raise Exception(f"Error deleting vector: {str(e)}")
    
    def delete_by_filter(self, filter_dict: Dict[str, Any], namespace: Optional[str] = None):
        """
        Delete vectors matching filter criteria
        
        Args:
            filter_dict (Dict[str, Any]): Metadata filter for deletion
            namespace (Optional[str]): Optional namespace
        """
        try:
            delete_params = {"filter": filter_dict}
            if namespace:
                delete_params["namespace"] = namespace
            self.index.delete(**delete_params)
        except Exception as e:
            raise Exception(f"Error deleting vectors by filter: {str(e)}")
    
    def delete_namespace(self, namespace: str):
        """
        Delete all vectors in a specific namespace
        
        Args:
            namespace (str): Namespace to delete
        """
        try:
            self.index.delete(delete_all=True, namespace=namespace)
        except Exception as e:
            raise Exception(f"Error deleting namespace: {str(e)}")
    
    def clear_session_data(self, session_id: str):
        """
        Clear all vectors for a specific session
        
        Args:
            session_id (str): Session identifier
        """
        return self.delete_namespace(session_id)
    
    def get_index_stats(self, namespace: Optional[str] = None) -> Dict[str, Any]:
        """
        Get statistics about the index
        
        Args:
            namespace (Optional[str]): Optional namespace to get stats for
            
        Returns:
            Dict[str, Any]: Index statistics
        """
        try:
            if namespace:
                stats = self.index.describe_index_stats(filter={"namespace": namespace})
            else:
                stats = self.index.describe_index_stats()
            return stats
        except Exception as e:
            raise Exception(f"Error getting index stats: {str(e)}")    
    
    def get_session_stats(self, session_id: str) -> Dict[str, Any]:
        """
        Get statistics for a specific session namespace
        
        Args:
            session_id (str): Session identifier
            
        Returns:
            Dict[str, Any]: Session statistics
        """
        return self.get_index_stats(namespace=session_id)
    
    def list_vectors(self, prefix: str = None, limit: int = 100) -> List[str]:
        """
        List vector IDs in the index
        
        Args:
            prefix (str): Optional prefix filter
            limit (int): Maximum number of IDs to return
            
        Returns:
            List[str]: List of vector IDs
        """
        try:
            # Note: This is a simplified implementation
            # Pinecone doesn't have a direct list_vectors method
            # You might need to implement this based on your specific needs
            stats = self.get_index_stats()
            return []
        except Exception as e:
            raise Exception(f"Error listing vectors: {str(e)}")
    
    def clear_index(self):
        """
        Clear all vectors from the index
        """
        try:
            self.index.delete(delete_all=True)
        except Exception as e:
            raise Exception(f"Error clearing index: {str(e)}")
    
    def search_by_metadata(self, filter_dict: Dict[str, Any], top_k: int = 10, namespace: Optional[str] = None) -> Dict[str, Any]:
        """
        Search vectors by metadata only (without vector similarity)
        
        Args:
            filter_dict (Dict[str, Any]): Metadata filter
            top_k (int): Number of results to return
            namespace (Optional[str]): Optional namespace to search
            
        Returns:
            Dict[str, Any]: Search results
        """
        try:
            # Create a dummy query vector (all zeros)
            dummy_vector = [0.0] * 1536
            
            query_params = {
                "vector": dummy_vector,
                "top_k": top_k,
                "filter": filter_dict,
                "include_metadata": True,
                "include_values": False
            }
            
            if namespace:
                query_params["namespace"] = namespace
            
            results = self.index.query(**query_params)
            
            return results
            
        except Exception as e:
            raise Exception(f"Error searching by metadata: {str(e)}")
    
    def get_documents_by_filename(self, filename: str) -> List[Dict[str, Any]]:
        """
        Get all document chunks for a specific filename
        
        Args:
            filename (str): Name of the file
            
        Returns:
            List[Dict[str, Any]]: List of document chunks
        """
        try:
            filter_dict = {"filename": filename}
            results = self.search_by_metadata(filter_dict, top_k=1000)
            
            documents = []
            for match in results.get('matches', []):
                documents.append({
                    'id': match['id'],
                    'metadata': match['metadata'],
                    'score': match.get('score', 0)
                })
            
            # Sort by chunk_index if available
            documents.sort(key=lambda x: x['metadata'].get('chunk_index', 0))
            
            return documents
            
        except Exception as e:
            raise Exception(f"Error getting documents by filename: {str(e)}")