import csv
# for dic use below ones 

def read_csv(filename):
    data = []
    with open(filename) as the_file:
        reader = csv.DictReader(the_file)
        for line in reader:
            data.append(line)
    return data
    
def write_csv(data: list, filename):
    with open(filename, mode="w", newline="\n") as sf:
        writer = csv.DictWriter(sf, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
 
def save_state(data):
    write_csv(data["couriers"], "./data/courier.csv" )
    write_csv(data["products"], "./data/products.csv")
    write_csv(data["orders"], "./data/orders.csv")
    
def load_state(fetch_couriers,fetch_products,fetch_transaction,conn):
    state = {}
    state["products"] = fetch_products(conn)
    state["couriers"] = fetch_couriers(conn)
    state["orders"] = fetch_transaction(conn)
    return state 

