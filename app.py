import os
import socket
from flask import Flask

app = Flask(__name__)
bg_color = os.getenv('BG_COLOR', '#ffffff')
ip = socket.gethostbyname(socket.gethostname())

@app.route("/")
def index():
    return f"""
    <html><body style="background-color:{bg_color};">
    <h1>Hello from {ip}</h1>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

