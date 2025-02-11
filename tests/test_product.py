import pytest

from src.product import Product


def test_create_product():
    product = Product("Hammer", 150)
    info_product = product.get_product_info()
    assert info_product['name'] == "Hammer"
    assert info_product['price'] == 150

def test_unique_product_id():
    product1 = Product("Hammer", 150)
    product2 = Product("Screwdriver", 90)
    assert product1.get_id_product() != product2.get_id_product()

def test_zero_price():
    product = Product("Free Sample", 0)
    assert product.get_product_info()['price'] == 0

def test_negative_price():
    with pytest.raises(ValueError,match= 'Price must be non-negative'):
        Product("Hammer", -150)

def test_empty_product_name():
    with pytest.raises(ValueError, match='Name cannot be empty'):
        Product('', 150)