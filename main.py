from src.order import Order
from src.product import Product
from src.shopping_cart import ShoppingCart


def main():

    # Create a product
    hammer = Product("Hammer", 150)
    screwdriver = Product("Screwdriver", 90)

    hammer.print_product_info()
    #print(hammer.get_product_info())
    screwdriver.print_product_info()
    #print(hammer.get_product_info())

    # Create shopping cart
    shopping_cart = ShoppingCart()
    shopping_cart.add_product(hammer)
    shopping_cart.add_product(screwdriver)
    #print(shopping_cart.view_cart())
    shopping_cart.print_cart_info()

    # Create order
    order = Order(shopping_cart,"1234")
    order.print_order_info()







if __name__ == "__main__":
    main()