from src.product import Product

def main():

    # Create a product
    hammer = Product("Hammer", 150)
    screwdriver = Product("Screwdriver", 90)

    hammer.get_id_product()
    hammer.get_product_info()
    screwdriver.get_product_info()
    screwdriver.get_id_product()






if __name__ == "__main__":
    main()