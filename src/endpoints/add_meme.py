import json

import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class AddMeme(BaseEndpoint):
    @allure.step("Добавление нового мема")
    def add_meme(self, payload: dict):
        url = f"{self.url}/{self.endpoint['meme']}"
        self.response = requests.post(url, json=payload, headers=self.headers)
        try:
            self.meme_id = self.response.json()["id"]
        except json.decoder.JSONDecodeError:
            pass
        return self.response