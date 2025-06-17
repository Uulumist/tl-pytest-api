import os
from dotenv import load_dotenv

import requests
import pytest

from services.orders.api_orders import OrdersAPI

load_dotenv()

url = os.getenv("TEST_URL")
username = os.getenv("TEST_USERNAME")
password = os.getenv("TEST_PASSWORD")

@pytest.fixture(scope="session")
def authenticate():
    login_url = f"{url}/login/student"
    body = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, json=body)
    if response.status_code == 200:
        token = response.text.strip()
        if token:
            print("✅ Successfully logged in. Bearer Token:", token)
            return token
        else:
            pytest.fail("❌ Authentication failed: No token found in response.")
    else:
        pytest.fail(f"❌ Failed to authenticate. Status: {response.status_code}, Response: {response.text}")

@pytest.fixture(autouse=True)
def cleanup_orders(authenticate):
    api = OrdersAPI(token=authenticate)
    api.delete_all_orders()