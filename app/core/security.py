import secrets
import hashlib


def generate_api_key():
    """Generate a secure API key."""
    return "pk_" + secrets.token_urlsafe(32)


def hash_api_key(api_key: str):
    """Hash an API key before storing it."""
    return hashlib.sha256(api_key.encode("utf-8")).hexdigest()


def verify_api_key(api_key: str, hashed_key: str):
    """Verify an API key against its stored hash."""
    return secrets.compare_digest(
        hash_api_key(api_key),
        hashed_key
    )
