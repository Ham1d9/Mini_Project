import os
import tabulate
import pyinputplus as pyip
from src.core_modules.core_persistence import save_state
from src.core_modules.core_db import query, add, conn

couriermenu = """
Slecet a Number for your Chosen Option 
--------------------------------------
     Courier Menu
--------------------------------------
[1]  Print the courier 
[2]  Create a new courier 
[3]  Update a courier 
[4]  Delete a courier 
--------------------------------------
[0]  Return to Main Menu
"""

sel_all_courier = "select * from courier"
insert_new = "INSERT INTO courier (name, phone_number) VALUES ( %s, %s)"


def fetch_couriers():
    couriers = []
    courier = query(conn, "select * from courier")
    for raw in courier:
        couriers.append({"id":raw[0],"name":raw[1],"phone":raw[2]})
    return couriers

    
    

def view_couriers(state):
    os.system("clear")
    print(tabulate.tabulate(state["couriers"], headers="keys", tablefmt ="fancy_grid", showindex=True))
    
    
def create_couriers(state):
    os.system("clear")
    name = str(input("name: "))
    phone = str(input("phone: "))

    courier_append = {
        "name": name,
        "phone": phone, 
        }
    
    try:
        add(conn, insert_new, courier_append.values())
        state["couriers"].append(courier_append)
    except:
        
        print("there is problem appending")
    
    return state


def update_couriers(state):
    view_couriers(state)
    idx = pyip.inputNum("please select a courier to update: ", min = 0, max =len(state["couriers"]))

    for key in state["couriers"][idx].keys():
        update = input(f"{key}: ")
        if update != "":
                state["couriers"][idx][key] = update
            
    os.system("clear")
    return state

def delete_couriers(state):
    view_couriers(state)
    idx = int(input("Select: "))
    state["couriers"].pop(idx)
    
    os.system("clear")
    return state


def courier_menu(state):
    
    while True:
        state["couriers"] = fetch_couriers()
        option2 = pyip.inputNum(couriermenu, min = 0, max = 4)

        if option2 == 0:
            save_state(state)
            break

        elif option2 == 1:
            view_couriers(state)

        elif option2 == 2:
            create_couriers(state)
            
        elif option2 == 3:
            update_couriers(state)
            
        elif  option2 == 4:
            delete_couriers(state)

