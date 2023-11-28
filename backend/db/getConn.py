import psycopg2
import os
# This function only exists to reduce code duplication.
def getConn():
    conn = psycopg2.connect(
              host="localhost",
              database="secret-server",
              user=os.environ['DB_USERNAME'],
              password=os.environ['DB_PASSWORD'])
      
    return conn