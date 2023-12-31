import re
import hashlib

def password_verification(password: str) -> int:
    if len(password) < 8:
        return 1
    
    match = re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[?!.,@£$%&*#;:])", password)

    if match:
        return 0
    else:
        return 2
    

def pass_to_hash(password: str):
    return hashlib.sha256(password.encode()).hexdigest()
