import secrets
import os
import string
from fastapi import HTTPException, Header

def generate_api_key(length: int = 40) -> str:
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+-[]{}|;:,.<>?`~'
    api_key = ''.join(secrets.choice(characters) for _ in range(length))
    return api_key

async def get_api_key(api_key: str = Header(None)):
    API_KEY = os.getenv("API_KEY")
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="无效或缺失的API密钥"
        )
    return api_key

if __name__ == "__main__":
    # Example usage
    print("Generated API Key:", generate_api_key())