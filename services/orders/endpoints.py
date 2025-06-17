import os

class Endpoints:
    def __init__(self):
        url = os.getenv("TEST_URL")
        if not url:
            raise ValueError("❌ TEST_URL is not set in environment!")

        self.create_order = f"{url}/orders"
        self.get_all_orders = f"{url}/orders"
        self.get_order_by_id = lambda orderid: f"{url}/orders/{orderid}"
        self.delete_order_by_id = lambda orderid: f"{url}/orders/{orderid}"
        self.get_deleted_order_by_id = lambda orderid: f"{url}/orders/{orderid}"
