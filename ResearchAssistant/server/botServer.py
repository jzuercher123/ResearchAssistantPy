import http.server
import socketserver
import threading


class BotServer:
    def __init__(self):
        self.port = 8080
        self.server = None
        self.thread = None

    def start_server(self):
        handler = http.server.SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer(("", self.port), handler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()
        print(f"Server started at localhost:{self.port}")

    def stop_server(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            print("Server stopped")


# Usage
bot_server = BotServer()
bot_server.start_server()
# bot_server.stop_server()  # Uncomment this line to stop the server
