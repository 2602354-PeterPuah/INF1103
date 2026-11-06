from product import Product

class OrderLine ():
    def __init__(self, product: Product, quantity: int):
        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def get_product_id(self) -> str:
        return self.__product.get_product_id()

    def display_information(self) -> None:
        self.__product.display_information()
        print(f"Quantity Ordered: {self.__quantity}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")