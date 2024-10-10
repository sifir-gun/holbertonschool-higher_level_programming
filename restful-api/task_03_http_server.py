#!/usr/bin/env python3
"""
This script sets up a basic HTTP server using Python's http.server module.
It handles various HTTP GET requests and serves plain text or JSON responses.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# Constants for Content Types
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_TEXT = 'text/plain'


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom handler for processing HTTP GET requests."""

    def do_GET(self):
        """Handle GET requests based on the request path."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/":
            self._send_plain_text_response(200, "Hello, this is a simple API!")
        elif path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)
        elif path == "/status":
            self._send_plain_text_response(200, "OK")
        elif path == "/info":
            data = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self._send_json_response(200, data)
        else:
            self._send_error_response(404, "404 Not Found: Endpoint not found")

    def _send_plain_text_response(self, status_code, message):
        """
        Send a plain text response with the provided status code and message.
        """
        self.send_response(status_code)
        self.send_header("Content-type", CONTENT_TYPE_TEXT)
        self.end_headers()
        self.wfile.write(message.encode())

    def _send_json_response(self, status_code, data):
        """Send a JSON response with the provided status code and data."""
        json_data = json.dumps(data)
        self.send_response(status_code)
        self.send_header("Content-type", CONTENT_TYPE_JSON)
        self.end_headers()
        self.wfile.write(json_data.encode())

    def _send_error_response(self, status_code, message):
        """Send an error response with the provided status code and message."""
        self.send_response(status_code)
        self.send_header("Content-type", CONTENT_TYPE_TEXT)
        self.end_headers()
        self.wfile.write(message.encode())


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """Set up and run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting http.server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
