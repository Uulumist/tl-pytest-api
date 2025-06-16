import allure
import requests

from config.headers import Headers
from services.orders.endpoints import Endpoints
from services.orders.models.order_model import OrderModel
from services.orders.payloads import Payloads
from utils.helper import Helper

class OrdersAPI(Helper):

    def __init__(self, token):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers(token)

    @allure.step("Create order")
    def create_order(self):
        response = requests.post(
            url=self.endpoints.create_order,
            headers=self.headers.basic,
            json=self.payloads.create_order()
        )

        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = OrderModel(**response.json())
        return model

    @allure.step("Get all orders")
    def get_all_orders(self):
        response = requests.get(
            url=self.endpoints.get_all_orders,
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return [OrderModel(**order) for order in response.json()]

    @allure.step("Get order by ID")
    def get_order_by_id(self, orderid):
        response = requests.get(
            url=self.endpoints.get_order_by_id(orderid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = OrderModel(**response.json())
        return model

    @allure.step("Delete all existing orders")
    def delete_all_orders(self):
        orders = self.get_all_orders()
        assert isinstance(orders, list), f"Expected a list of orders, got: {type(orders)}"

        for order in orders:
            order_id = order.id
            assert order_id is not None, f"Order missing 'id': {order}"
            self.delete_order_by_id(order_id)

        remaining_orders = self.get_all_orders()
        assert remaining_orders == [] or len(remaining_orders) == 0, f"Some orders were not deleted: {remaining_orders}"

    @allure.step("Delete order by ID")
    def delete_order_by_id(self, orderid):
        response = requests.delete(
            url=self.endpoints.delete_order_by_id(orderid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200
        assert response.json() is True

    @allure.step("Check that order is deleted by ID")
    def get_deleted_order_by_id(self, orderid):
        response = requests.get(
            url=self.endpoints.get_order_by_id(orderid),
            headers=self.headers.basic,
            )
        assert response.status_code == 200
        assert response.text.strip() == ""