import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAllMemes(BaseEndpoint):
    @allure.step("Получение всех мемов")
    def get_all_memes(self):
        url = f"{self.url}/{self.endpoint['meme']}"
        return requests.get(url, headers=self.headers)
