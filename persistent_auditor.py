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
            return []

        transaction_history = lines[0:]

        return transaction_history


def get_valid_inputs():
    failed_entries = 0
    while True:
        product_name = input("Enter Product Name (or quit): ")
        
        if product_name.lower() == "quit":
            return "quit", failed_entries

        quantity = input("Enter Quantity: ")

        if not quantity.isdigit():
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            continue

        quantity = int(quantity)

        transaction_history = []
        transaction = [product_name, quantity]
        transaction_history.append(str(transaction) + "\n")

        return transaction_history, failed_entries


def generate_report(name, quantity):
    print("New orders added: \n")

while True:
    inventory_history = load_inventory()
    for line in inventory_history:
        print(line.strip(   )) 
    product, failed_entries = get_valid_inputs()


