from flask import Flask
from src.controllers.route_mapper import register_routes

app = Flask(__name__)

# Register all routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)