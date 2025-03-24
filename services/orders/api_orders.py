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
            json=self.payloads.create_order
        )

        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = OrderModel(**response.json())
        return model

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