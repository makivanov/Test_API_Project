import allure
import pytest

from endpoints.autorization import Authorization
from test_data.authorization_test_data import name_positive, name_negative


@allure.feature("Тесты для авторизации")
@allure.step("Тест авторизации с корректными данными")
@allure.title("Тест авторизации с корректными данными")
@pytest.mark.parametrize("name", name_positive)
def test_authorization_positive(name):
    auth = Authorization(name=name)
    auth.get_token()
    auth.check_that_status_is_200()
    del auth


@allure.step("Тест авторизации с некорректными данными")
@allure.title("Тест авторизации с некорректными данными")
@pytest.mark.parametrize("name", name_negative)
def test_authorization_negative(name):
    auth = Authorization(name=name)
    auth.get_token()
    auth.check_that_status_is_400()
    del auth


@allure.step("Тест авторизации без данных")
@allure.title("Тест авторизации без данных")
def test_authorization_without_name():
    auth = Authorization()
    auth.get_token()
    auth.check_that_status_is_400()
    del auth
