import functools
import time
import logging
import streamlit as st
from typing import Callable, Any, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def handle_errors(default_return: Any = None, show_error: bool = True):
    """Decorator to handle errors gracefully with optional Streamlit error display."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_msg = f"Error in {func.__name__}: {str(e)}"
                logger.error(error_msg, exc_info=True)
                
                if show_error:
                    st.error(f"⚠️ {error_msg}")
                
                return default_return
        return wrapper
    return decorator

def log_execution_time(func: Callable) -> Callable:
    """Decorator to log function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"{func.__name__} executed in {execution_time:.3f} seconds")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"{func.__name__} failed after {execution_time:.3f} seconds: {str(e)}")
            raise
    return wrapper

def cache_with_ttl(ttl_seconds: int = 300):
    """Decorator to cache function results with time-to-live."""
    def decorator(func: Callable) -> Callable:
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from function name, args, and kwargs
            cache_key = f"{func.__name__}_{hash(str(args) + str(sorted(kwargs.items())))}"
            current_time = time.time()
            
            # Check if cached result exists and is still valid
            if cache_key in cache:
                cached_result, cached_time = cache[cache_key]
                if current_time - cached_time < ttl_seconds:
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cached_result
            
            # Execute function and cache result
            result = func(*args, **kwargs)
            cache[cache_key] = (result, current_time)
            logger.debug(f"Cache miss for {func.__name__}, result cached")
            
            # Clean up old cache entries
            expired_keys = [
                key for key, (_, cached_time) in cache.items()
                if current_time - cached_time >= ttl_seconds
            ]
            for key in expired_keys:
                del cache[key]
            
            return result
        return wrapper
    return decorator

def retry_on_failure(max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator to retry function execution on failure with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    
                    if attempt < max_retries:
                        logger.warning(
                            f"Attempt {attempt + 1} failed for {func.__name__}: {str(e)}. "
                            f"Retrying in {current_delay:.1f} seconds..."
                        )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(
                            f"All {max_retries + 1} attempts failed for {func.__name__}: {str(e)}"
                        )
            
            raise last_exception
        return wrapper
    return decorator

def validate_inputs(validators):
    """Decorator to validate function inputs.
    
    Args:
        validators: List of tuples (validator_func, error_message) or dict of {param_name: validator_func}
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Handle list of validators (for first parameter)
            if isinstance(validators, list):
                # Get the first parameter value
                param_names = list(sig.parameters.keys())
                if param_names and len(args) > 0:
                    first_param_value = args[0]
                    
                    # Apply each validator to the first parameter
                    for validator_func, error_message in validators:
                        if not validator_func(first_param_value):
                            raise ValueError(error_message)
            
            # Handle dict of validators (for named parameters)
            elif isinstance(validators, dict):
                for param_name, validator_func in validators.items():
                    if param_name in bound_args.arguments:
                        value = bound_args.arguments[param_name]
                        if not validator_func(value):
                            raise ValueError(f"Invalid value for parameter '{param_name}': {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def streamlit_spinner(message: str = "Processing..."):
    """Decorator to show Streamlit spinner during function execution."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with st.spinner(message):
                return func(*args, **kwargs)
        return wrapper
    return decorator

def log_user_action(action_type: Optional[str] = None, session_id: Optional[str] = None):
    """Decorator to log user actions for analytics."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                
                log_data = {
                    "action_type": action_type or func.__name__,
                    "function_name": func.__name__,
                    "session_id": session_id or getattr(st.session_state, 'current_session_id', 'unknown'),
                    "timestamp": start_time.isoformat(),
                    "duration_seconds": duration,
                    "status": "success"
                }
                
                logger.info(f"User action logged: {log_data}")
                return result
                
            except Exception as e:
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                
                log_data = {
                    "action_type": action_type or func.__name__,
                    "function_name": func.__name__,
                    "session_id": session_id or getattr(st.session_state, 'current_session_id', 'unknown'),
                    "timestamp": start_time.isoformat(),
                    "duration_seconds": duration,
                    "status": "error",
                    "error_message": str(e)
                }
                
                logger.error(f"User action failed: {log_data}")
                raise
        return wrapper
    return decorator

def rate_limit(calls_per_minute: int = 60):
    """Decorator to rate limit function calls."""
    def decorator(func: Callable) -> Callable:
        call_times = []
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Remove calls older than 1 minute
            call_times[:] = [t for t in call_times if current_time - t < 60]
            
            # Check if rate limit exceeded
            if len(call_times) >= calls_per_minute:
                raise Exception(
                    f"Rate limit exceeded: {calls_per_minute} calls per minute for {func.__name__}"
                )
            
            # Record this call
            call_times.append(current_time)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Validation functions for common use cases
def is_non_empty_string(value: Any) -> bool:
    """Validate that value is a non-empty string."""
    return isinstance(value, str) and len(value.strip()) > 0

def is_positive_number(value: Any) -> bool:
    """Validate that value is a positive number."""
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False

def is_valid_file_size(value: Any, max_size_mb: int = 10) -> bool:
    """Validate file size is within limits."""
    try:
        size_bytes = getattr(value, 'size', 0)
        size_mb = size_bytes / (1024 * 1024)
        return size_mb <= max_size_mb
    except:
        return False

def is_valid_file_extension(value: Any, allowed_extensions: list = None) -> bool:
    """Validate file extension is allowed."""
    if allowed_extensions is None:
        allowed_extensions = ['.pdf', '.txt', '.docx', '.md']
    
    try:
        filename = getattr(value, 'name', str(value))
        extension = '.' + filename.split('.')[-1].lower() if '.' in filename else ''
        return extension in [ext.lower() for ext in allowed_extensions]
    except:
        return False