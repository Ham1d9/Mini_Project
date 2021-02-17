import csv
import os
import tabulate
import pyinputplus as pyip
from src.core_modules.core_persistence import save_state
from src.core_modules.core_courier import view_couriers
from src.core_modules.core_product import view_products
from src.core_modules.core_db import query, add, conn

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
top_part_print =  """
---------------------------------------
        Order Information 
---------------------------------------

Order: {}, {}, {}
 
Order status: {}
 
Courier_Name: {} Phone: {}
"""
total = """  Total\t\t      £{}"""
status_options = ["preparing", "delayed", "done"]

sel_all_transaction = """select transaction.id,status,customer_name,customer_address,customer_phone, 
courier_name,courier_phone from transaction join courier on courier.id = transaction.courier_id;"""

sel_sql_basket= """select product_name,price from basket join product on product.id = basket.product_id 
        where transaction_id = %s """
        
add_transaction = """INSERT INTO transaction (status, customer_name, customer_address,
        customer_phone, courier_id) VALUES (%s, %s, %s, %s, %s)"""   
        
add_basket = "INSERT INTO basket (transaction_id, product_id) VALUES(%s, %s)"
         
def fetch_transaction():
    transaction = []
    transactions = query(conn,sel_all_transaction)
    for raw in transactions:
        transaction.append({"status":raw[1],"customer_name":raw[2],"customer_address":raw[3],"customer_phone":raw[4],"courier_name":raw[5],"courier_phone":raw[6],"id":raw[0]})
    return transaction

def view_orders(state):
    os.system("clear")
    print_orders = []
    for order in state["orders"]:
        print_orders.append(dict(status =order["status"],customer_name=order["customer_name"],customer_address=order["customer_address"],customer_phone=order["customer_phone"]))
    print(tabulate.tabulate(print_orders, headers="keys", tablefmt ="fancy_grid", showindex=True))
       

def update_status(state):
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
    courier = pyip.inputNum("Select a courier for the order: ", min = 0, max = len(state["couriers"])-1)
    values_trans = ("preparing", name,address,phone,state["couriers"][courier]["id"])
    add(conn,add_transaction,values_trans)
    state["orders"] = fetch_transaction()
    
    while True:
        view_products(state)
        ask = "select the product and press enter to add it \n or leave it blank to contine ,just press Enter to go back..... "
        update_value = pyip.inputNum(ask, min = 0, max = len(state["products"])-1, blank=True)
        if update_value == "":
            break
        else:
            print(state["orders"][len(state["orders"])-1]["id"])
            value_basket = (state["orders"][len(state["orders"])-1]["id"],state["products"][update_value]["id"])
            add(conn,add_basket,value_basket)
    
    # os.system("clear")
    return state


def update_orders(state):
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



def print_sub_menu(state):
    view_orders(state)
    
    while True:
        
        idx = pyip.inputNum("select a order to see more \n or press Enter to go back menu..... ",blank=True, min=0, max=len(state["orders"]))
        os.system("clear")
        
        if idx == "":
            os.system("clear")
            break
        
        else:
           
            parsed_data = []
            price_list = []
            raw_data = query(conn,sel_sql_basket, state["orders"][idx]["id"])
            
            for raw in raw_data:
                parsed_data.append({"product_name":raw[0],"price":raw[1]})
                price_list.append(raw[1])
                
            print(top_part_print.format(state["orders"][idx]["customer_name"],state["orders"][idx]["customer_address"],\
                state["orders"][idx]["customer_phone"],state["orders"][idx]["status"],state["orders"][idx]["courier_name"],\
                    state["orders"][idx]["courier_phone"]))
            print(tabulate.tabulate(parsed_data, headers="keys", tablefmt ="psql"))
            print(total.format(sum(price_list)))
            
            input("press any key to go back......")
            os.system("clear")
            break
        
def order_sub_menu(state):
    
    while True:
        state["orders"] = fetch_transaction()
        option = pyip.inputNum(order_menu, min = 0, max = 5)

        if option == 0:
            save_state(state)
            break

        elif option == 1:
            print_sub_menu(state)

        elif option == 2:
            create_orders(state)
            
        elif option == 3:
            update_status(state)
            
        elif option == 4:
            update_orders(state)
           
        elif  option == 5:
            delete_orders(state)
         







