"""
This script sets up a simple Flask web application to demonstrate API routing,
JSON data handling, and basic request-response cycles.

It uses the following Flask components:
- Flask: To create the web application.
- jsonify: To convert Python objects (dictionaries, lists) to JSON responses.
- request: To handle incoming HTTP requests, including JSON data parsing.

Modules:
    - Flask: A lightweight web framework for creating web applications and APIs
    - jsonify: A utility that converts Python data structures to JSON format.
    - request: Handles incoming requests, allowing access to headers and data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28,
             "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """
    Handle the root endpoint and return a welcome message.

    Returns:
        str: A welcome message for the API.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    """
    Return a JSON response with a list of all usernames.

    Returns:
        Response: A JSON response containing the usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Return the status of the API.

    Returns:
        str: API status message.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Return the full object corresponding to the provided username.

    Args:
        username (str): The username to search for.

    Returns:
        Response: JSON object of user details if found,
        else a 404 error message.
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

    # Vérifier si le nom d'utilisateur est fourni
    if not data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    # Ajouter l'utilisateur au dictionnaire
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
    app.run(debug=True)
