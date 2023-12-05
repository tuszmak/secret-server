import shortuuid
from base64 import b64encode, b64decode
import db
def encryptSecret(secret: str):
     foo = b64encode(secret.encode("ascii"))
     return foo.decode("ascii")
def generateLink():
    return shortuuid.uuid()
def decryptSecret(input: str):
    secret :str = db.getSecretFromDb(input)
    if(secret != ""):
        secretBytes = b64decode(secret.encode())
        foo = secretBytes.decode("ascii")
        return foo
