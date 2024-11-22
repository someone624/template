from flask import Flask
from src.utils import setup_logger, get_config

# Initialize app and logger
app = Flask(__name__)
logger = setup_logger("main")

@app.route("/")
def home():
    """Home endpoint."""
    logger.info("Home endpoint was accessed.")
    return {"message": "Welcome to the API!"}

if __name__ == "__main__":
    # Load configuration
    port = int(get_config("APP_PORT", 5000))
    debug = get_config("DEBUG", "false").lower() == "true"

    logger.info(f"Starting application on port {port}")
    app.run(host="0.0.0.0", port=port, debug=debug)