#!/usr/bin/env python3
"""
This script sets up a simple Flask web application to demonstrate API routing,
JSON data handling, and basic request-response cycles.

It provides endpoints to:

- Display a welcome message at the root URL (`/`).
- Return a list of usernames at `/data`.
- Check the API status at `/status`.
- Retrieve user information at `/users/<username>`.
- Add a new user via a POST request to `/add_user`.

Modules:

- Flask: A lightweight web framework for creating web applications and APIs.
- jsonify: A utility function to convert Python data structures to JSON format.
- request: Handles incoming requests, allowing access to headers and data.
- Response: Used to customize response objects,
including headers and mimetypes.
"""


from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# In-memory dictionary to store users
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """
    Handle the root endpoint and return a welcome message.

    Returns:
        Response: A plain text welcome message.
    """
    return Response("Welcome to the Flask API!", mimetype='text/plain')


@app.route('/data')
def get_users():
    """
    Return a JSON response with a list of all usernames.

    Returns:
        Response: A JSON array of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Return the status of the API.

    Returns:
        Response: A plain text message indicating the API status.
    """
    return Response("OK", mimetype='text/plain')


@app.route('/users/<username>')
def get_user(username):
    """
    Return the full user object corresponding to the provided username.

    Args:
        username (str): The username to retrieve.

    Returns:
        Response: A JSON object of user details if found,
                  else a JSON error message with a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handle POST requests to add a new user.

    Expects JSON data containing 'username', 'name', 'age', and 'city'.

    Returns:
        Response: A confirmation message with the added user's data,
                  or an error message if 'username' is missing.
    """
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

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
