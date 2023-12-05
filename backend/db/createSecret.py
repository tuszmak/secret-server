import traceback
from model import SecretData
from .getConn import getConn
from encrypt import generateLink, encryptSecret

def createSecret(data: SecretData):
        print("Insert data")
        conn = getConn()
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Execute a command: this creates a new table
        insert_query = "INSERT INTO secrets (link, secret, rem_visits, expiry_date) VALUES (%s, %s, %s, %s);"
        didWork = False
        try:
                cur.execute(insert_query, (generateLink(), encryptSecret(data.text), data.numberOfVisits, data.expDate))
                conn.commit()
                didWork= True
        except Exception: 
                print(traceback.print_exc())
                didWork= False
                print("Something's wrong with insert")
        
        cur.close()
        return didWork
        