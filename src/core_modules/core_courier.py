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
def new_courier(courier_data):
    newcourier = str(input('write name of new courier: '))            
    courier_data.append(newcourier)

    return courier_data

def update_courier(courier_data):
    selectedcourier = pyip.inputMenu(courier_data, numbered=True)
    updatecourier = str(input('Wrtite the new courier: '))
            
    for n, i in enumerate(courier_data):
        if i == selectedcourier:
            courier_data[n]= updatecourier
            return courier_data
        
def remove_courier(courier_data):
    remove_courier = pyip.inputMenu(courier_data, numbered=True)
    print('the courier is removed')
    courier_data.remove(remove_courier)
    return courier_data


def courier_menu(courier_data):
    
    while True:
        
        option2 = pyip.inputNum(couriermenu, min = 0, max = 4)

        if option2 == 0:
            save_courier(courier_data)
            break

        elif option2 == 1:
            print(courier_data)

        elif option2 == 2:
            new_courier(courier_data)
            
        elif option2 == 3:
            update_courier(courier_data)
            
        elif  option2 == 4:
            remove_courier(courier_data)

