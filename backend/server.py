
import json
from flask import Flask, Response, request
from service import createSecretService
from dotenv import dotenv_values
from db import init
from encrypt import decryptSecret


app = Flask(__name__)
envVariables = dotenv_values("./db/.env")
@app.post("/api/v1/secret")
def createSecretEndpoint():
    data = json.loads(request.data.decode()) #This is a dictionary. 
    link = createSecretService.createSecretDAO(data, envVariables)
    return Response(link, status=200, mimetype='text/html')
@app.post("/api/v1/getSecret")
def getSecretByHash():
    data : dict = json.loads(request.data.decode())
    parsedHash = data.get("hash")
    secret = decryptSecret(parsedHash)
    responseData = {"secret": secret}
    return Response(json.dumps(responseData), status=200, mimetype='application/json')
if(__name__ == '__main__'):
    app.run(debug=True)
    init(envVariables)
