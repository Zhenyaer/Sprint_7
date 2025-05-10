import pytest
import allure
from src.data import create_courier_data


class TestCourierCreate:

    @allure.title('Проверка создания курьера')
    def test_courier_create(self, courier_data_with_delete_courier, courier_methods):
        response = courier_methods.courier_create(courier_data_with_delete_courier)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_courier_impossibility_create_two_similar(self, courier_data, courier_methods):
        courier_methods.courier_create(courier_data)
        response = courier_methods.courier_create(courier_data)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка невозможности регистрации курьера без заполнения одного из полей')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_courier_impossibility_create_without_obligatory_field(self, courier_data, empty_field, courier_methods):
        courier_data[empty_field] = ''
        response = courier_methods.courier_create(courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка невозможности создания курьера с логином, который уже есть')
    def test_courier_impossibility_create_with_similar_login(self, courier_data, courier_methods):
        courier_methods.courier_create(courier_data)
        login_1 = courier_data['login']
        courier_data_2 = create_courier_data()
        courier_data_2['login'] = login_1
        response = courier_methods.courier_create(courier_data_2)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
