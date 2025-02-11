import uuid


class Product:

    def __init__(self, name, price):
        self.__id = str(uuid.uuid4())
        self.__name = name
        self.__price = price

    def get_info(self):
        return {"id": self.__id, "name": self.__name, "price": self.__price}
