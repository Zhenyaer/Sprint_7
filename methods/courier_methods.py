import allure
from src.urls import Urls
from methods.base_methods import BaseMethods


class CourierMethods:

    @allure.step('Регистрация курьера')
    def courier_create(self, payload):
        url = Urls.url_courier_create
        return BaseMethods.post_request(url, payload)

    @allure.step('Регистрация курьера и получение его логина и пароля')
    def login_pass_registration_courier(self, payload):
        login_pass = []
        response = self.courier_create(payload)
        if response.status_code == 201:
            login_pass.append(payload['login'])
            login_pass.append(payload['password'])
        return login_pass

    @allure.step('Авторизация курьера')
    def courier_login(self, login, password):
        payload = {
            "login": login,
            "password": password}
        url = Urls.url_courier_login
        return BaseMethods.post_request(url, payload)

    @allure.step('Удаление курьера')
    def courier_delete(self, courier_id):
        return BaseMethods.delete_request(f'{Urls.url_courier_delete}/{courier_id}')

    @allure.step('Получение id курьера')
    def get_courier_id(self, login, password):
        response = self.courier_login(login, password)
        return response.json()["id"]
