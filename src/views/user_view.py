from flask import jsonify, render_template
from src.models.user_model import User

def get_user(user_id):
    # Fetch user data from the model
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    else:
        return jsonify({"error": "User not found"}), 404

def render_user_template(user_id):
    # Render a user profile page in HTML
    user = User.query.get(user_id)
    if user:
        return render_template('user_template.html', user=user)
    else:
        return "User not found", 404
