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
insert_new = "INSERT INTO courier (courier_name, courier_phone) VALUES ( %s, %s)"
update_new = "UPDATE courier SET courier_name = %s, courier_phone = %s WHERE ID = %s"
delete_courier = "DELETE from courier WHERE id = %s"

def fetch_couriers():
    couriers = []
    courier = query(conn, "select * from courier")
    for raw in courier:
        couriers.append({"courier_name":raw[1],"courier_phone":raw[2],"id":raw[0]})
    return couriers

def view_couriers(state):
    os.system("clear")
    print_courier = []
    for item in state["couriers"]:
        print_courier.append(dict(courier_name =item["courier_name"],courier_phone=item["courier_phone"]))
    print(tabulate.tabulate(print_courier, headers="keys", tablefmt ="fancy_grid", showindex=True))
    
    
def create_couriers(state):
    os.system("clear")
    name = str(input("courier_name: "))
    phone = str(input("phone number: "))

    courier_append = {
        "name": name,
        "phone": phone, 
        }
    try:
        add(conn, insert_new, tuple(courier_append.values()))
    except:
        print("there is problem appending")
    
    return state


def update_couriers(state):
    view_couriers(state)
    idx = pyip.inputNum("please select a courier to update: ", min = 0, max =len(state["couriers"])-1)

    for key in state["couriers"][idx].keys():
        if key ==  "courier_name":
            update = input(f"{key}: ")
            if update != "":
                state["couriers"][idx][key] = update
        elif key == "courier_phone":
            update = input(f"{key}: ")
            if update != "":
                state["couriers"][idx][key] = int(update)
                
    try:
        add(conn, update_new, tuple(state["couriers"][idx].values()))
        os.system("clear")   
    except: 
        print("something went wrong")            
    return state
    

def delete_couriers(state):
    view_couriers(state)
    idx = int(input("Select: "))
    x = state["couriers"][idx]["id"]
    add(conn, delete_courier, x)
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

