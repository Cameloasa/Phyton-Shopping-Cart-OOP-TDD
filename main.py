from src.product import Product

def main():

    # Create a product
    hammer = Product("Hammer", 150)
    screwdriver = Product("Screwdriver", 90)

    print(hammer.get_id_product())
    print(hammer.get_product_info())
    print(screwdriver.get_id_product())
    print(screwdriver.get_product_info())







if __name__ == "__main__":
    main()