from product import Product

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
        product_name = input("Product Name: ")
        product_price = input("Product Price: ")
        product_quantity = input("Stock Quantity: ")

        for product in self.__inventory:
            if product.get_product_id() == product_id:
                print("Invalid input. Product ID already exists.")
                return self.__inventory

        new_product = Product(
            product_id,
            product_name,
            float(product_price),
            int(product_quantity)
        )

        self.__inventory.append(new_product)
        print("Product added successsfully!")\
            
        return self.__inventory

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