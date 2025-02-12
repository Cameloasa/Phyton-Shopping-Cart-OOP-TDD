import uuid


class Order:
    def __init__(self, cart, customer_id):
        self.__id_order = str(uuid.uuid4())[-4:]
        self.__cart = cart.view_cart()
        self.__total = cart.calculate_total()
        self.__customer_id = customer_id #hardcode

    def get_id_order(self):
        return self.__id_order

    def get_order_info(self):
        return {
            "id": self.__id_order,
            "cart": self.__cart,
            "total": self.__total,
            "customer_id": self.__customer_id
        }

    def confirm_order(self):
        pass

    def cancel_order(self):
        pass

    def print_order_info(self):
        pass