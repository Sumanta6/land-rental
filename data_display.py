def data_show(lands_data):
    """
    Display the available lands to the user.
    """
    print("\t |--------------------------------------|")
    print("\t |      TECHNO PROPERTY NEPAL           |")
    print("\t |--------------------------------------|")
    print("\nAVAILABLE LANDS:\n")
    for item in lands_data:
        if item['status'] == 'Available':
            print(f"Kitta No: {item['kitta_no']}\nPlace: {item['place']}\nDirection: {item['dir']}\nSize: {
                  item['size']} anna\nPrice: NPR {item['price']}\nStatus: {item['status']}\n------------------")