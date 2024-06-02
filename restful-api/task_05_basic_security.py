#!/usr/bin/python3
"""Flask"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from functools import wraps


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)


"""In-memory user storage"""
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role": "user"},
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password2"),
        "role": "admin"}
}


"""User data retrieval function"""


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        a_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]})
        return jsonify({"access_token": a_token})
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})


def role_required(role):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            claims = get_jwt()
            if claims['role'] != role:
                return jsonify({"message": "Forbidden"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.route('/admin-only')
@role_required('admin')
def admin_only():
    return jsonify({"message": "Admin Access: Granted"})


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
