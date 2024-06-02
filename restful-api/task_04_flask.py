#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify({"username": username, **user})
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["Post"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {key: data[key] for key in ("name", "age", "city")}

    return jsonify({
        "message": "User added",
        "user": {"username": username, **users[username]}
        }), 201


if __name__ == "__main__":
    app.run(debug=True)
