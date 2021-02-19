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
-----------------------------------------
        Order Information 
-----------------------------------------

Order: {}, {}, {}
 
Order status: {}
 
Courier_Name: {} Phone: {}
"""
basket_item_update= """
[0] go back to products list 
[1] change the item 
[2] change the quantity
[3] delete the product from the order
"""
total = """  Total\t\t\t\t   £{}"""
status_options = ["preparing",  "ready", "delayed", "out for delivery", "delivered"]

sel_all_transaction = """select transaction.id,status,customer_name,customer_address,customer_phone, 
courier_name,courier_phone,courier_id from transaction join courier on courier.id = transaction.courier_id;"""

sel_sql_basket= """select product_name,price,basket.quantity from basket join product on product.id = basket.product_id 
        where transaction_id = %s """
        
sel_sql_basket_with_id = """select basket.id,product_name,basket.quantity,price,product_id from basket join product on product.id = basket.product_id 
        where transaction_id = %s """
             
add_transaction = """INSERT INTO transaction (status, customer_name, customer_address,
        customer_phone, courier_id) VALUES (%s, %s, %s, %s, %s)"""   
        
add_basket = "INSERT INTO basket (transaction_id, product_id, quantity) VALUES(%s, %s, %s)"

update_status_sql = "UPDATE transaction SET status = %s WHERE ID = %s"      

update_transaction = "UPDATE transaction SET status=%s, customer_name=%s, customer_address=%s, customer_phone=%s, courier_id=%s WHERE ID = %s"

update_basket_product = "UPDATE basket set product_id= %s where transaction_id = %s and id =%s"
update_basket_quantity = "UPDATE basket set quantity = %s where transaction_id = %s and id =%s"

delete_basket_product = "DELETE FROM basket WHERE id = %s"
delte_transaction = "DELETE FROM transaction WHERE id =%s" 

def fetch_transaction():
    transaction = []
    transactions = query(conn,sel_all_transaction)
    for raw in transactions:
        transaction.append({"status":raw[1],"customer_name":raw[2],"customer_address":raw[3],"customer_phone":raw[4],"courier_name":raw[5],"courier_phone":raw[6],"courier_id":raw[7],"id":raw[0]})
    return transaction

def view_orders(state):
    os.system("clear")
    print_orders = []
    for order in state["orders"]:
        print_orders.append(dict(status=order["status"],customer_name=order["customer_name"],customer_address=order["customer_address"],customer_phone=order["customer_phone"]))
    print(tabulate.tabulate(print_orders, headers="keys", tablefmt ="fancy_grid", showindex=True))
       

def create_orders(state):
    os.system("clear")
    name = str(input("Name: "))
    address = str(input("Address: "))
    while True:
        phone = str(input("phone: ")))
        if len(phone)!= 11:
            print("wrong number of digits")
        elif len(phone)== 11:
            break
    view_couriers(state)
    courier = pyip.inputNum("Select a courier for the order: ", min = 0, max = len(state["couriers"])-1)
    values_trans = ("preparing", name,address,phone,state["couriers"][courier]["id"])
    add(conn,add_transaction,values_trans)
    state["orders"] = fetch_transaction()
    
    while True:
        view_products(state)
        ask = "select the product and press enter to add it \n or leave it blank to contine ,just press Enter to go back.....  "
        update_value = pyip.inputNum(ask, min = 0, max = len(state["products"])-1, blank=True)
        if update_value == "":
            break
        else:
            quantity_value = pyip.inputNum("\nselect a quantity: ", min = 1)
            value_basket = (state["orders"][len(state["orders"])-1]["id"],state["products"][update_value]["id"],quantity_value)
            add(conn,add_basket,value_basket)
    
    os.system("clear")
    return state

def update_status(state):
    view_orders(state)
    select_idx = pyip.inputNum("Select a order: ", min = 0, max = len(state["orders"])-1)
    new_status = pyip.inputMenu(status_options,"select a status to update:\n", numbered=True)
    add(conn,update_status_sql,(new_status,state["orders"][select_idx]["id"]))
    os.system("clear")
    return state

def update_orders(state):
    os.system("clear")
    view_orders(state)
    idx = pyip.inputNum("please select a order to update: ", min = 0, max =len(state["orders"])-1)
    del state["orders"][idx]["courier_name"],state["orders"][idx]["courier_phone"]
    
    for key in state["orders"][idx].keys():
        
        if key == "courier_id":
            view_couriers(state)
            update = pyip.inputNum("\nselect a new courier\n or leave it blank to skip,just press Enter to continue.... : ",blank=True, min=0, max=len(state["couriers"])-1)
            if update != "":
                state["orders"][idx][key] = state["couriers"][update]["id"]
               
        elif key == "status":
            view_orders(state)
            status_prompt= "select one of the option to update status.\n or leave it blank to skip,just press Enter to continue.....\n"
            update = pyip.inputMenu(status_options,prompt=status_prompt, blank=True, numbered=True)
            if update != "":
                state["orders"][idx][key] = update
            
        elif key == "customer_address" or key == "customer_name" or key == "customer_phone":
            update = input(f"\nwrite the new {key}\n or leave it blank to skip, just press Enter to continue..... ")
            if update != "":
                state["orders"][idx][key] = update

        add(conn,update_transaction,tuple(state["orders"][idx].values()))
# --------------------------------------------------- 
 
    def refresh():
        basket_data = []
        raw_data = query(conn,sel_sql_basket_with_id, state["orders"][idx]["id"])    
        for raw in raw_data:
            basket_data.append({"id":raw[0],"product_name":raw[1],"quantity":raw[2],"price":raw[3],"product_id":raw[4]})
        return basket_data
    
    basket_data = refresh()
    
    def basket_print(basket_data):
        basket_print = []
        for dic in basket_data:  
            basket_print.append(dict(product_name=dic["product_name"],quantity=dic["quantity"],price=dic["price"]))
        print(tabulate.tabulate(basket_print, headers="keys", tablefmt ="fancy_grid", showindex=True))
        
    def basket_print_idx(basket_data,idx_basket):
        basket_print = []
        for dic in basket_data:  
            basket_print.append(dict(product_name=dic["product_name"],quantity=dic["quantity"],price=dic["price"]))
        print(tabulate.tabulate([basket_print[idx_basket]], headers="keys", tablefmt ="fancy_grid"))

    while True:
        os.system("clear")
        basket_data = refresh()
        basket_print(basket_data)
        idx_basket = pyip.inputNum("please select a product to update\n or leave it blank to skip ,just press Enter to continue.....  ",blank=True, min = 0, max =len(basket_data)-1)
        
        if idx_basket == "":
            break
        
        else:
            os.system("clear")
            basket_print_idx(basket_data,idx_basket)
            option_update =  pyip.inputNum(basket_item_update, min = 0, max =3)
            
            if option_update == 0:
                pass
            elif option_update == 1:
                view_products(state)
                ask_new_product = "select a new product: "
                update_product_idx = pyip.inputNum(ask_new_product, min = 0, max = len(state["products"])-1, blank=True)
                update_product_value = (state["products"][update_product_idx]["id"],state["orders"][idx]["id"],basket_data[idx_basket]["id"])
                add(conn,update_basket_product,update_product_value)
               
            elif option_update == 2:
                ask_new_quantity = pyip.inputNum("select a new quantity: ", min = 0)
                update_quantity_value = (ask_new_quantity,state["orders"][idx]["id"],basket_data[idx_basket]["id"])
                add(conn,update_basket_quantity,update_quantity_value)
            
            elif option_update == 3:
                add(conn,delete_basket_product,basket_data[idx_basket]["id"])
    os.system("clear")                
    return state


def delete_orders(state):
    view_orders(state)
    idx = pyip.inputNum("please select a order to delete\n or leave it blank to skip, press Enter to go back...",blank=True, min = 0, max =len(state["orders"])-1)
    if idx !="":
        add(conn, delte_transaction,state["orders"][idx]["id"])
    os.system("clear")
    return state



def print_sub_menu(state):
    
    while True:
        view_orders(state)
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
                parsed_data.append({"product_name":raw[0],"quantity":raw[2],"price":raw[1]})
                price_list.append(raw[1]*raw[2])
                
            print(top_part_print.format(state["orders"][idx]["customer_name"],state["orders"][idx]["customer_address"],\
                state["orders"][idx]["customer_phone"],state["orders"][idx]["status"],state["orders"][idx]["courier_name"],\
                    state["orders"][idx]["courier_phone"]))
            print(tabulate.tabulate(parsed_data, headers="keys", tablefmt ="psql"))
            print(total.format(sum(price_list)))
            
            input("\npress any key to go back......")
            os.system("clear")
            
        
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
         







