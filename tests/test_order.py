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
    order = Order(cart, "123")

    order_info = order.get_order_info()
    assert len(order_info) == 4

    assert isinstance(order_info["id"], str)
    assert len(order_info["id"]) == 4


def test_confirm_order():
    assert False


def test_cancel_order():
    assert False


def test_print_order_info():
    assert True
