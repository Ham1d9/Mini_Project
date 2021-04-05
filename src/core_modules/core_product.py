import pyinputplus as pyip
import os
import tabulate
from src.core_modules.core_persistence import save_state, load_state
from src.core_modules import core_db as db
# import query, add


productmenu = """
Select a Number for your chosen Option 
--------------------------------------
     Product Menu
--------------------------------------
[1]  Print the products 
[2]  Create a new Products 
[3]  Update a Product 
[4]  Delete a Product 
--------------------------------------
[0]  Return to Main Menu
"""

sel_all_products = "select * from product"
insert_new = "INSERT INTO product (product_name,quantity, price) VALUES ( %s, %s,%s)"
update_new = "UPDATE product SET product_name = %s, quantity= %s, price = %s WHERE ID = %s"
delete_product = "DELETE from product WHERE id = %s"

def fetch_products(conn):
    products = []
    product = db.query(conn,sel_all_products)
    print(product)
    for raw in product:
        products.append({"product_name":raw[1],"quantity":raw[2],"price":raw[3], "id":raw[0]})
    return products
    
def view_products(state):
    os.system("clear")
    print_products = []
    for item in state["products"]:
        print_products.append(dict(product_name =item["product_name"],quantity= item["quantity"],price=item["price"]))
    print(tabulate.tabulate(print_products, headers="keys", tablefmt ="fancy_grid", showindex=True))
    return state 
    
def create_products(state,conn):
    os.system("clear")
    
    name = pyip.inputStr("Enter the product: ")
    price = pyip.inputFloat("Enter the new price: ")
    
    quantity = pyip.inputInt("please select quantity: ", min = 1)
    product_values = (name, quantity, price)
    try: 
        add(conn, insert_new, product_values)
        os.system("clear")
    except:
        print("there is a problem with creating new product")  
    return state


def update_products(state,conn):
    view_products(state)
    idx = pyip.inputNum("please select a product to update: ", min = 0, max =len(state["products"])-1)

    for key in state["products"][idx].keys():
        
        if key ==  "price":
            update = pyip.inputFloat(f"\nwrite the new {key}\n or leave it blank to skip, just press Enter to continue..... ",blank=True, min=0.1)
            if update != "":
                state["products"][idx][key] = float(update)
        elif key == "quantity":
            update = pyip.inputInt(f"\nwrite the new {key}\n or leave it blank to skip, just press Enter to continue..... ",blank=True, min=1)
            if update != "":
                state["products"][idx][key] = int(update)
        elif key == "product_name":
            update = input(f"\nwrite the new {key}\n or leave it blank to skip, just press Enter to continue..... ")
            if update != "":
                state["products"][idx][key] = update
    try:
        add(conn, update_new, tuple(state["products"][idx].values()))
        os.system("clear")   
    except: 
        print("something went wrong")            
    return state


def delete_products(state,conn):
    view_products(state)
    idx = pyip.inputNum("please select a product to delete: ", min = 0, max =len(state["products"])-1, blank=True)
    if idx !="":
        add(conn, delete_product, state["products"][idx]["id"])
    os.system("clear")
    return state


def product_menu(state,conn):
    
    while True:
        
        state["products"] = fetch_products(conn)
        option2 = pyip.inputNum(productmenu, min = 0, max = 4)

        if option2 == 0:
            save_state(state)
            break

        elif option2 == 1:
            view_products(state)

        elif option2 == 2:
            create_products(state,conn)
            
        elif option2 == 3:
            update_products(state,conn)
            
        elif  option2 == 4:
            delete_products(state,conn)



