"""
This script sets up a basic HTTP server using Python's
built-in http.server module.
It handles various HTTP GET requests and serves plain text or JSON responses.

Modules:
    json: Provides functionality for working with JSON data.
    http.server: Provides classes for implementing HTTP servers.

Classes:
    SimpleHTTPRequestHandler: Custom handler for processing HTTP GET requests.
        - Handles specific endpoints and returns responses based on the request

Functions:
    run: Initializes and starts the HTTP server.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Custom handler for processing HTTP GET requests.

    Handles the following endpoints:
    - "/" : Returns a simple plain text message.
    - "/data" : Returns a JSON response with a sample dataset.
    - "/status" : Returns a plain text 'OK' message.
    For any other endpoint, returns a 404 Not Found error.
    """

    def do_GET(self):
        """Handle GET requests based on the request path."""
        if self.path == "/":
            self._send_plain_text_response(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)
        elif self.path == "/status":
            self._send_plain_text_response(200, "OK")
        else:
            self._send_plain_text_response(
                404, "404 Not Found: Endpoint not found")

    def _send_plain_text_response(self, status_code, message):
        """
        Send a plain text response with the provided status code and message.
        """
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

    def _send_json_response(self, status_code, data):
        """Send a JSON response with the provided status code and data."""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Set up and run the HTTP server.

    Args:
        server_class:
        The class to use for the HTTP server (default: HTTPServer).
        handler_class:
        The request handler class (default: SimpleHTTPRequestHandler).
        port: The port on which the server will listen (default: 8000).
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting http.server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
