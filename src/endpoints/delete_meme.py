import allure
import requests

from check_status import CheckStatus
from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_one_meme import GetMeme


class DeleteMeme(BaseEndpoint, CheckStatus):
    @allure.step("Удаление мема")
    def delete_meme(self, meme_id):
        self.meme_id = meme_id
        url = f"{self.url}/{self.endpoint['meme']}/{self.meme_id}"
        self.response = requests.delete(url, headers=self.headers)
        return self.response
