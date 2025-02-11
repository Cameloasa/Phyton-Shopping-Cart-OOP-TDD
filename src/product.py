import uuid


class Product:

    def __init__(self, name:str, price:float):
        if not name :
            raise ValueError('Name cannot be empty')
        if price < 0:
            raise ValueError('Price must be non-negative')
        self.__id_product = str(uuid.uuid4())[-4:]
        self.__name = name
        self.__price = price

    def get_id_product(self):
        return self.__id_product

    def get_product_info(self):
        info_product = {"id": self.__id_product,
                        "name": self.__name,
                        "price": self.__price}
        print(info_product)
