import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/9595")
    assert response.status_code == 200

def test_necessary_name():
    response = requests.get("https://petstore.swagger.io/v2/pet/9595")
    assert response.json()["name"] == "excavator"
