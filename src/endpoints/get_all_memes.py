import allure
import requests

from src.endpoints.base_endpoint import BaseEndpoint


class GetAllMemes(BaseEndpoint):
    @allure.step("Получение всех мемов")
    def get_all_memes(self):
        url = f"{self.url}/{self.endpoint["meme"]}"
        return requests.get(url, headers=self.headers)
