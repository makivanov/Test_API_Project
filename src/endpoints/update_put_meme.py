import requests

from check_status import CheckStatus
from endpoints.base_endpoint import BaseEndpoint


class PutMeme(BaseEndpoint, CheckStatus):
    def update_put_meme(self, meme_id: int, payload: dict):
        self.meme_id = meme_id
        payload["id"] = self.meme_id
        url = f"{self.url}/{self.endpoint['meme']}/{self.meme_id}"
        self.response = requests.put(url, json=payload, headers=self.headers)
        del payload["id"]
        return self.response
