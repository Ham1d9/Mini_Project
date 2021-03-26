import os
import tabulate
import pyinputplus as pyip
from src.core_modules.core_persistence import save_state
from src.core_modules.core_db import query, add

couriermenu = """
Select a Number for your chosen Option 
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

def fetch_couriers(conn):
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
    
    
def create_couriers(state,conn):
    os.system("clear")
    name = str(input("write courier name: "))
    
    while True:
            phone = pyip.inputStr("write phone: ")
            if len(phone)!= 11:
                print("wrong number of digits")
            elif len(phone)== 11:
                break

    try:
        add(conn, insert_new, (name, phone))
    except:
        print("there is problem appending")
    
    return state


def update_couriers(state,conn):
    view_couriers(state)
    idx = pyip.inputInt("please select a courier to update: ", min = 0, max =len(state["couriers"])-1)

    for key in state["couriers"][idx].keys():
        
        if key ==  "courier_name":
            update = input(f"write the new {key}\n or leave it blank to skip, just press Enter to continue.....")
            if update != "":
                state["couriers"][idx][key] = update
        
        elif key == "courier_phone":
            while True:
                update = pyip.inputStr(f"\nwrite the new {key}\n or leave it blank to skip, just press Enter to continue.....", blank=True)

                if update !="" and len(update)== 11:
                    state["couriers"][idx][key] = update
                    break
                
                elif update !="" and len(update)!= 11:
                    print("wrong number of digits")
                
                elif update =="":
                     break
                
    try:
        add(conn, update_new, tuple(state["couriers"][idx].values()))
        os.system("clear")   
    except: 
        print("something went wrong")            
    return state
    
def delete_couriers(state,conn):
    view_couriers(state)
    idx = pyip.inputInt("please select a courier to delete: ", min = 0, max =len(state["couriers"])-1,blank=True)
    if idx !="":
        add(conn, delete_courier, state["couriers"][idx]["id"])
    os.system("clear")
    return state


def courier_menu(state,conn):
    
    while True:
        state["couriers"] = fetch_couriers(conn)
        option2 = pyip.inputInt(couriermenu, min = 0, max = 4)

        if option2 == 0:
            save_state(state)
            break

        elif option2 == 1:
            view_couriers(state)

        elif option2 == 2:
            create_couriers(state,conn)
            
        elif option2 == 3:
            update_couriers(state,conn)
            
        elif  option2 == 4:
            delete_couriers(state,conn)

