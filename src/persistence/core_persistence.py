import csv 

def read_txt(file_name: str):
    
    with open(file_name, "r") as file:
        
        data = file.read().splitlines()   
    return data


def save_txt (datain: list, file):
    with open(file, "w") as opened_file:
        for row in datain: 
            opened_file.write(f"{row}\n")

  

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

def save(data):
    write_csv(data, "./data/orders.csv")