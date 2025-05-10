import allure
from src.data import order_data


class TestOrderAccept:

    @allure.title('Проверка принятия заказа')
    def test_order_accept(self, courier_data_with_delete_courier, order_methods, courier_methods):
        # Создание и получение id курьера
        login_pass = courier_methods.login_pass_registration_courier(courier_data_with_delete_courier)
        response_courier = courier_methods.courier_login(login_pass[0], login_pass[1])
        courier_id = response_courier.json()["id"]
        # Создание и получение id заказа
        payload = order_data()
        response_order = order_methods.order_create(payload)
        track_id = response_order.json()["track"]
        order_id = order_methods.get_order_on_track(track_id).json()['order']['id']
        # Проверка принятия заказа
        response = order_methods.accept_order(order_id, courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Проверка ошибки при указании несуществующего id курьера')
    def test_order_accept_error_nonexistent_id_courier(self, order_methods):
        courier_id = '56785336'
        # Создание и получение id заказа
        payload = order_data()
        response_order = order_methods.order_create(payload)
        track_id = response_order.json()["track"]
        order_id = order_methods.get_order_on_track(track_id).json()['order']['id']
        # Проверка принятия заказа
        response = order_methods.accept_order(order_id, courier_id)
        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id не существует"

    @allure.title('Проверка ошибки при указании пустого id курьера')
    def test_order_accept_error_empty_id_courier(self, order_methods):
        courier_id = ''
        payload = order_data()
        response_order = order_methods.order_create(payload)
        track_id = response_order.json()["track"]
        order_id = order_methods.get_order_on_track(track_id).json()['order']['id']

        response = order_methods.accept_order(order_id, courier_id)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title('Проверка ошибки при указании несуществующего id заказа')
    def test_order_accept_error_nonexistent_id_order(self, courier_data_with_delete_courier, order_methods, courier_methods):
        login_pass = courier_methods.login_pass_registration_courier(courier_data_with_delete_courier)
        response_courier = courier_methods.courier_login(login_pass[0], login_pass[1])
        courier_id = response_courier.json()["id"]
        order_id = '564567854'

        response = order_methods.accept_order(order_id, courier_id)
        assert response.status_code == 404
        assert response.json()["message"] == "Заказа с таким id не существует"

    @allure.title('Проверка ошибки при указании пустого id заказа')
    def test_order_accept_error_empty_id_order(self, courier_data_with_delete_courier, order_methods, courier_methods):
        login_pass = courier_methods.login_pass_registration_courier(courier_data_with_delete_courier)
        response_courier = courier_methods.courier_login(login_pass[0], login_pass[1])
        courier_id = response_courier.json()["id"]
        order_id = ''

        response = order_methods.accept_order(order_id, courier_id)
        assert response.status_code == 404
        assert response.json()["message"] == "Not Found."
