#!/usr/bin/python3
"""This module contains restful-api tasks."""
from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    """class RequestHandler"""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello, this is a simple API!\n".encode("utf-8"))


server = HTTPServer(("localhost", 8000), RequestHandler)
print("Server started at http://localhost:8000")
server.serve_forever()
