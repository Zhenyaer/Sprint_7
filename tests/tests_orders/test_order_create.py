import pytest
import allure
from src.data import order_data


class TestOrderCreate:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize('colour', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_create_order_with_different_colour(self, order_methods, colour):
        payload = order_data()
        payload["colour"] = colour
        response = order_methods.order_create(payload)
        assert response.status_code == 201
        assert 'track' in response.json()
