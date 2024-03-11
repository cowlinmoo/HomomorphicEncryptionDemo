def write_data(file_name, data):
    with open(file_name, "wb") as file: 
        file.write(data) 

def read_data(file_name):
    with open(file_name, "rb") as file: 
        data = file.read()
        return data