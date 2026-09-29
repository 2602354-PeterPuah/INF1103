inventory=0
total_tax=0

#output list of transaction history
def load_inventory():
    # Create the file if it does not exist
    with open("inventory.txt", "a") as file:
        pass

    # Read the file
    with open("inventory.txt", "r") as file:
        lines = file.readlines()

        if len(lines) == 0:
            return [], 1001

        transaction_history = lines[0:]
        last_order_id = int(transaction_history[-1][0:4])
        return transaction_history, last_order_id

def save_inventory(transaction_info):
    with open("inventory.txt", "a") as file:
        for item in transaction_info:
            file.write("\n" + str(item[0]) + ", " + item[1] + ", " + str(item[2]))
        print("Order successfully saved to inventory.txt.")

def get_valid_inputs(last_order_id):
    failed_entries = 0
    quantity = 0
    current_transaction = []

    while True:
        product_name = input("Enter Product Name (or quit): ")
        
        if product_name.lower() == "quit":
            return 1, current_transaction

        quantity = input("Enter Quantity: ")

        if not quantity.isdigit():
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            continue

        quantity = int(quantity)

        last_order_id += 1

        transaction = [last_order_id, product_name, quantity]
        current_transaction.append(transaction)


def generate_report(transaction):
    print("New orders added:")
    for item in transaction:
        print(str(item[0]) + ",", item[1] + ",", str(item[2]))

while True:
    inventory_history, last_order_id = load_inventory()
    for line in inventory_history:
        print(line.strip())
    
    quit_status, transaction_info = get_valid_inputs(last_order_id)

    if quit_status == 1:
        break

generate_report(transaction_info)
save_inventory(transaction_info)

