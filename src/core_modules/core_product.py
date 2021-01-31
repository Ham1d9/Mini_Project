import pyinputplus as pyip
from src.core_modules.core_persistence import save_product


productmenu = """

Slecet a Number for your Chosen Option 

[0]  Return to Main Menu
[1]  Print the products 
[2]  Create a new Products 
[3]  Update a Product 
[4]  Delete a Product 

"""
def new_product(products_data):
    newproduct = str(input('write name of new product: '))            
    products_data.append(newproduct)

    return products_data

def update_product(products_data):
    selectedproduct = pyip.inputMenu(products_data, numbered=True)
    updateproduct = str(input('Wrtite the new product: '))
            
    for n, i in enumerate(products_data):
        if i == selectedproduct:
            products_data[n]= updateproduct
            return products_data
        
def remove_product(products_data):
    remove_product = pyip.inputMenu(products_data, numbered=True)
    print('the product is removed')
    products_data.remove(remove_product)
    return products_data


def product_menu(products_data):
    
    while True:
        
        option2 = pyip.inputNum(productmenu, min = 0, max = 4)

        if option2 == 0:
            save_product(products_data)
            break

        elif option2 == 1:
            print(products_data)

        elif option2 == 2:
            new_product(products_data)
            
        elif option2 == 3:
            update_product(products_data)
            
        elif  option2 == 4:
            remove_product(products_data)





    
