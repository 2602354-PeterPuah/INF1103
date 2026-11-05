from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class Inventory:
    def __init__(self, inventory):
        self.__inventory = inventory

    def store_product(self):
        pass

    def get_inventory(self):
        return self.__inventory
    
    def add_product(self):
        print("\nAdd New Product")

        product_id = input("Product ID: ")

        for product in self.__inventory:
            if product.get_product_id() == product_id:
                print("Invalid input. Product ID already exists.")
                return

        product_name = input("Product Name: ")
        product_price = float(input("Product Price: "))
        product_quantity = int(input("Stock Quantity: "))

        print("\nSelect Product Type")
        print("1. Physical Product")
        print("2. Digital Product\n")

        product_type = input("Enter option: ")

        if product_type == "1":
            weight = float(input("\nProduct Weight (kg): "))

            new_product = PhysicalProduct(
                product_id,
                product_name,
                product_price,
                product_quantity,
                weight
            )

        elif product_type == "2":
            download_size = float(input("\nDownload Size (MB): "))

            new_product = DigitalProduct(
                product_id,
                product_name,
                product_price,
                product_quantity,
                download_size
            )

        else:
            print("Invalid product type.")
            return

        self.__inventory.append(new_product)
        print("Product added successfully!")

    def search_product(self):
        print("\nSearch Product")
        get_id = input("Enter Product ID: ")
        found = False
    
        for product in self.__inventory:
            if product.get_product_id() == get_id:
                print("\nProduct Found:")
                print("-----------------------------------------------")
                product.display_information()
                print("-----------------------------------------------")
                found = True
                break
    
        if found == False:
            print("Product not found.")

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