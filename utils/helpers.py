from datetime import datetime
import hashlib

def generate_session_seed(topic: str) -> str:
    return hashlib.md5(f"{topic}{datetime.now().timestamp()}".encode()).hexdigest()
