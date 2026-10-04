import json

def load_inventory():
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    return inventory

def get_menu_selection():
    print("\n----------- MENU ----------")
    print("1. Display All Product")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------\n")

    menu_user_input = int(input("Enter option: "))
    return menu_user_input

def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")
    for product in inventory:
        print(f"ID: {product['ID']} | Name: {product['Name']} | Price: ${product['Price']:.2f} | Stock: {product['Stock']}")
    print("------------------------------------------------")

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = input("Product Price: ")
    product_quantity = input("Stock Quantity: ")

    new_product = {
        "ID": product_id,
        "Name": product_name,
        "Price": float(product_price),
        "Stock": int(product_quantity)
    }

    inventory.append(new_product)
    print("Product added successsfully!")

    return inventory

def update_stock(inventory):
    print("\nUpdate Stock")
    get_id = input("Enter Product ID: ")

    for product in inventory:
        if product["ID"] == get_id:
            print("\nProduct Found:")
            print("Name:", product["Name"])
            print("Current Stock:", product["Stock"])

            get_new_quantity = int(input("\nNew Stock Quantity: "))
            product["Stock"] = get_new_quantity
            print("Stock updated successfully!")
    return inventory

def search_product(inventory):
    print("\nSearch Product")
    get_id = input("Enter Product ID: ")
    
    for product in inventory:
        if product["ID"] == get_id:
            print("\nProduct Found:")
            print("-----------------------------------------------")
            print("ID:", product["ID"])
            print("Name:", product["Name"])
            print("Price:", product["Price"])
            print("Current Stock:", product["Stock"])
            print("-----------------------------------------------")
    
def save_inventory(inventory):
    print("\nSaving inventory...")

    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

    print("Inventory saved successfully to inventory.json.")

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

inventory = load_inventory()

while True:
    menu_user_input = get_menu_selection()

    if menu_user_input == 1:
        display_all(inventory)
    elif menu_user_input == 2:
        inventory = add_product(inventory)
    elif menu_user_input == 3:
        inventory = update_stock(inventory)
    elif menu_user_input == 4:
        inventory = search_product(inventory)
    elif menu_user_input == 5:
        save_inventory(inventory)


