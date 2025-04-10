import allure
from src.data import order_data


class TestOrderList:

    @allure.title('Проверка получения списка заказа')
    def test_get_order_list(self, order_methods):
        response = order_methods.get_order_list()
        assert response.status_code == 200
        assert 'orders' in response.json()

    @allure.title('Проверка получения заказа по id')
    def test_get_order_on_id(self, order_methods):
        payload = order_data()
        response_order = order_methods.order_create(payload)
        order_id = response_order.json()["track"]
        response = order_methods.get_order_on_track(order_id)
        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title('Проверка ошибки при отсутствии номера заказа')
    def test_get_order_error_with_empty_id(self, order_methods):
        order_id = ''
        response = order_methods.get_order_on_track(order_id)
        assert response.status_code == 400

    @allure.title('Проверка ошибки при несуществующем номера заказа')
    def test_get_order_error_with_nonexistent_id(self, order_methods):
        order_id = '999888777'
        response = order_methods.get_order_on_track(order_id)
        assert response.status_code == 404
