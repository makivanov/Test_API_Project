import allure
import requests

from src.endpoints.base_endpoint import BaseEndpoint


class Authorization(BaseEndpoint):
    @allure.step("Получение токена")
    def get_token(self, name:str):
        url = f"{self.url}/{self.endpoint["authorize"]}"
        payload = {
            "name": name
        }
        response = requests.get(url, json=payload, headers=self.headers)
        self.user = response.json()["user"]
        self.token = response.json()["token"]
        self.headers["Authorization"] = self.token
        return self.token

    @allure.step("Проверка актуальности токена")
    def check_token(self):
        url = f"{self.url}/{self.endpoint["authorize"]}/{self.token}"
        response = requests.get(url, headers=self.headers)
        try:
            if "Token is alive" in response.text:
                return True
        except:
            pass
        finally:
            self.headers.pop("Authorization", None)
            return False
