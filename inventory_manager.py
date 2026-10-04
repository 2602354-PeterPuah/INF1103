import json

inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": 1200.00, "Stock": 15},
    {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stock": 40}
]

def get_menu_selection():
    print("----------- MENU ----------")
    print("1. Display All Product")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------\n")

    menu_user_input = int(input("Enter option: "))
    return menu_user_input

def load_inventory():
    with open("inventory.json", "r") as file:
        inventory = json.load(file)
    
    for product in inventory:
        print(f"ID: {product['ID']} | Name: {product['Name']} | Price: ${product['Price']:.2f} | Stock: {product['Stock']}")

def add_product():
    return 1

def update_stock():
    return 2

def search_product():
    return 3
    
def display_all():
    return 4

#output list of transaction history
# def load_inventory():
#     # Create the file if it does not exist
#     with open("inventory.txt", "a") as file:
#         pass

#     # Read the file
#     with open("inventory.txt", "r") as file:
#         lines = file.readlines()

#         if len(lines) == 0:
#             return [], 1001

#         transaction_history = lines[0:]
#         last_order_id = int(transaction_history[-1][0:4])
#         return transaction_history, last_order_id

# def save_inventory(transaction_info):
#     with open("inventory.txt", "a") as file:
#         for item in transaction_info:
#             file.write("\n" + str(item[0]) + ", " + item[1] + ", " + str(item[2]))
#         print("Order successfully saved to inventory.txt.")

# def get_valid_inputs(last_order_id):
#     failed_entries = 0
#     quantity = 0
#     current_transaction = []

#     while True:
#         product_name = input("Enter Product Name (or quit): ")
        
#         if product_name.lower() == "quit":
#             return 1, current_transaction

#         quantity = input("Enter Quantity: ")

#         if not quantity.isdigit():
#             print("Invalid input. Please enter a non-negative integer.")
#             failed_entries += 1
#             continue

#         quantity = int(quantity)

#         last_order_id += 1

#         transaction = [last_order_id, product_name, quantity]
#         current_transaction.append(transaction)


# def generate_report(transaction):
#     print("New orders added:")
#     for item in transaction:
#         print(str(item[0]) + ",", item[1] + ",", str(item[2]))

while True:
    print("========================================\n")
    print("INVENTORY MANAGEMENT SYSTEM\n")
    print("========================================\n")

    menu_user_input = get_menu_selection()

    if menu_user_input == 1:
        load_inventory()
        break

    break

    # inventory_history, last_order_id = load_inventory()
    # for line in inventory_history:
    #     print(line.strip())
    
    # quit_status, transaction_info = get_valid_inputs(last_order_id)

    # if quit_status == 1:
    #     break

# generate_report(transaction_info)
# save_inventory(transaction_info)
print("hi")
