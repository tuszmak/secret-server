import psycopg2
import os
from dotenv import load_dotenv

# This function only exists to reduce code duplication.
load_dotenv()

def getConn():
    conn = psycopg2.connect(
              host="localhost",
              database="secret-server",
              user=os.environ['DB_USERNAME'],
              password=os.environ['DB_PASSWORD'])
      
    return conn