import os

url = os.getenv("TEST_URL")

class Endpoints:

    create_order = f"{url}/orders"
    get_all_orders = f"{url}/orders"
    get_order_by_id = lambda self, orderid: f"{url}/orders/{orderid}"
    delete_order_by_id = lambda self, orderid: f"{url}/orders/{orderid}"
    get_deleted_order_by_id = lambda self, orderid: f"{url}/orders/{orderid}"
