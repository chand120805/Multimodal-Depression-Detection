from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt_text(text: str) -> str:
    return fernet.encrypt(text.encode()).decode()

def decrypt_text(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()