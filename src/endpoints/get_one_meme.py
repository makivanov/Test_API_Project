import allure
import requests

from src.endpoints.base_endpoint import BaseEndpoint

class GetMeme(BaseEndpoint):
    @allure.step("Получение мема")
    def get_meme(self, post_id):
        url = f"{self.url}/{self.endpoint["meme"]}/{post_id}"
        return requests.get(url, headers=self.headers)
