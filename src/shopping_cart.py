import uuid

from src.product import Product


class ShoppingCart:

    def __init__(self):
        self.__id_cart = str(uuid.uuid4())[-4:]
        self.__cart = []

    def get_id_cart(self):
        return self.__id_cart

    # add product
    def add_product(self, product: Product):
        pass

    def view_cart(self):
        pass

    def calculate_total(self):
        pass
