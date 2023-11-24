import os
import sys
import traceback


from dotenv import load_dotenv
from model.secretData import SecretData
import psycopg2
load_dotenv()
def createSecret(data: SecretData):
        
        print("Insert data")
        conn = psycopg2.connect(
                host="localhost",
                database="secret-server",
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'])
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Execute a command: this creates a new table
        insert_query = "INSERT INTO secrets (link, rem_visits, expiry_date) VALUES (%s, %s, %s);"
        didWork = False
        try:
                cur.execute(insert_query, (data.text, data.numberOfVisits, data.expDate))
                conn.commit()
                didWork= True
        except Exception: 
                print(traceback.print_exc())
                didWork= False
                print("Something's wrong with insert")
        
        cur.close()
        return didWork
        