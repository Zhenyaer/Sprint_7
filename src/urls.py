class Api:
    courier_create = '/api/v1/courier'
    courier_login = '/api/v1/courier/login'
    courier_delete = '/api/v1/courier'
    order_create = '/api/v1/orders'
    order_list = '/api/v1/orders'
    order_accept = '/api/v1/orders/accept'
    order_get = '/api/v1/orders/track'


class Urls:
    url_scooter_base = 'https://qa-scooter.praktikum-services.ru'
    url_courier_create = f'{url_scooter_base}{Api.courier_create}'  # Создание курьера
    url_courier_login = f'{url_scooter_base}{Api.courier_login}'   # Логин курьера
    url_courier_delete = f'{url_scooter_base}{Api.courier_delete}'  # /:id Удаление курьера
    url_order_create = f'{url_scooter_base}{Api.order_create}'  # Создание заказа
    url_order_list = f'{url_scooter_base}{Api.order_list}'  # Получение списка заказов
    url_order_accept = f'{url_scooter_base}{Api.order_accept}'  # Принятие заказа
    url_order_get = f'{url_scooter_base}{Api.order_get}'  # Получение заказа
