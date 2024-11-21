import allure
import requests

from check_status import CheckStatus
from endpoints.base_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint, CheckStatus):
    @allure.step("Получение мема")
    def get_meme(self, meme_id):
        self.meme_id = meme_id
        url = f"{self.url}/{self.endpoint['meme']}/{self.meme_id}"
        self.response = requests.get(url, headers=self.headers)
        return self.response
