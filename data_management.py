import os

def data_read(file_name):
    """
    Read data from a text file and return a list of dictionaries representing lands data.
    """
    lands_data = []
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write("101, Kathmandu, North, 4, 50000, Available\n102, Pokhara, East, 5, 60000, Not Available\n103, Lalitpur, South, 10, 100000, Available")
    with open(file_name, 'r') as f:
        for line in f:
            values = line.strip().split(', ')
            try:
                kitta_no = int(values[0])
                size = int(values[3])
            except ValueError:
                print("Error: Unable to convert values to integers:", values)
                continue
            data_dict = {'kitta_no': kitta_no, 'place': values[1], 'dir': values[2], 'size': size, 'price': int(values[4]), 'status': values[5]}
            lands_data.append(data_dict)
    return lands_data



def data_write(file_name, lands_data):
    """
    Write data to a text file based on the provided lands data.
    """
    with open(file_name, 'w') as f:
        for item in lands_data:
            f.write(f"{item['kitta_no']}, {item['place']}, {item['dir']}, {
                    item['size']}, {item['price']}, {item['status']}\n")
