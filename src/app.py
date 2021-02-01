import csv 
import pyinputplus as pyip
from src.core_modules.core_product import product_menu
from src.core_modules.core_orders import order_sub_menu
from src.core_modules.core_courier import courier_menu
from src.core_modules.core_persistence import read_txt,read_csv

products = read_csv('./data/products.csv')
courier = read_txt('./data/courier.txt')
orders = read_csv('./data/orders.csv')


MainMenu = """
Slecet a Number for your Chosen Option 

[0] Exit App
[1] Product Menu
[2] Courier Menu
[3] Order Menu
"""

while True:
    option = pyip.inputNum(MainMenu, min = 0, max = 3 )
    
    if option == 0:
        break
    
    elif option == 1:
        product_menu(products)
    
    elif option == 2:
        courier_menu(courier)
    
    elif option == 3:
        order_sub_menu(orders)
        
        