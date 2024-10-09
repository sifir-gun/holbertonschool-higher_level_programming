#!/usr/bin/env python3
"""
This script sets up a simple Flask web application to demonstrate API routing,
JSON data handling, and basic request-response cycles.
"""

from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# Dictionary to store users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city":
             "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """Handle the root endpoint and return a welcome message."""
    return Response("Welcome to the Flask API!", mimetype='text/plain')


@app.route('/data')
def get_users():
    """Return a JSON response with a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return the status of the API."""
    return Response("OK", mimetype='text/plain')


@app.route('/users/<username>')
def get_user(username):
    """Return the full object corresponding to the provided username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Handle POST requests to add a new user."""
    data = request.get_json()

    # Check if the username is provided
    if not data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    # Add the user to the dictionary
    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
