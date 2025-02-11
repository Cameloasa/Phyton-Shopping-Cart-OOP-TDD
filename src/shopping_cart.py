import uuid


class ShoppingCart:

    def __init__(self):
        self.__id_cart = str(uuid.uuid4())
        self.__cart = []

    def get_id_cart(self):
        pass

    # add product
    def add_product(self,product):
        pass

    def view_cart(self):
        pass

    def calculate_total(self):
        pass
