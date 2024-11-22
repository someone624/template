import os

def get_config(key: str, default: str = None) -> str:
    """Get a configuration value from environment variables."""
    return os.getenv(key, default)