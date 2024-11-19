import json.decoder

import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class Authorization(BaseEndpoint):
    def __init__(self, name:str = None):
        super().__init__()
        self.user = name

    @allure.step("Получение токена")
    def get_token(self):
        url = f"{self.url}/{self.endpoint['authorize']}"
        payload = None
        if self.user is not None:
            payload = {
                "name": self.user
            }
        response = requests.post(url, json=payload, headers=self.headers)
        self.response = response
        try:
            self.token = response.json()["token"]
            return self.token
        except json.decoder.JSONDecodeError:
            return None

    @allure.step("Проверка актуальности токена")
    def check_token(self):
        url = f"{self.url}/{self.endpoint["authorize"]}/{self.token}"
        print(url)
        response = requests.get(url, headers=self.headers)
        assert "Token is alive" in response.text == True
