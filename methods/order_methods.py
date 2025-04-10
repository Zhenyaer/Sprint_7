import allure
from src.urls import Urls
from methods.base_methods import BaseMethods


class OrderMethods:

    @allure.step('Создание заказа')
    def order_create(self, payload):
        url = Urls.url_order_create
        return BaseMethods.post_request(url, payload)

    @allure.step('Получение списка заказов')
    def get_order_list(self):
        url = Urls.url_order_list
        return BaseMethods.get_request(url)

    @allure.step('Принятие заказа')
    def accept_order(self, order_id, courier_id):
        url = Urls.url_order_accept
        return BaseMethods.put_request(f'{url}/{order_id}?courierId={courier_id}')

    @allure.step('Получение заказа')
    def get_order_on_track(self, track_id):
        url = Urls.url_order_get
        return BaseMethods.get_request(f'{url}?t={track_id}')
