from db.visitSecret import getSecretFromDb
from encrypt import decryptSecret
def get_secret_by_hash(hash: str, envVariables):
    try:
        secret = getSecretFromDb(hash, envVariables)
        return decryptSecret(secret)
    except:
        raise
    