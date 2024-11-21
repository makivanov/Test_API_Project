import allure
import requests

from check_status import CheckStatus
from endpoints.base_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint, CheckStatus):
    @allure.step("Получение мема")
    def get_meme(self, meme_id: int = None):
        self.meme_id = meme_id
        url = f"{self.url}/{self.endpoint['meme']}/{self.meme_id}"
        self.response = requests.get(url, headers=self.headers)
        return self.response

    @allure.step("Проверка что мем отсутствует")
    def check_missing(self, meme_id: int = None):
        if meme_id:
            self.meme_id = meme_id
        self.get_meme(meme_id=self.meme_id)
        self.check_that_status_is_404()
