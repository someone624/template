import logging

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Set up a logger with the given name and logging level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:
        logger.addHandler(ch)

    return logger