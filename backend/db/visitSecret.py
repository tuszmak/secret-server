
import psycopg2
import traceback
from .getConn import getConn

def getSecretFromDb(hash : str):
    conn = getConn()
    cur = conn.cursor()
    secret = []
    getQuery = "SELECT secret FROM secrets WHERE link = %s;"
    #TODO Update query to reduce visits by 1  
    try:
              cur.execute(getQuery, (hash,)) # The execute wants a tuple as parameter, that's the weird parameters.
              secret = cur.fetchall()
              
    except Exception: 
              raise Exception("Select query can't be executed")
    cur.close()
    
    if(len(secret) == 0):
      return None
    elif(len(secret) > 1):
      raise Exception("There are multiple secrets with the same hash.")
    else:
      return secret[0][0]
            