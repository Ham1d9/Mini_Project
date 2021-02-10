import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DB = os.environ.get("DB")
PORT = int(os.environ.get("PORT"))


def connection():
    return pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, port=PORT)

def query(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def update(conn, sql, values):
    with conn.cursor() as cursor:
          cursor.execute(sql,tuple(values))
          conn.commit()
          
          