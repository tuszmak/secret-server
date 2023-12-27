import psycopg2
import os
from dotenv import load_dotenv

# This function only exists to reduce code duplication.
load_dotenv()

def getConn():
    conn = psycopg2.connect(
              host=os.environ['DB_HOST'],
              database=os.environ['DB_NAME'],
              user=os.environ['DB_USERNAME'],
              password=os.environ['DB_PASSWORD'])
      
    return conn