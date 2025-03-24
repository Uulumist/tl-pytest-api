import allure
import pytest

from services.orders.api_orders import OrdersAPI

@allure.epic("Order Operations")
@allure.feature("Orders")

class TestOrders:

        @pytest.mark.orders
        @allure.title("Create new order")
        def test_create_order(self, authenticate):
            orders_api = OrdersAPI(token=authenticate)
            order = orders_api.create_order()
            orders_api.get_order_by_id(order.id)
