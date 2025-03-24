
url = "https://backend.tallinn-learning.ee"

class Endpoints:

    create_order = f"{url}/orders"
    get_all_orders = f"{url}/orders"
    get_order_by_id = lambda self, orderid: f"{url}/orders/{orderid}"
