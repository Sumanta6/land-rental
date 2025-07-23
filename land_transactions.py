import datetime


def place_occupy(lands_data, kitta_nos, months, name):
    """
    Rent one or more lands and generate a bill for the rented lands.
    """
    bill = []
    total_cost = 0
    for kitta_no in kitta_nos:
        for item in lands_data:
            if item['kitta_no'] == kitta_no and item['status'] == 'Available':
                item['status'] = 'Not Available'
                item['duration'] = months
                cost = item['price'] * months
                total_cost += cost
                bill.append(
                    {'kitta_no': kitta_no, 'place': item['place'], 'direction': item['dir'], 'duration': months, 'cost': cost, 'client': name})
                break

    generate_bill(bill, total_cost, name)


def place_vacate(lands_data, kitta_nos):
    """
    Return one or more rented lands and generate a bill for the returned lands.
    """
    bill = []
    total_cost = 0
    for kitta_no in kitta_nos:
        for item in lands_data:
            if item['kitta_no'] == kitta_no and item['status'] == 'Not Available':
                item['status'] = 'Available'
                duration = item.get('duration', 0)
                cost = item['price'] * duration if duration > 0 else 0
                total_cost += cost
                fine = 0
                if duration > 0:
                    returned_date = datetime.datetime.now()
                    rented_date = returned_date - \
                        datetime.timedelta(days=30 * duration)
                    if returned_date > rented_date:
                        fine = int(
                            0.1 * (returned_date - rented_date).days * item['price'])
                        total_cost += fine
                bill.append(
                    {'kitta_no': kitta_no, 'place': item['place'], 'direction': item['dir'], 'duration': duration, 'cost': cost + fine})
                break

    generate_bill(bill, total_cost)


def generate_bill(bill_items, total_cost, client_name=None):
    """
    Generate a bill for the transaction.
    """
    bill_file_name = f"bill_{
        datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    VAT=total_cost*0.13
    Finalcost=VAT+total_cost
    with open(bill_file_name, 'w') as bill_file:
        if client_name:
            bill_file.write(f"Client Name: {client_name}\n\n")
        bill_file.write("BILL DETAILS\n\n")
        for item in bill_items:
            bill_file.write(f"Kitta No: {item['kitta_no']}\nPlace: {item['place']}\nDirection: {
                            item['direction']}\nDuration: {item['duration']} months\nCost: NPR {item['cost']}\n\n")
        bill_file.write(f"TOTAL COST: NPR {total_cost}"+"\n")
        bill_file.write(f"VAT: NPR {VAT}"+"\n")
        bill_file.write(f"FINALCOST: NPR {Finalcost}")


def is_valid_kitta(lands_data, kitta_nos):
    """
    Check if the entered kitta numbers are valid.
    """
    valid_kittas = [item['kitta_no']
                    for item in lands_data if item['status'] == 'Available']
    return all(kitta in valid_kittas for kitta in kitta_nos)
