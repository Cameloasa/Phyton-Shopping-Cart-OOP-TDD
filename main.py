from src.order import Order
from src.product import Product
from src.shopping_cart import ShoppingCart
import json

def load_products_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return [Product(item["name"], item["price"]) for item in data]

def main():

    # Load products from JSON
    products = load_products_from_json("data/products.json")

    # Create shopping cart and add some products
    shopping_cart = ShoppingCart()
    shopping_cart.add_product(products[0])  # Hammer
    shopping_cart.add_product(products[1])  # Screwdriver
    shopping_cart.print_cart_info()

    # Create order
    order = Order(shopping_cart, "1234")
    order.print_order_info()




if __name__ == "__main__":
    main()