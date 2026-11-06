from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product

class Inventory:
    def __init__(self, inventory: list[Product]):
        self.__inventory: list[Product] = inventory

    def store_product(self):
        pass

    def get_inventory(self) -> list[Product]:
        return self.__inventory
    
    def add_product(self, product: Product) -> None:
        for existing_product in self.__inventory:
            if existing_product.get_product_id() == product.get_product_id():
                print("Invalid input. Product ID already exists.")
                return

        self.__inventory.append(product)
        print("Product added successfully!")

    def remove_product(self, product_id: str) -> None:
        for product in self.__inventory:
            if product.get_product_id() == product_id:
                self.__inventory.remove(product)
                print("Product removed successfully!")
                return

        print("Product not found.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__inventory:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")

        for product in self.__inventory:
            product.display_information()

        print("------------------------------------------------")

    def update_stock(self):
        print("\nUpdate Stock")

        get_id = input("Enter Product ID: ")

        for product in self.__inventory:
            if product.get_product_id() == get_id:

                print("\nProduct Found:")
                print("Name:", product.get_name())
                print("Current Stock:", product.get_stock())

                get_new_quantity = int(input("\nNew Stock Quantity: "))

                product.update_stock(get_new_quantity)
                return

        print("Product not found.")