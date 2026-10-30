from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}kg\n")

    def get_fulfilment_info(self):
        return "Product requires physical shipping."