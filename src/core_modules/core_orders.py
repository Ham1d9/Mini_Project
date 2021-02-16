import csv
import os
import tabulate
import pyinputplus as pyip
from src.core_modules.core_persistence import save_state
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

sel_all_transaction = "select * from transaction"

def fetch_transaction():
    transaction = []
    transactions = query(conn,sel_all_products)
    for raw in transactions:
        transaction.append({"status":raw[1],"customer_name":raw[2],"customer_address":raw[3],"customer_phone":raw[4],"courier_id":raw[5], "id":raw[0]})
    return transaction


def view_products(state):
    os.system("clear")
    print_products = []
    for item in state["products"]:
        print_products.append(dict(name =item["name"],quantity= item["quantity"],price=item["price"]))
    print(tabulate.tabulate(print_products, headers="keys", tablefmt ="fancy_grid", showindex=True))

def view_orders(state):
    os.system("clear")
    print_orders = []
    for item in state["order"]:
        print(tabulate.tabulate(state["orders"], headers="keys", tablefmt ="fancy_grid", showindex=True))
       

def update_status(state,status_options):
    view_orders(state)
    select_idx = pyip.inputNum("Select a order number: ", min = 0, max = len(state["orders"]))
    state["orders"][select_idx]["status"] = pyip.inputMenu(status_options, numbered=True)
    os.system("clear")
    return state

def create_orders(state):
    os.system("clear")
    name = str(input("Name: "))
    address = str(input("Address: "))
    phone = str(input("phone: "))
    view_couriers(state)
    courier = pyip.inputNum("Select a courier number: ", min = 0, max = len(state["couriers"]))
    view_products(state)
    items = str(input("Select the items for order separate by comma: "))
    
    order_append = {
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone,
        "courier": courier,
        "status": "preparing",
        "items": [items]
    }

    state["orders"].append(order_append)
    
    os.system("clear")
    return state


def update_orders(state,status_options):
    os.system("clear")
    view_orders(state)
    idx = pyip.inputNum("please select a order to update: ", min = 0, max =len(state["orders"]))

    for key in state["orders"][idx].keys():
        
        if key == "courier":
            view_couriers(state)
            update = pyip.inputNum("select a courier no seprated by commas: ",blank=True, min=0, max=len(state["couriers"]))
            if update != "":
                state["orders"][idx][key] = update

        elif key == "items":
            view_products(state)
            update = str(input("Select the items for the order separate by comma: "))
            if update != "":
                state["orders"][idx][key] = [update]
        
        elif key == "status":
            view_orders(state)
            status_prompt= "select one of the option to update status: "
            update = pyip.inputMenu(status_options,prompt=status_prompt, blank=True, numbered=True)
            if update != "":
                state["orders"][idx][key] = update
                
        elif key == "customer_address" or "key == customer_name" or "customer_phone":
            update = input(f"write the new {key}: ")
            if update != "":
                state["orders"][idx][key] = update
                
    os.system("clear")
    return state


def delete_orders(state):
    view_orders(state)
    idx = int(input("Select: "))
    state["orders"].pop(idx)
    os.system("clear")
    return state


def order_sub_menu(state):
    
    while True:
        
        option = pyip.inputNum(order_menu, min = 0, max = 5)

        if option == 0:
            save_state(state)
            break

        elif option == 1:
            view_orders(state)

        elif option == 2:
            create_orders(state)
            
        elif option == 3:
            update_status(state,status_options)
            
        elif option == 4:
            update_orders(state,status_options)
           
        elif  option == 5:
            delete_orders(state)
         







