import time
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class RAGMetrics:
    """Data class for RAG operation metrics."""
    query: str
    session_id: str
    timestamp: str
    retrieval_time: float
    generation_time: float
    total_time: float
    chunks_retrieved: int
    top_chunk_score: float
    avg_chunk_score: float
    response_length: int
    model_used: str
    embedding_model: str
    
class RAGTracer:
    """Traces and monitors RAG pipeline operations."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.metrics_file = self.data_dir / "rag_metrics.json"
        self.current_operation = {}
        
    def start_operation(self, query: str, session_id: str, model: str, embedding_model: str):
        """Start tracking a new RAG operation."""
        operation_id = f"{session_id}_{int(time.time() * 1000)}"
        self.current_operation[operation_id] = {
            "query": query,
            "session_id": session_id,
            "model_used": model,
            "embedding_model": embedding_model,
            "start_time": time.time(),
            "retrieval_start": None,
            "retrieval_end": None,
            "generation_start": None,
            "generation_end": None,
            "chunks_retrieved": 0,
            "chunk_scores": [],
            "response_length": 0
        }
        return operation_id
    
    def start_retrieval(self, operation_id: str):
        """Mark the start of retrieval phase."""
        if operation_id in self.current_operation:
            self.current_operation[operation_id]["retrieval_start"] = time.time()
    
    def end_retrieval(self, operation_id: str, chunks: List[Dict], scores: List[float]):
        """Mark the end of retrieval phase and record metrics."""
        if operation_id in self.current_operation:
            op = self.current_operation[operation_id]
            op["retrieval_end"] = time.time()
            op["chunks_retrieved"] = len(chunks)
            op["chunk_scores"] = scores
    
    def start_generation(self, operation_id: str):
        """Mark the start of generation phase."""
        if operation_id in self.current_operation:
            self.current_operation[operation_id]["generation_start"] = time.time()
    
    def end_generation(self, operation_id: str, response: str):
        """Mark the end of generation phase and record response."""
        if operation_id in self.current_operation:
            op = self.current_operation[operation_id]
            op["generation_end"] = time.time()
            op["response_length"] = len(response)
    
    def complete_operation(self, operation_id: str) -> RAGMetrics:
        """Complete the operation and save metrics."""
        if operation_id not in self.current_operation:
            return None
            
        op = self.current_operation[operation_id]
        end_time = time.time()
        
        # Calculate timings with proper null checks
        retrieval_start = op.get("retrieval_start") or op["start_time"]
        retrieval_end = op.get("retrieval_end") or end_time
        generation_start = op.get("generation_start") or retrieval_end
        generation_end = op.get("generation_end") or end_time
        
        retrieval_time = retrieval_end - retrieval_start
        generation_time = generation_end - generation_start
        total_time = end_time - op["start_time"]
        
        # Calculate chunk score statistics
        scores = op.get("chunk_scores", [])
        top_score = max(scores) if scores else 0.0
        avg_score = sum(scores) / len(scores) if scores else 0.0
        
        # Create metrics object
        metrics = RAGMetrics(
            query=op["query"],
            session_id=op["session_id"],
            timestamp=datetime.now().isoformat(),
            retrieval_time=retrieval_time,
            generation_time=generation_time,
            total_time=total_time,
            chunks_retrieved=op["chunks_retrieved"],
            top_chunk_score=top_score,
            avg_chunk_score=avg_score,
            response_length=op["response_length"],
            model_used=op["model_used"],
            embedding_model=op["embedding_model"]
        )
        
        # Save metrics
        self.save_metrics(metrics)
        
        # Clean up
        del self.current_operation[operation_id]
        
        return metrics
    
    def save_metrics(self, metrics: RAGMetrics):
        """Save metrics to file."""
        # Load existing metrics
        all_metrics = self.load_all_metrics()
        
        # Add new metrics
        all_metrics.append(asdict(metrics))
        
        # Keep only last 1000 entries to prevent file from growing too large
        if len(all_metrics) > 1000:
            all_metrics = all_metrics[-1000:]
        
        # Save to file
        with open(self.metrics_file, 'w', encoding='utf-8') as f:
            json.dump(all_metrics, f, indent=2, ensure_ascii=False)
    
    def load_all_metrics(self) -> List[Dict]:
        """Load all saved metrics."""
        if not self.metrics_file.exists():
            return []
        
        try:
            with open(self.metrics_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def get_session_metrics(self, session_id: str, limit: int = 50) -> List[Dict]:
        """Get metrics for a specific session."""
        all_metrics = self.load_all_metrics()
        session_metrics = [m for m in all_metrics if m.get('session_id') == session_id]
        return session_metrics[-limit:] if limit else session_metrics
    
    def get_recent_metrics(self, limit: int = 20) -> List[Dict]:
        """Get most recent metrics across all sessions."""
        all_metrics = self.load_all_metrics()
        return all_metrics[-limit:] if limit else all_metrics
    
    def get_performance_stats(self, session_id: Optional[str] = None) -> Dict[str, Any]:
        """Get performance statistics."""
        if session_id:
            metrics = self.get_session_metrics(session_id, limit=None)
        else:
            metrics = self.load_all_metrics()
        
        if not metrics:
            return {}
        
        # Calculate statistics
        total_times = [m['total_time'] for m in metrics]
        retrieval_times = [m['retrieval_time'] for m in metrics]
        generation_times = [m['generation_time'] for m in metrics]
        chunk_counts = [m['chunks_retrieved'] for m in metrics]
        top_scores = [m['top_chunk_score'] for m in metrics]
        
        return {
            "total_queries": len(metrics),
            "avg_total_time": sum(total_times) / len(total_times),
            "avg_retrieval_time": sum(retrieval_times) / len(retrieval_times),
            "avg_generation_time": sum(generation_times) / len(generation_times),
            "avg_chunks_retrieved": sum(chunk_counts) / len(chunk_counts),
            "avg_top_score": sum(top_scores) / len(top_scores),
            "min_total_time": min(total_times),
            "max_total_time": max(total_times),
            "min_top_score": min(top_scores) if top_scores else 0,
            "max_top_score": max(top_scores) if top_scores else 0
        }
    
    def clear_session_metrics(self, session_id: str):
        """Clear metrics for a specific session."""
        all_metrics = self.load_all_metrics()
        filtered_metrics = [m for m in all_metrics if m.get('session_id') != session_id]
        
        with open(self.metrics_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_metrics, f, indent=2, ensure_ascii=False)