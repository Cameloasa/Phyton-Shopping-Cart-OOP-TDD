import uuid


class Order:
    def __init__(self, cart, customer_id):
        self.__id_order = str(uuid.uuid4())[-4:]
        self.__cart = cart.view_cart()
        self.__total = cart.calculate_total()
        self.__customer_id = customer_id #hardcode
        self.__status = "Pending"

    def get_id_order(self):
        return self.__id_order

    def get_order_info(self):
        return {
            "id": self.__id_order,
            "cart": self.__cart,
            "total": self.__total,
            "customer_id": self.__customer_id
        }

    def get_status(self):
        return self.__status

    def confirm_order(self):
        self.__status = "Confirmed"
        return f"Order {self.__id_order} has been confirmed successfully."

    def cancel_order(self):
        if self.__status == "Confirmed":
            return f"Order {self.__id_order} has already been confirmed and cannot be canceled."
        self.__status = "Canceled"
        return f"Order {self.__id_order} has been canceled."

    def print_order_info(self):
        print(f"🛒 Order ID: {self.__id_order}")
        print(f"👤 Customer ID: {self.__customer_id}")

        if not self.__cart:
            print("🛍️ Your cart is empty.")
        else:
            print("🛍️ Your Cart:")
            for product in self.__cart:
                print(f"  - {product['name']} | Price: {product['price']} SEK")

        print(f"💰 Total: {self.__total} SEK")

