
import json
from flask import Flask, Response, request
from service import createSecretService
from dotenv import dotenv_values
from db import init
from encrypt import decryptSecret


app = Flask(__name__)
@app.post("/api/v1/secret")
def createSecretEndpoint():
    data = json.loads(request.data.decode()) #This is a dictionary. 
    try:
        link = createSecretService.create_secret_dao(data, envVariables)
        return Response(link, status=200, mimetype='text/html')
    except Exception as e:
        return Response(str(e), status=400, mimetype='text/html')  

@app.post("/api/v1/getSecret")
def getSecretByHash():
    data : dict = json.loads(request.data.decode())
    secret = decryptSecret(data)
    return Response(json.dumps(secret), status=200, mimetype='application/json')

if(__name__ == '__main__'):
    envVariables = dotenv_values("./db/.env")
    app.run(debug=True)
    init(envVariables)
