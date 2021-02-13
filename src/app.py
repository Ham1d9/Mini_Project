import csv 
import os
import pyinputplus as pyip
from src.core_modules.core_product import product_menu, fetch_products
from src.core_modules.core_orders import order_sub_menu
from src.core_modules.core_courier import courier_menu, fetch_couriers 
from src.core_modules.core_persistence import load_state
from src.core_modules.core_db import connection

conn = connection()

state  = load_state(conn,fetch_couriers,fetch_products)
# state = load_state()


MainMenu = """

Slecet a Number foryour Chosen Option 
--------------------------------------
    Main Menu 
--------------------------------------
  
[1] Product Menu
[2] Courier Menu
[3] Order Menu

--------------------------------------
[0] Exit App

"""

while True:
    os.system("clear")
    option = pyip.inputNum(MainMenu, min = 0, max = 3 )
    
    if option == 0:
        os.system("clear")
        break
    
    elif option == 1:
        os.system("clear")
        product_menu(state)
    
    elif option == 2:
        os.system("clear")
        courier_menu(state)
    
    elif option == 3:
        os.system("clear")
        order_sub_menu(state)
        
        