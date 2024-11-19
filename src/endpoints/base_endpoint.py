import json
import logging
import string
import random

import logger

import allure
import requests

from check_status import CheckStatus
from settings import BASE_URL
from test_data.authorization_test_data import AUTHORIZATION_NAME


class BaseEndpoint(CheckStatus):
    def __init__(self, url: str = BASE_URL, token: str = None):
        super().__init__()
        self.token = token
        self.user = None
        self.meme_id = None
        self.url = url
        self.endpoint = {
            "authorize": "authorize",
            "meme": "meme"
        }
        self.headers = {'Content-type': 'application/json'}
        if self.token is not None:
            self.headers["Authorization"] = self.token
        self.logger = logging.getLogger(__name__)

    def set_randon_token(self):
        characters = string.ascii_letters + string.digits
        token = ''.join(random.choices(characters, k=15))
        self.token = token
        self.headers["Authorization"] = self.token

    def deleted_authorization(self):
        self.headers.pop("Authorization", None)

    def set_new_name_and_token(self):
        while True:
            new_user = random.choice(AUTHORIZATION_NAME)
            if self.user != new_user:
                self.user = new_user
                url = f"{self.url}/{self.endpoint['authorize']}"
                payload = {"name": self.user}
                response = requests.post(url, json=payload, headers=self.headers)
                self.token = response.json()["token"]
                self.headers["Authorization"] = self.token
                break


    def check_2_dict(self, payload: dict, response_json: dict):
        response_keys_set = set(response_json.keys())
        payload_keys_set = set(payload.keys())
        keys = list(payload_keys_set & response_keys_set)
        for key in keys:
            assert response_json[key] == payload[key]

    @allure.step("Проверка что данные в ответе сервера верны")
    def check_returned_data(self, payload: dict):
        try:
            response_json = self.response.json()
        except json.decoder.JSONDecodeError as e:
            logger.error(e)
            raise
        self.check_2_dict(payload, response_json)

    @allure.step("Проверка что с сервера получены корректные данные")
    def check_upload_data(self, payload: dict):
        url = f"{self.url}/{self.endpoint["meme"]}/{self.meme_id}"
        response = requests.get(url, headers=self.headers)
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError as e:
            logger.error(e)
            raise
        self.check_2_dict(payload, response_json)
