
import psycopg2
import traceback
from db.getConn import getConn

def getSecretFromDb(hash : str):
    conn = getConn()
    cur = conn.cursor()
    secret = []
    print(hash)
    getQuery = "SELECT secret FROM secrets WHERE link = %s;"
    didWork = False
    try:
              cur.execute(getQuery, (hash,))
              secret = cur.fetchall()
              didWork= True
    except Exception: 
              print(traceback.print_exc())
              didWork= False
              print("Something's wrong with getting stuff")
      
    cur.close()
    print(secret[0][0])
    return secret