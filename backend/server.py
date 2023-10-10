from flask import Flask, Response
# from manageSecret.manageSecret import manageSecret
from model.secretData import secretData
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.post("/createSecret")
def createSecret():
    return Response("igen", status=200, mimetype='application/json')
    # data = secretData("igen", 5, "")
    # manageSecret()