import pytest
import allure


class TestCourierLogin:

    @allure.title('Проверка авторизации зарегистрированного курьера')
    def test_courier_login(self, courier_data, courier_methods):
        login_pass = courier_methods.login_pass_registration_courier(courier_data)
        login = login_pass[0]
        password = login_pass[1]
        response = courier_methods.courier_login(login, password)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка ошибки авторизации при отсутствии одного из обязательных полей')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_courier_error_login_without_obligatory_field(self, courier_data, empty_field, courier_methods):
        courier_methods.login_pass_registration_courier(courier_data)
        courier_data[empty_field] = ''
        login = courier_data['login']
        password = courier_data['password']
        response = courier_methods.courier_login(login, password)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка ошибки авторизации при неверном в логине или пароле')
    @pytest.mark.parametrize('false_field', ['login', 'password'])
    def test_courier_error_login_with_false_login_or_password(self, courier_data, false_field, courier_methods):
        courier_methods.login_pass_registration_courier(courier_data)
        courier_data[false_field] = 'false_data'
        login = courier_data['login']
        password = courier_data['password']
        response = courier_methods.courier_login(login, password)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка ошибки регистрации под несуществующим пользователем')
    def test_courier_error_login_with_nonexistent_user(self, courier_methods):
        login = 'nonexistent_login'
        password = 'nonexistent_user'
        response = courier_methods.courier_login(login, password)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
