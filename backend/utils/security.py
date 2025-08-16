import secrets
import string

# generate_api_key: function to create a secure API key
def generate_api_key(length: int = 40) -> str:
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?`~'
    api_key = ''.join(secrets.choice(characters) for _ in range(length))
    return api_key