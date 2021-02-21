
import os
import pyinputplus as pyip
from src.core_modules.core_product import product_menu, fetch_products
from src.core_modules.core_orders import order_sub_menu, fetch_transaction
from src.core_modules.core_courier import courier_menu, fetch_couriers 
from src.core_modules.core_persistence import load_state


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
    
    while True:
        os.system("clear")
        option = pyip.inputInt(MainMenu, min = 0, max = 3 )
        
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
 
            
if __name__ == '__main__':
    start_app()
