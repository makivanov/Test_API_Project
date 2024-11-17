import allure

from src.check_status import CheckStatus
from src.settings import BASE_URL


class BaseEndpoint(CheckStatus):
    def __init__(self, url:str=BASE_URL):
        super().__init__()
        self.token = None
        self.user = None
        self.url = url
        self.endpoint = {
            "authorize": "authorize",
            "meme": "meme"
        }
        self.headers = {'Content-type': 'application/json'}
