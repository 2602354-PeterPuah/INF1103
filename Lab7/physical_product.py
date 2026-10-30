from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}kg\n")

    def get_fulfilment_info(self):
        return "Product requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 2
        return shipping_cost

    