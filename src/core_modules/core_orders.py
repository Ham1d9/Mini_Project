import csv
from src.core_modules.core_persistence import save_order
import pyinputplus as pyip
import os


order_menu = """

[0]  Return to Main Menu
[1]  Print the orders 
[2]  Create a new order 
[3]  Update a order 
[4]  Delete a order 

"""


def view_orders(orders):
    os.system("clear")
    idx = 0
    for order in orders:
        # print(f"""{idx} - Customer Name: {order['customer_name']}, Customer Address: {order['customer_address']}
        #     Customer Phone: {order['customer_phone']}, Courier: {order['courier']}, Status: {order['status']}""")
        print(f"{[idx]} - {order}")
        idx += 1



def create_orders(orders,input,save_order):
    name = str(input("Name: "))
    address = str(input("Address: "))
    phone = int(input("phone: "))
    courier = int(input("courier: "))
    status = str(input("status: "))

    order_append = {
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone,
        "courier": courier,
        "status": status
    }

    orders.append(order_append)
    save_order(orders)
    return orders


def update_orders(orders):
    view_orders(orders)
    idx = int(input("Select: "))

    for key in orders[idx].keys():
        update = input(f"{key}: ")
        if update != "":
            if key == "customer_phone" or key == "courier":
                orders[idx][key] = int(update)
            else:
                orders[idx][key] = update

    save_order(orders)
    return orders


def delete_orders(orders,view_orders,input,save_order):
    view_orders(orders)
    idx = int(input("Select: "))
    orders.pop(idx)
    save_order(orders)
    return orders


def order_sub_menu(order_data):
    
    while True:
        
        option = pyip.inputNum(order_menu, min = 0, max = 4)

        if option == 0:
            break

        elif option == 1:
            view_orders(order_data)

        elif option == 2:
            create_orders(order_data)
            
        elif option == 3:
            update_orders(order_data)
            
        elif  option == 4:
            delete_orders(order_data)







