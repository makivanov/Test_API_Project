import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_one_meme import GetMeme


class DeleteMeme(BaseEndpoint):
    @allure.step("Удаление мема")
    def delete_meme(self, meme_id):
        self.meme_id = meme_id
        url = f"{self.url}/{self.endpoint["meme"]}/{self.meme_id}"
        self.response = requests.delete(url, headers=self.headers)
        return self.response

    @allure.step("Проверка что мем отсутствует")
    def check_missing(self):
        meme = GetMeme(token=self.token)
        meme.get_meme(meme_id=self.meme_id)
        meme.check_that_status_is_404()