import pyinputplus as pyip
import os
import tabulate
from src.core_modules.core_persistence import save_state
from src.core_modules.db import query, update


productmenu = """
Slecet a Number for your Chosen Option 
--------------------------------------
     Product Menu
--------------------------------------
[1]  Print the products 
[2]  Create a new Products 
[3]  Update a Product 
[4]  Delete a Product 
---------------------------------------
[0]  Return to Main Menu
"""

sel_all_products = "select * from product"
insert_new = "INSERT INTO product (name, price) VALUES ( %s, %s)"

def parse_product(raw):
    return{"id":raw[0],"name":raw[1],"price":raw[2]}


def fetch_products(conn):
    products = query(conn,sel_all_products)
    return [parse_product(p) for p in products]
    

def view_products(state):
    os.system("clear")
    print(tabulate.tabulate(state["products"], headers="keys", tablefmt ="fancy_grid", showindex=True))
    
    
def create_products(state,conn):
    os.system("clear")
    name = str(input("name: "))
    while True:
        try: 
            price = float(input("price: "))
            break
        except ValueError:
            print("Only numbers are allowed")

    product_append = {
        "name": name,
        "price": price,
      
    }
    try: 
        update(conn, insert_new, product_append.values())
        state["products"].append(product_append)
    except: 
        os.system("clear")
        print("there is a problem with creating new product")
    
    return state

def update_products(state):
    view_products(state)
    idx = pyip.inputNum("please select a product to update: ", min = 0, max =len(state["products"]))

    for key in state["products"][idx].keys():
        update = input(f"{key}: ")
        if update != "":
            if key ==  "price":
                state["products"][idx][key] = float(update)
            else:
                state["products"][idx][key] = update
                
    os.system("clear")            
    return state

def delete_products(state):
    view_products(state)
    idx = int(input("Select: "))
    state["products"].pop(idx)
    os.system("clear")
    return state


def product_menu(state,conn):
    
    while True:
        
        option2 = pyip.inputNum(productmenu, min = 0, max = 4)

        if option2 == 0:
            save_state(state)
            break

        elif option2 == 1:
            view_products(state)

        elif option2 == 2:
            create_products(state,conn)
            
        elif option2 == 3:
            update_products(state)
            
        elif  option2 == 4:
            delete_products(state)


