import pytest
from methods.courier_methods import CourierMethods
from src.data import create_courier_data
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier_data():
    payload = create_courier_data()
    yield payload


@pytest.fixture()
def courier_data_with_delete_courier():
    payload = create_courier_data()
    yield payload
    login = payload['login']
    password = payload['password']
    response = CourierMethods()
    courier_id = response.courier_login(login, password).json()["id"]
    response.courier_delete(courier_id)


@pytest.fixture()
def courier_methods():
    yield CourierMethods()


@pytest.fixture()
def order_methods():
    yield OrderMethods()
