import pytest

from src.product import Product
from src.shopping_cart import ShoppingCart


def test_shopping_cart_unique_id():
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()
    assert cart1.get_id_cart() != cart2.get_id_cart()

def test_view_empty_cart():
    cart = ShoppingCart()
    assert cart.view_cart() == "Cart is empty"

def test_add_product():
    cart = ShoppingCart()
    product = Product("Hammer",150)
    cart.add_product(product)

    print("Cart content:", cart.view_cart())
    assert len(cart.view_cart()) == 1
    assert cart.view_cart()[0]["name"] == "Hammer"
    assert cart.view_cart()[0]["price"] == 150

def test_add_invalid_product():
    cart = ShoppingCart()
    with pytest.raises(TypeError, match= 'Can only add Product objects to the cart'):
        cart.add_product("Not a product")

def test_view_cart():
    cart = ShoppingCart()
    assert cart.view_cart() == ["Hammer", 150]


def test_calculate_total():
    cart = ShoppingCart()
    product1 = Product("Hammer", 150)
    product2 = Product("Screwdriver", 90)
    cart.add_product(product1)
    cart.add_product(product2)

    assert cart.calculate_total() == 240
