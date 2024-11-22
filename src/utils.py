import logging
import os

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Set up a logger with the given name and logging level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    if not logger.handlers:  # Avoid duplicate handlers
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

def get_config(key: str, default: str = None) -> str:
    """Get a configuration value from environment variables."""
    return os.getenv(key, default)