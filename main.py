from flask import Flask, request

app = Flask(__name__)

@app.before_request
def before_request():
    request.remote_addr = request.headers.get('X-Forwarded-For', request.remote_addr)

@app.route("/")
def index():
    ip_address = request.remote_addr
    return f"Your IP address is: {ip_address}"

@app.route("/alive")
def alive():
    return "alive"
