import uuid
from src.product import Product


class ShoppingCart:

    def __init__(self):
        self.__id_cart = str(uuid.uuid4())[-4:]
        self.__cart = []

    def get_id_cart(self):
        return self.__id_cart

    def view_cart(self):
        return [product.get_product_info() for product in self.__cart]

    # add product
    def add_product(self, product: Product):
        if not isinstance(product,Product):
            raise TypeError('Can only add Product objects to the cart')
        self.__cart.append(product)



    def calculate_total(self):
        return sum(product.get_product_info()['price'] for product in self.__cart)

    def print_cart_info(self):
        if not self.__cart:
            print("🛒 Cart is empty!")
            return
        print("\n🛍️ Shopping Cart:")
        for product in self.__cart:
            print(f"📦 {product.get_product_info()['name']} - 💰 {product.get_product_info()['price']} SEK")
        print("────────────────────────")
        print(f"🧾 Total: {self.calculate_total()} SEK")