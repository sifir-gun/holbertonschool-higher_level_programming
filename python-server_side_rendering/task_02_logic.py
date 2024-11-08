from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Read data from items.json
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []  # Default to an empty list if file not found or invalid

    # Render the items.html template with the items list
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
