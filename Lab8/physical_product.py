from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
             stock: int, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = float(weight)

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight}kg\n")

    def get_fulfilment_info(self) -> str:
        return "Product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_cost = self.__weight * 2
        return shipping_cost

    def get_product_type(self) -> str:
        return "physical"