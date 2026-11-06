from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from order import Order

from file_handling import load_inventory, save_inventory

def get_menu_selection() -> int:
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

def create_product() -> Product | None:
    print("\nAdd New Product")

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Product Price: "))
    stock = int(input("Stock Quantity: "))

    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Email: ")

    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    print("\n1. Physical Product")
    print("2. Digital Product")
    product_type = input("Select Product Type: ")

    if product_type == "1":
        weight = float(input("Weight (kg): "))
        return PhysicalProduct(
            product_id, name, price, stock, weight, supplier
        )

    elif product_type == "2":
        download_size = float(input("Download Size (MB): "))
        return DigitalProduct(
            product_id, name, price, stock, download_size, supplier
        )

    print("Invalid product type.")
    return None

def main() -> None:
    inventory = load_inventory()

    if inventory is None:
        inventory = Inventory([])
    
    while True:
        menu_user_input = get_menu_selection()

        if menu_user_input == 1:
            inventory.display_all()
        elif menu_user_input == 2:
            new_product = create_product()

            if new_product is not None:
                inventory.add_product(new_product)
        elif menu_user_input == 3:
            inventory.update_stock()
        elif menu_user_input == 4:
            inventory.find_product()
        elif menu_user_input == 5:
            save_inventory(inventory)
        elif menu_user_input == 6:
            break
        else: 
            print("Invalid choice. Please enter 1 to 6.")
            continue
            
if __name__ == "__main__":
    main()