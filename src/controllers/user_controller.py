from flask import Blueprint, request, jsonify
from ..models.user_model import User
from ..utils.validation import validate_email

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/register", methods=["POST"])
def register_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    if not validate_email(email):
        return jsonify({"error": "Invalid email address"}), 400
    
    user = User.create(email=email, password=password)
    return jsonify({"message": "User registered successfully", "user_id": user.id}), 201

@user_blueprint.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.get_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())