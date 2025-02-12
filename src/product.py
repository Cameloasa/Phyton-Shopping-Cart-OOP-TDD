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
        return {
            "id": self.__id_product,
            "name": self.__name,
            "price": self.__price
            }

    def print_product_info(self):
        info_product = f"📦 Produkt:\n" \
                       f"   🆔 ID: {self.__id_product}\n" \
                       f"   🏷️ Namn: {self.__name}\n" \
                       f"   💰 Pris: {self.__price} SEK"
        print(info_product)