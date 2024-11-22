from flask import Flask
from .user_controller import user_blueprint
from .product_controller import product_blueprint
from .auth_controller import auth_blueprint

def register_routes(app: Flask):
    app.register_blueprint(user_blueprint, url_prefix="/api/users")
    app.register_blueprint(product_blueprint, url_prefix="/api/products")
    app.register_blueprint(auth_blueprint, url_prefix="/api/auth")