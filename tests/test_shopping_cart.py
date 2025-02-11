from src.shopping_cart import ShoppingCart


def test_shopping_cart_unique_id():
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()
    assert cart1.get_id_cart() != cart2.get_id_cart()

def test_add_product():
    assert False


def test_view_cart():
    assert False


def test_calculate_total():
    assert False
