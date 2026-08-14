import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import webview

# Path to your 'build' directory
BUILD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')

def run_server():
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=BUILD_DIR, **kwargs)

    server = HTTPServer(('127.0.0.1', 8000), Handler)
    server.serve_forever()

if __name__ == '__main__':
    if not os.path.exists(BUILD_DIR):
        print(f"Error: Build directory isnt at {BUILD_DIR}")
        print("Wrong directory or not built?")
        sys.exit(1)

    # http server on port 8000
    threading.Thread(target=run_server, daemon=True).start()

    # Launch webview pointing to localhost:8000/editor.html
    webview.create_window('PenguinMod Desktop', 'http://127.0.0.1:8000/editor.html', width=1280, height=720)
    webview.start()