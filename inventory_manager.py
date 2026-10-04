import json
exit_status = 0

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

    for product in inventory:
        if product["ID"] == product_id:
            print("Invalid input. Product ID already exists.")
            return inventory

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
    found = False

    for product in inventory:
        if product["ID"] == get_id:
            print("\nProduct Found:")
            print("-----------------------------------------------")
            print("ID:", product["ID"])
            print("Name:", product["Name"])
            print("Price:", product["Price"])
            print("Current Stock:", product["Stock"])
            print("-----------------------------------------------")
            found = True
            break

    if found == False:
        print("Product not found.")
    
def save_inventory(inventory):
    print("\nSaving inventory...")

    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

    print("Inventory saved successfully to inventory.json.")

def exit_program(inventory):
    print("\nSaving inventory before exit..")
    print("Inventory saved successfully")

    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
    
    print("\nThank you for using Inventory Management System")
    print("Program terminated")

    return 1

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
        search_product(inventory)
    elif menu_user_input == 5:
        save_inventory(inventory)
    elif menu_user_input == 6:
        exit_status = exit_program(inventory)
    else: 
        continue

    if exit_status == 1:
        break
