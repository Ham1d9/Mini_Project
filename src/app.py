
import os
import pyinputplus as pyip
from src.core_modules.core_product import product_menu, fetch_products
from src.core_modules.core_orders import order_sub_menu, fetch_transaction
from src.core_modules.core_courier import courier_menu, fetch_couriers 
from src.core_modules.core_persistence import load_state
from src.core_modules import core_db as db

state  = load_state(fetch_couriers,fetch_products,fetch_transaction)



MainMenu = """

Select a Number foryour chosen Option 
--------------------------------------
    Main Menu 
--------------------------------------
  
[1] Product Menu
[2] Courier Menu
[3] Order Menu

--------------------------------------
[0] Exit App

"""
def start_app():
    
    conn = db.connection()
    
    while True:
        os.system("clear")
        option = pyip.inputInt(MainMenu, min = 0, max = 3 )
        
        if option == 0:
            os.system("clear")
            print("good bye")
            break
        
        elif option == 1:
            os.system("clear")
            
            product_menu(state,conn)
        
        elif option == 2:
            os.system("clear")
            
            courier_menu(state,conn)
        
        elif option == 3:
            os.system("clear")
            
            order_sub_menu(state,conn)
 
            
if __name__ == '__main__':
    start_app()
