import json
from inventory import Inventory
from product import Product

def load_inventory():
    try:    
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        product_list = []

        for product_data in inventory:
            product = Product(
                product_data["ID"],
                product_data["Name"],
                product_data["Price"],
                product_data["Stock"]
            )

            product_list.append(product)

        inventory = Inventory(product_list)

    except:
        print("inventory.json is empty.")
        inventory = Inventory([])

    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    return inventory

def save_inventory(inventory):
    print("\nSaving inventory...")

    inventory_data = []

    for product in inventory.get_inventory():
        product_data = {
            "ID": product.get_product_id(),
            "Name": product.get_name(),
            "Price": product.get_price(),
            "Stock": product.get_stock()
        }

        inventory_data.append(product_data)

    with open("inventory.json", "w") as file:
        json.dump(inventory_data, file)

    print("Inventory saved successfully to inventory.json.")