import openai
import os
from typing import List
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI client for embeddings
embedding_client = openai.OpenAI(
    api_key=os.getenv("EMBEDDING_API_KEY"),
    base_url=os.getenv("EMBEDDING_BASE_URL", "https://api.openai.com/v1")
)

# Get default embedding model from environment
DEFAULT_EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")

def get_embeddings(text: str, model: str = None) -> List[float]:
    """
    Generate embeddings for given text using OpenAI API
    
    Args:
        text (str): Input text to embed
        model (str): OpenAI embedding model to use
        
    Returns:
        List[float]: Vector embedding
    """
    try:
        # Clean the text
        text = text.replace("\n", " ").strip()
        
        if not text:
            raise ValueError("Empty text provided for embedding")
        
        # Use default model if none specified
        if model is None:
            model = DEFAULT_EMBEDDING_MODEL
            
        # Create embedding using OpenAI API
        response = embedding_client.embeddings.create(
            input=text,
            model=model
        )
        
        # Extract embedding vector
        embedding = response.data[0].embedding
        
        return embedding
        
    except Exception as e:
        raise Exception(f"Error generating embedding: {str(e)}")

def get_batch_embeddings(texts: List[str], model: str = None) -> List[List[float]]:
    """
    Generate embeddings for multiple texts in batch
    
    Args:
        texts (List[str]): List of input texts to embed
        model (str): OpenAI embedding model to use
        
    Returns:
        List[List[float]]: List of vector embeddings
    """
    try:
        # Clean the texts
        cleaned_texts = []
        for text in texts:
            cleaned_text = text.replace("\n", " ").strip()
            if cleaned_text:
                cleaned_texts.append(cleaned_text)
        
        if not cleaned_texts:
            raise ValueError("No valid texts provided for embedding")
        
        # Use default model if none specified
        if model is None:
            model = DEFAULT_EMBEDDING_MODEL
            
        # Create embeddings using OpenAI API
        response = embedding_client.embeddings.create(
            input=cleaned_texts,
            model=model
        )
        
        # Extract embedding vectors
        embeddings = [item.embedding for item in response.data]
        
        return embeddings
        
    except Exception as e:
        raise Exception(f"Error generating batch embeddings: {str(e)}")

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Calculate cosine similarity between two vectors
    
    Args:
        vec1 (List[float]): First vector
        vec2 (List[float]): Second vector
        
    Returns:
        float: Cosine similarity score
    """
    try:
        # Convert to numpy arrays
        a = np.array(vec1)
        b = np.array(vec2)
        
        # Calculate cosine similarity
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
        
        similarity = dot_product / (norm_a * norm_b)
        return float(similarity)
        
    except Exception as e:
        raise Exception(f"Error calculating cosine similarity: {str(e)}")

def find_most_similar(query_embedding: List[float], 
                     candidate_embeddings: List[List[float]], 
                     top_k: int = 5) -> List[tuple]:
    """
    Find most similar embeddings to query
    
    Args:
        query_embedding (List[float]): Query vector
        candidate_embeddings (List[List[float]]): List of candidate vectors
        top_k (int): Number of top results to return
        
    Returns:
        List[tuple]: List of (index, similarity_score) tuples
    """
    try:
        similarities = []
        
        for i, candidate in enumerate(candidate_embeddings):
            similarity = cosine_similarity(query_embedding, candidate)
            similarities.append((i, similarity))
        
        # Sort by similarity score (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k results
        return similarities[:top_k]
        
    except Exception as e:
        raise Exception(f"Error finding similar embeddings: {str(e)}")

def get_embedding_dimension(model: str = None) -> int:
    """
    Get the dimension of embeddings for a given model
    
    Args:
        model (str): OpenAI embedding model name
        
    Returns:
        int: Embedding dimension
    """
    # Use default model if none specified
    if model is None:
        model = DEFAULT_EMBEDDING_MODEL
        
    # Known dimensions for OpenAI models
    model_dimensions = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072,
        "text-embedding-ada-002": 1536
    }
    
    return model_dimensions.get(model, 1536)  # Default to 1536

def validate_embedding(embedding: List[float], expected_dim: int = None) -> bool:
    """
    Validate embedding vector
    
    Args:
        embedding (List[float]): Embedding vector to validate
        expected_dim (int): Expected dimension (optional)
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        if not isinstance(embedding, list):
            return False
        
        if len(embedding) == 0:
            return False
        
        # Check if all elements are numbers
        for val in embedding:
            if not isinstance(val, (int, float)):
                return False
        
        # Check dimension if specified
        if expected_dim and len(embedding) != expected_dim:
            return False
        
        return True
        
    except Exception:
        return False