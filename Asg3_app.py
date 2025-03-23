from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello this is Auto scalable to AWS!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
