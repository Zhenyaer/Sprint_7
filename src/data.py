import random
import string
from faker import Faker

fake = Faker('ru_RU')


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


def order_data():
    payload_order = {
        "firstName": fake.first_name_male(),
        "lastName": fake.last_name_male(),
        "address": "Москва, ул. Карла Маркса 145",
        "metroStation": 4,
        "phone": "+7 981 555 44 33",
        "rentTime": 5,
        "deliveryDate": str(fake.future_date()),
        "comment": "Йо-хо-хо!!!",
        "color": [
            "BLACK"
        ]
    }
    return payload_order
