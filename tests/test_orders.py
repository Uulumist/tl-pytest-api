import allure
import pytest

from services.orders.api_orders import OrdersAPI
from tests.conftest import authenticate

number_of_orders=10

@allure.epic("Order Operations")
@allure.feature("Orders")

class TestOrders:



        @pytest.mark.orders
        @allure.title("Create new order")
        def test_create_order(self, authenticate):
            orders_api = OrdersAPI(token=authenticate)
            order = orders_api.create_order()
            print(f"Created Order ID: {order.id}")
            print(f"Created Order customerName: {order.customerName}")
            print(f"Created Order customerPhone: {order.customerPhone}")
            orders_api.get_order_by_id(order.id)
            orders_api.delete_order_by_id(order.id)
            orders_api.get_deleted_order_by_id(order.id)

        @pytest.mark.orders
        @allure.title("Create and verify orders")
        def test_create_and_verify_orders(self, authenticate):
            api = OrdersAPI(token=authenticate)
            created_orders = []

            for _ in range(number_of_orders):
                order = api.create_order()
                created_orders.append(order)

            all_orders = api.get_all_orders()
            all_ids = [order.id for order in all_orders]

            for created in created_orders:
                fetched = api.get_order_by_id(created.id)
                assert fetched == created

            for created in created_orders:
                api.delete_order_by_id(created.id)

            remaining = api.get_all_orders()
            remaining_ids = [order.id for order in remaining]
            for created in created_orders:
                assert created.id not in remaining_ids, f"Order ID {created.id} was not deleted"