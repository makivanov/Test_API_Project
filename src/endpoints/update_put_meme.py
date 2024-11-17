import requests

from src.endpoints.base_endpoint import BaseEndpoint


class PutMeme(BaseEndpoint):
    def update_put_meme(self, meme_id, payload: dict):
        url = f"{self.url}/{self.endpoint["meme"]}/{meme_id}"
        payload["id"] = meme_id
        return requests.put(url, json=payload, headers=self.headers)
