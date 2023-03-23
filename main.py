from fastapi import FastAPI

app = FastAPI()

@app.route("/")
def index():
    return "Hello world"

@app.route("/main")
def main():
    return "main"
