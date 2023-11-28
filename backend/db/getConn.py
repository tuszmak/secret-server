import psycopg2
import os
def getConn():
    conn = psycopg2.connect(
              host="localhost",
              database="secret-server",
              user=os.environ['DB_USERNAME'],
              password=os.environ['DB_PASSWORD'])
      
      # Open a cursor to perform database operations
    return conn