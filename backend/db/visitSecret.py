
import psycopg2
import traceback
from db.getConn import getConn

def getSecretFromDb(hash : str):
    conn = getConn()
    cur = conn.cursor()
    secret = []
    print(hash)
    getQuery = "SELECT secret FROM secrets WHERE link = %s;"
    try:
              cur.execute(getQuery, (hash,)) # The execute wants a tuple as parameter, that's the weird parameters.
              secret = cur.fetchall()
    except Exception: 
              print(traceback.print_exc())
              raise Exception("Select query can't be executed")
              
      
    cur.close()
    
    if(len(secret) == 0):
      return None
    elif(len(secret) > 1):
      raise Exception("WTF there are two secrets with the same hash.")
    else:
      return secret[0][0]
            