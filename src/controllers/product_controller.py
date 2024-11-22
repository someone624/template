from flask import Blueprint, request, jsonify
from ..models.product_model import Product

product_blueprint = Blueprint("product", __name__)

@product_blueprint.route("/products", methods=["POST"])
def create_product():
    data = request.json
    name = data.get("name")
    price = data.get("price")
    
    if not name or not isinstance(price, (int, float)):
        return jsonify({"error": "Invalid product data"}), 400
    
    product = Product.create(name=name, price=price)
    return jsonify({"message": "Product created successfully", "product_id": product.id}), 201

@product_blueprint.route("/products", methods=["GET"])
def list_products():
    products = Product.get_all()
    return jsonify([product.to_dict() for product in products])