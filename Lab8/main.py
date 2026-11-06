from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from order import Order

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
    # Create Supplier
    supplier = Supplier("S001", "ABC Electronics", "abc@email.com")

    # Create Products
    physical = PhysicalProduct(
        "P001", "Guitar", 1500, 10, 3.5, supplier
    )

    digital = DigitalProduct(
        "P002", "Software", 100, 20, 500, supplier
    )

    # Create Orders
    order1 = Order("O001")
    order2 = Order("O002")

    # Add Products to Order 1
    order1.add_order_line(physical, 2)
    order1.add_order_line(digital, 3)

    # Add the same Product to Order 2
    order2.add_order_line(physical, 1)

    # Display Order 1
    print("\nOrder 1:")
    order1.display_order_lines()
    print(f"Total: ${order1.calculate_total():.2f}")

    # Display Order 2
    print("\nOrder 2:")
    order2.display_order_lines()
    print(f"Total: ${order2.calculate_total():.2f}")

    # Remove one OrderLine from Order 1
    order1.remove_order_line("P001")

    print("\nOrder 1 after removal:")
    order1.display_order_lines()
    print(f"Total: ${order1.calculate_total():.2f}")

    # Check that original Product still exists
    print("\nOriginal Product:")
    physical.display_information()