from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

from file_handling import load_inventory, save_inventory

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
    
def main():
    inventory = load_inventory()
    
    while True:
        menu_user_input = get_menu_selection()

        if menu_user_input == 1:
            inventory.display_all()
        elif menu_user_input == 2:
            inventory.add_product()
        elif menu_user_input == 3:
            inventory.update_stock()
        elif menu_user_input == 4:
            inventory.search_product()
        elif menu_user_input == 5:
            save_inventory(inventory)
        elif menu_user_input == 6:
            break
        else: 
            print("Invalid choice. Please enter 1 to 6.")
            continue

if __name__ == "__main__":
    product1 = PhysicalProduct("P001", "Guitar", 1500, 10, 3.5)
    product2 = PhysicalProduct("P002", "Laptop", 1200, 15, 2.0)

    print("Guitar Shipping Cost: $", product1.calculate_shipping_cost())
    print("Laptop Shipping Cost: $", product2.calculate_shipping_cost())