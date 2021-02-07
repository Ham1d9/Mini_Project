import csv
import os
import tabulate
import pyinputplus as pyip
from src.core_modules.core_persistence import save_order
from src.core_modules.core_courier import view_couriers
from src.core_modules.core_product import view_products

order_menu = """
Slecet a Number for your Chosen Option 
--------------------------------------
     Order Menu
--------------------------------------
[1]  Print the orders 
[2]  Create a new order 
[3]  Update a order status
[4]  Update a order 
[5]  Delete a order 
--------------------------------------
[0]  Return to Main Menu
"""
status_options = ["preparing", "delayed", "done"]


def view_orders(orders):
    os.system("clear")
    print(tabulate.tabulate(orders, headers="keys", tablefmt ="fancy_grid", showindex=True))

def update_status(orders,status_options):
    view_orders(orders)
    select_idx = pyip.inputNum("Select a order number: ", min = 0, max = len(orders))
    orders[select_idx]["status"] = pyip.inputMenu(status_options, numbered=True)
    os.system("clear")
    return orders

def create_orders(orders,couriers,products):
    os.system("clear")
    name = str(input("Name: "))
    address = str(input("Address: "))
    phone = str(input("phone: "))
    view_couriers(couriers)
    courier = pyip.inputNum("Select a courier number: ", min = 0, max = len(couriers))
    view_products(products)
    items = str(input("Select the items for order separate by comma: "))
    
    order_append = {
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone,
        "courier": courier,
        "status": "preparing",
        "items": [items]
    }

    orders.append(order_append)
    save_order(orders)
    os.system("clear")
    return orders


def update_orders(orders,couriers,products,status_options):
    os.system("clear")
    view_orders(orders)
    idx = pyip.inputNum("please select a order to update: ", min = 0, max =len(orders))

    for key in orders[idx].keys():
        
        if key == "courier":
            view_couriers(couriers)
            update = pyip.inputNum("select a courier no seprated by commas: ",blank=True, min=0, max=len(couriers))
            if update != "":
                orders[idx][key] = update

        elif key == "items":
            view_products(products)
            update = str(input("Select the items for the order separate by comma: "))
            if update != "":
                orders[idx][key] = [update]
        
        elif key == "status":
            view_orders(orders)
            status_prompt= "select one of the option to update status: "
            update = pyip.inputMenu(status_options,prompt=status_prompt, blank=True, numbered=True)
            if update != "":
                orders[idx][key] = update
                
        elif key == "customer_address" or "key == customer_name" or "customer_phone":
            update = input(f"write the new {key}: ")
            if update != "":
                orders[idx][key] = update
                
    save_order(orders)
    os.system("clear")
    return orders


def delete_orders(orders):
    view_orders(orders)
    idx = int(input("Select: "))
    orders.pop(idx)
    save_order(orders)
    os.system("clear")
    return orders


def order_sub_menu(order_data,couriers,products):
    
    while True:
        
        option = pyip.inputNum(order_menu, min = 0, max = 5)

        if option == 0:
            break

        elif option == 1:
            view_orders(order_data)

        elif option == 2:
            create_orders(order_data,couriers,products)
            
        elif option == 3:
            update_status(order_data,status_options)
            
        elif option == 4:
            update_orders(order_data,couriers,products,status_options)
           
        elif  option == 5:
            delete_orders(order_data)
         







