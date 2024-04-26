from flask import Flask, jsonify, make_response, request
from utils import auth_required
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify("Flask has started successfully"), 200

@app.route("/home")
@auth_required
def home():
    return "<h1>Welcome Jaduong</h1>"

if __name__ == "__main__":
    app.run(debug=True)