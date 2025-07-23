import datetime
from data_display import data_show
from land_transactions import place_occupy, place_vacate, is_valid_kitta
from data_management import data_write

def transactions_manage(lands_data):
    """
    Manage land transactions including renting and returning lands, generating bills, and updating data.
    """
    while True:
        try:
            data_show(lands_data)
            choice = input(
                "\nEnter '1' to rent land(s), '2' to return land(s), or '0' to exit: ")
            if choice == '1':
                kitta_nos = input(
                    "Enter comma-separated kitta numbers to rent: ").split(',')
                months = int(input("Enter the duration of rental (in months): "))
                name = input("Enter client name: ")
                if is_valid_kitta(lands_data, [int(k) for k in kitta_nos]):
                    place_occupy(lands_data, [int(k)
                                 for k in kitta_nos], months, name)
                else:
                    print("Invalid kitta number(s) or land(s) already rented.")
            elif choice == '2':
                kitta_nos = input(
                    "Enter comma-separated kitta numbers to return: ").split(',')
                place_vacate(lands_data, [int(k) for k in kitta_nos])
            elif choice == '0':
                print("EXIT")
                break
            else:
                print("\nInvalid input. Please enter '1', '2', or '0'.")
        except Exception as e:
            print("An error occurred:", e)

    data_write("lands_data.txt", lands_data) 


