import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import webview
import subprocess
from multiprocessing import freeze_support
import time
from pypresence import Presence


def start_rich_presence(): # discord rich presence
    try:
        # rich presence
        client_id = "1538180761453072435"

        RPC = Presence(client_id)
        RPC.connect()

        # put status here
        RPC.update(
            details="Coding in PenguinMod",
            state="Unofficial Port by Wyte",
            start=time.time(),  # starts timer
            large_image="logo",
            large_text="PenguinMod",
            # small_image="placeholder",
            # small_text="placeholder",
            buttons=[
                {"label": "Visit Github", "url": "https://github.com/WyteHAHA/pmdesktop"}
            ]
        )

        print("discord rpc OK")
        while True:
            time.sleep(15)  # Updates every 15 seconds  
    except Exception:
        pass


# web
BUILD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')

def run_server():
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=BUILD_DIR, **kwargs)

    server = HTTPServer(('127.0.0.1', 8000), Handler)
    server.serve_forever()

if __name__ == '__main__':
    freeze_support() # stop it from tweaking

    # launch rpc
    threading.Thread(target=start_rich_presence, daemon=True).start()

    if not os.path.exists(BUILD_DIR):
        print(f"Error: Build directory isnt at {BUILD_DIR}")
        print("Wrong directory or not built?")
        sys.exit(1)

    # http server on port 8000
    threading.Thread(target=run_server, daemon=True).start()

    # Launch webview pointing to localhost:8000/editor.html
    webview.create_window('PenguinMod Desktop', 'http://127.0.0.1:8000/editor.html', width=1280, height=720)
    webview.start()