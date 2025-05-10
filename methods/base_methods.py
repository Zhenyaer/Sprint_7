import requests


class BaseMethods:

    # POST запрос
    @staticmethod
    def post_request(url, payload):
        return requests.post(url, json=payload)

    # GET запрос
    @staticmethod
    def get_request(url):
        return requests.get(url)

    # DELETE запрос
    @staticmethod
    def delete_request(url):
        return requests.delete(url)

    # PUT запрос
    @staticmethod
    def put_request(url):
        return requests.put(url)
