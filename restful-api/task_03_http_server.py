#!/usr/bin/env python3
"""
This script sets up a basic HTTP server using Python's http.server module.
It handles various HTTP GET requests and serves plain text or JSON responses.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom handler for processing HTTP GET requests."""

    def do_GET(self):
        """Handle GET requests based on the request path."""
        if self.path == "/":
            self._send_plain_text_response(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)
        elif self.path == "/status":
            self._send_plain_text_response(200, "OK")
        elif self.path == "/info":
            data = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self._send_json_response(200, data)
        else:
            self.send_error(404, "Endpoint not found")

    def _send_plain_text_response(self, status_code, message):
        """
        Send a plain text response with the provided status code and message.
        """
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", str(len(message.encode())))
        self.end_headers()
        self.wfile.write(message.encode())

    def _send_json_response(self, status_code, data):
        """Send a JSON response with the provided status code and data."""
        json_data = json.dumps(data)
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(json_data.encode())))
        self.end_headers()
        self.wfile.write(json_data.encode())


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """Set up and run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting http.server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
