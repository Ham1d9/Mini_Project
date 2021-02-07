import pyinputplus as pyip
import os
import tabulate
from src.core_modules.core_persistence import save_product


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

def view_products(products):
    os.system("clear")
    print(tabulate.tabulate(products, headers="keys", tablefmt ="fancy_grid", showindex=True))
    
def create_products(products):
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

    products.append(product_append)
    save_product(products)
    return products

def update_products(products):
    view_products(products)
    idx = pyip.inputNum("please select a product to update: ", min = 0, max =len(products))

    for key in products[idx].keys():
        update = input(f"{key}: ")
        if update != "":
            if key ==  "price":
                products[idx][key] = float(update)
            else:
                products[idx][key] = update

    save_product(products)
    return products

def delete_products(products):
    view_products(products)
    idx = int(input("Select: "))
    products.pop(idx)
    save_product(products)
    
    return products


def product_menu(products_data):
    
    while True:
        
        option2 = pyip.inputNum(productmenu, min = 0, max = 4)

        if option2 == 0:
            break

        elif option2 == 1:
            view_products(products_data)

        elif option2 == 2:
            create_products(products_data)
            
        elif option2 == 3:
            update_products(products_data)
            
        elif  option2 == 4:
            delete_products(products_data)



