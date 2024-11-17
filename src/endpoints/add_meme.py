import allure
import requests

from src.endpoints.base_endpoint import BaseEndpoint


class AddMeme(BaseEndpoint):
    @allure.step("Добавление нового мема")
    def add_meme(self, payload: dict):
        url = f"{self.url}/{self.endpoint["meme"]}"
        return requests.post(url, json=payload, headers=self.headers)