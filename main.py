from data_management import data_read
from transactions_manage import transactions_manage

if __name__ == "__main__":
    lands_data = data_read("lands_data.txt")
    transactions_manage(lands_data)
