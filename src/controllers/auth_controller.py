from flask import Blueprint, request, jsonify
from ..models.user_model import User
from ..utils.auth_utils import generate_token

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    user = User.authenticate(email, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = generate_token(user.id)
    return jsonify({"message": "Login successful", "token": token})