import json
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def load_inventory():
    try:    
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        product_list = []

        for product_data in inventory:
            if product_data["Type"] == "physical":
                product = PhysicalProduct(
                    product_data["ID"],
                    product_data["Name"],
                    product_data["Price"],
                    product_data["Stock"],
                    product_data["Weight"]
                )

            elif product_data["Type"] == "digital":
                product = DigitalProduct(
                    product_data["ID"],
                    product_data["Name"],
                    product_data["Price"],
                    product_data["Stock"],
                    product_data["DownloadSize"]
                )

            else:
                print("Unknown product type. Skipping product.")
                continue

            product_list.append(product)


        inventory = Inventory(product_list)

    except:
        print("inventory.json is empty.")
        return

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

        if product.get_product_type() == "physical":
            product_data["Type"] = "physical"
            product_data["Weight"] = product.get_weight()

        elif product.get_product_type() == "digital":
            product_data["Type"] = "digital"
            product_data["DownloadSize"] = product.get_download_size()

        inventory_data.append(product_data)

    with open("inventory.json", "w") as file:
        json.dump(inventory_data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")