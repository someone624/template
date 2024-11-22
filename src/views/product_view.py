from flask import jsonify, render_template
from src.models.product_model import Product

def get_product(product_id):
    # Fetch product data from the model
    product = Product.query.get(product_id)
    if product:
        return jsonify({"id": product.id, "name": product.name, "price": product.price}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

def render_product_template(product_id):
    # Render a product details page in HTML
    product = Product.query.get(product_id)
    if product:
        return render_template('product_template.html', product=product)
    else:
        return "Product not found", 404
