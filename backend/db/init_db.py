import os
import sys


from dotenv import load_dotenv
from .getConn import getConn
import psycopg2
load_dotenv()
def init():
        
        print(os.environ.get('DB_USERNAME'))
        conn = getConn()
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Execute a command: this creates a new table
        cur.execute('CREATE TABLE IF NOT EXISTS secrets (id serial PRIMARY KEY,'
                                         'link varchar (150) NOT NULL,'
                                         'secret varchar (150) NOT NULL,'
                                         'rem_visits integer NOT NULL,'
                                         'expiry_date timestamp NOT NULL);'
                                         )
        
        
        conn.commit()
        
        cur.close()
        