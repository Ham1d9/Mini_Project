import os
import pymysql.cursors
from dotenv import load_dotenv
from src.core_modules.core_persistence import read_csv

load_dotenv()

HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DB = os.environ.get("DB")
PORT = int(os.environ.get("PORT"))


def connection():
    return pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, port=PORT)
conn = connection()


def query(conn, sql, values=None):
    with conn.cursor() as cursor:
        cursor.execute(sql,values)
        result = cursor.fetchall()
        return result

def add(conn, sql, values):
    with conn.cursor() as cursor:
          cursor.execute(sql,values)
          conn.commit()







