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

def add(conn, sql, values):
    with conn.cursor() as cursor:
          cursor.execute(sql,values)
          conn.commit()
          
          

# def update(conn,sql,vlaues

def load_state(conn,fetch_couriers,fetch_products):
    state = {}
    state["products"] = fetch_products(conn)
    state["couriers"] = fetch_couriers(conn)
    state["orders"] = read_csv('./data/orders.csv')
    return state 
