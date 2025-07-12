import tiktoken
from typing import List

def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """
    Split text into chunks with specified size and overlap
    
    Args:
        text (str): Input text to chunk
        chunk_size (int): Maximum tokens per chunk
        chunk_overlap (int): Number of overlapping tokens between chunks
        
    Returns:
        List[str]: List of text chunks
    """
    # Initialize tokenizer
    encoding = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer
    
    # Tokenize the text
    tokens = encoding.encode(text)
    
    chunks = []
    start = 0
    
    while start < len(tokens):
        # Calculate end position
        end = start + chunk_size
        
        # Get chunk tokens
        chunk_tokens = tokens[start:end]
        
        # Decode back to text
        chunk_text = encoding.decode(chunk_tokens)
        
        # Clean up the chunk
        chunk_text = chunk_text.strip()
        
        if chunk_text:
            chunks.append(chunk_text)
        
        # Move start position with overlap
        start = end - chunk_overlap
        
        # Break if we've reached the end
        if end >= len(tokens):
            break
    
    return chunks

def chunk_text_by_sentences(text: str, max_chunk_size: int = 1000) -> List[str]:
    """
    Split text into chunks by sentences, respecting token limits
    
    Args:
        text (str): Input text to chunk
        max_chunk_size (int): Maximum tokens per chunk
        
    Returns:
        List[str]: List of text chunks
    """
    # Initialize tokenizer
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # Split by sentences (simple approach)
    sentences = text.replace('\n', ' ').split('. ')
    
    chunks = []
    current_chunk = ""
    current_tokens = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Add period back if it was removed
        if not sentence.endswith('.'):
            sentence += '.'
        
        # Count tokens for this sentence
        sentence_tokens = len(encoding.encode(sentence))
        
        # Check if adding this sentence would exceed the limit
        if current_tokens + sentence_tokens > max_chunk_size and current_chunk:
            # Save current chunk and start a new one
            chunks.append(current_chunk.strip())
            current_chunk = sentence
            current_tokens = sentence_tokens
        else:
            # Add sentence to current chunk
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence
            current_tokens += sentence_tokens
    
    # Add the last chunk if it exists
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    return chunks

def chunk_text_by_paragraphs(text: str, max_chunk_size: int = 1000) -> List[str]:
    """
    Split text into chunks by paragraphs, respecting token limits
    
    Args:
        text (str): Input text to chunk
        max_chunk_size (int): Maximum tokens per chunk
        
    Returns:
        List[str]: List of text chunks
    """
    # Initialize tokenizer
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # Split by paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    chunks = []
    current_chunk = ""
    current_tokens = 0
    
    for paragraph in paragraphs:
        # Count tokens for this paragraph
        paragraph_tokens = len(encoding.encode(paragraph))
        
        # If single paragraph exceeds limit, split it further
        if paragraph_tokens > max_chunk_size:
            # Save current chunk if it exists
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
                current_chunk = ""
                current_tokens = 0
            
            # Split large paragraph by sentences
            paragraph_chunks = chunk_text_by_sentences(paragraph, max_chunk_size)
            chunks.extend(paragraph_chunks)
            continue
        
        # Check if adding this paragraph would exceed the limit
        if current_tokens + paragraph_tokens > max_chunk_size and current_chunk:
            # Save current chunk and start a new one
            chunks.append(current_chunk.strip())
            current_chunk = paragraph
            current_tokens = paragraph_tokens
        else:
            # Add paragraph to current chunk
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph
            current_tokens += paragraph_tokens
    
    # Add the last chunk if it exists
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    return chunks

def get_chunk_info(chunks: List[str]) -> dict:
    """
    Get information about the chunks
    
    Args:
        chunks (List[str]): List of text chunks
        
    Returns:
        dict: Information about chunks
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    
    total_chunks = len(chunks)
    total_tokens = sum(len(encoding.encode(chunk)) for chunk in chunks)
    avg_tokens_per_chunk = total_tokens / total_chunks if total_chunks > 0 else 0
    
    chunk_sizes = [len(encoding.encode(chunk)) for chunk in chunks]
    min_chunk_size = min(chunk_sizes) if chunk_sizes else 0
    max_chunk_size = max(chunk_sizes) if chunk_sizes else 0
    
    return {
        'total_chunks': total_chunks,
        'total_tokens': total_tokens,
        'avg_tokens_per_chunk': round(avg_tokens_per_chunk, 2),
        'min_chunk_size': min_chunk_size,
        'max_chunk_size': max_chunk_size
    }