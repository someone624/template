from .user_controller import UserController
from .product_controller import ProductController
from .auth_controller import AuthController

# Export all controllers as part of the package API
__all__ = ["UserController", "ProductController", "AuthController"]