import os
import pyinputplus as pyip
from src.core_modules.core_persistence import save_courier

couriermenu = """

Slecet a Number for your Chosen Option 

[0]  Return to Main Menu
[1]  Print the courier 
[2]  Create a new courier 
[3]  Update a courier 
[4]  Delete a courier 

"""


def view_couriers(couriers):
    os.system("clear")
    idx = 0
    for courier in couriers:
        print(f"{[idx]} - {courier}")
        idx += 1

def create_couriers(couriers):
    name = str(input("name: "))
    phone = str(input("phone: "))


    courier_append = {
        "name": name,
        "phone": phone,
      
    }

    couriers.append(courier_append)
    save_courier(couriers)
    return couriers

def update_couriers(couriers):
    view_couriers(couriers)
    idx = int(input("Select: "))

    for key in couriers[idx].keys():
        update = input(f"{key}: ")
        if update != "":
                couriers[idx][key] = str(update)
            
    save_courier(couriers)
    return couriers

def delete_couriers(couriers):
    view_couriers(couriers)
    idx = int(input("Select: "))
    couriers.pop(idx)
    save_courier(couriers)
    return couriers


def courier_menu(courier_data):
    
    while True:
        
        option2 = pyip.inputNum(couriermenu, min = 0, max = 4)

        if option2 == 0:
            save_courier(courier_data)
            break

        elif option2 == 1:
            view_couriers(courier_data)

        elif option2 == 2:
            create_couriers(courier_data)
            
        elif option2 == 3:
            update_couriers(courier_data)
            
        elif  option2 == 4:
            delete_couriers(courier_data)

