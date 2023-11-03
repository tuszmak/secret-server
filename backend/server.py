
import sys
 
# setting path

from flask import Flask, Response, Request
from manageSecret.manageSecret import manageSecret
from model.secretData import secretData
from datetime import datetime
sys.path.append('../')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.post("/api/createSecret")
def createSecret():
    print("Fetch is here!")
    manageSecret(None)
    return Response("igen", status=200, mimetype='application/json')
    # data = secretData("igen", 5, "")