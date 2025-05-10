import allure
from methods.courier_methods import CourierMethods


class TestCourierDelete:

    @allure.title('Проверка удаления курьера по id')
    def test_courier_delete(self, courier_data, courier_methods):
        login_pass = courier_methods.login_pass_registration_courier(courier_data)
        res = courier_methods.courier_login(login_pass[0], login_pass[1])
        courier_id = res.json()["id"]
        courier = CourierMethods()
        response = courier.courier_delete(courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Проверка ошибки при попытке удаления курьера без указания id')
    def test_courier_delete_error_with_empty_id(self, courier_methods):
        courier_id = ''
        response = CourierMethods()
        assert response.courier_delete(courier_id).status_code == 404

    @allure.title('Проверка ошибки при попытке удаления курьера с несуществующим id')
    def test_courier_delete_error_with_empty(self, courier_methods):
        courier_id = '234563256'
        response = CourierMethods()
        assert response.courier_delete(courier_id).status_code == 404
