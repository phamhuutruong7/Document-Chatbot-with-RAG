import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

class SessionManager:
    """Manages chat sessions with unique IDs and metadata."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.sessions_file = self.data_dir / "sessions.json"
        self.chat_history_file = self.data_dir / "chat_history.json"
        
    def create_new_session(self, name: Optional[str] = None) -> str:
        """Create a new chat session and return its ID."""
        session_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        session_data = {
            "id": session_id,
            "name": name or f"Session {timestamp[:16]}",
            "created_at": timestamp,
            "last_updated": timestamp,
            "message_count": 0,
            "documents_uploaded": []
        }
        
        # Load existing sessions
        sessions = self.load_sessions()
        sessions[session_id] = session_data
        
        # Save sessions
        with open(self.sessions_file, 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
            
        # Initialize empty chat history for this session
        all_chat_history = self.load_chat_history()
        all_chat_history[session_id] = []
        self.save_chat_history(all_chat_history)
        
        return session_id
    
    def load_sessions(self) -> Dict:
        """Load all sessions metadata."""
        if not self.sessions_file.exists():
            return {}
        
        try:
            with open(self.sessions_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    
    def get_session(self, session_id: str) -> Optional[Dict]:
        """Get session metadata by ID."""
        sessions = self.load_sessions()
        return sessions.get(session_id)
    
    def update_session(self, session_id: str, **kwargs):
        """Update session metadata."""
        sessions = self.load_sessions()
        if session_id in sessions:
            sessions[session_id].update(kwargs)
            sessions[session_id]["last_updated"] = datetime.now().isoformat()
            
            with open(self.sessions_file, 'w', encoding='utf-8') as f:
                json.dump(sessions, f, indent=2, ensure_ascii=False)
    
    def delete_session(self, session_id: str):
        """Delete a session and its chat history."""
        # Remove from sessions
        sessions = self.load_sessions()
        if session_id in sessions:
            del sessions[session_id]
            with open(self.sessions_file, 'w', encoding='utf-8') as f:
                json.dump(sessions, f, indent=2, ensure_ascii=False)
        
        # Remove chat history
        chat_history = self.load_chat_history()
        if session_id in chat_history:
            del chat_history[session_id]
            self.save_chat_history(chat_history)
    
    def load_chat_history(self, session_id: Optional[str] = None) -> Dict:
        """Load chat history for all sessions or a specific session."""
        if not self.chat_history_file.exists():
            return {}
        
        try:
            with open(self.chat_history_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Handle legacy format where chat_history.json contains a list instead of dict
            if isinstance(data, list):
                # Convert legacy format to new format
                all_history = {"legacy_session": data}
                # Save in correct format
                self.save_chat_history(all_history)
            else:
                all_history = data
                
            if session_id:
                return all_history.get(session_id, [])
            return all_history
        except (json.JSONDecodeError, FileNotFoundError):
            return {} if not session_id else []
    
    def save_chat_history(self, chat_history: Dict):
        """Save chat history for all sessions."""
        with open(self.chat_history_file, 'w', encoding='utf-8') as f:
            json.dump(chat_history, f, indent=2, ensure_ascii=False)
    
    def add_message_to_session(self, session_id: str, message: Dict):
        """Add a message to a specific session's chat history."""
        chat_history = self.load_chat_history()
        if session_id not in chat_history:
            chat_history[session_id] = []
        
        chat_history[session_id].append(message)
        self.save_chat_history(chat_history)
        
        # Update session metadata
        self.update_session(session_id, message_count=len(chat_history[session_id]))
    
    def clear_session_history(self, session_id: str):
        """Clear chat history for a specific session."""
        chat_history = self.load_chat_history()
        if session_id in chat_history:
            chat_history[session_id] = []
            self.save_chat_history(chat_history)
            self.update_session(session_id, message_count=0)
    
    def get_session_list(self) -> List[Dict]:
        """Get list of all sessions sorted by last updated."""
        sessions = self.load_sessions()
        session_list = list(sessions.values())
        return sorted(session_list, key=lambda x: x.get('last_updated', ''), reverse=True)
    
    def list_sessions(self) -> List[Dict]:
        """Alias for get_session_list for backward compatibility."""
        return self.get_session_list()