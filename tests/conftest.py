import os
import requests
import pytest

url = os.getenv("URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

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