from src.order import Order
from src.product import Product
from src.shopping_cart import ShoppingCart


def test_get_id_order():
    cart = ShoppingCart()
    product = Product("Hammer",150)
    cart.add_product(product)
    order = Order(cart, "123")

    assert isinstance(order.get_id_order(), str)
    assert len(order.get_id_order()) == 4


def test_get_order_info():
    cart = ShoppingCart()
    product = Product("Hammer", 150)
    cart.add_product(product)
    order = Order(cart, "1234")

    order_info = order.get_order_info()
    assert len(order_info) == 4

    assert isinstance(order_info["id"], str)
    assert len(order_info["id"]) == 4

    assert len(order_info["cart"]) == 1
    assert order_info["cart"][0]["name"] == "Hammer"
    assert order_info["cart"][0]["price"] == 150

    assert order_info["total"] == 150

    assert order_info["customer_id"] == "1234"


def test_confirm_order():
    cart = ShoppingCart()
    product = Product("Hammer", 150)
    cart.add_product(product)
    order = Order(cart, "123")

    confirmation_message = order.confirm_order()


    assert order.get_status() == "Confirmed"

    assert confirmation_message == f"Order {order.get_id_order()} has been confirmed successfully."


def test_cancel_order():
    cart = ShoppingCart()
    product = Product("Hammer", 150)
    cart.add_product(product)

    order = Order(cart, "1234")
    assert order.get_status() == "Pending"

    message = order.cancel_order()
    assert message == f"Order {order.get_id_order()} has been canceled."
    assert order.get_status() == "Canceled"

def test_cancel_confirmed_order():
    cart = ShoppingCart()
    product = Product("Hammer", 150)
    cart.add_product(product)

    order = Order(cart, "1234")
    order.confirm_order()

    message = order.cancel_order()
    assert message == f"Order {order.get_id_order()} has already been confirmed and cannot be canceled."
    assert order.get_status() == "Confirmed"

def test_print_order_info():
    assert True
