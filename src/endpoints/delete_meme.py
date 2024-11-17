import requests

from src.endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    def delete_meme(self, meme_id):
        url = f"{self.url}/{self.endpoint["meme"]}/{meme_id}"
        return requests.delete(url, headers=self.headers)