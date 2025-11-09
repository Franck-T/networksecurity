from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with a 200 OK
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()

        # Write a response body
        message = "Hello, world! 👋 Python built-in HTTP server is working."
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("✅ Server running on http://0.0.0.0:8080")
    httpd.serve_forever()
