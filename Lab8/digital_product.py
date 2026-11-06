from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
             stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = float(download_size)

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Size: {self.__download_size}MB\n")

    def get_fulfilment_info(self) -> str:
        return "Product is delivered digitally."

    def get_product_type(self) -> str:
        return "digital"