import allure
import pytest

from test_data.authorization_test_data import name_positive, name_negative


@allure.step("Тест авторизации с корректными данными")
@pytest.mark.parametrize("name", name_positive)
def test_authorization_positive(authorization, name):
    authorization.get_token(name)
    authorization.check_that_status_is_200()

@allure.step("Тест авторизации с некорректными данными")
@pytest.mark.parametrize("name", name_negative)
def test_authorization_negative(authorization, name):
    authorization.get_token(name)
    authorization.check_that_status_is_400()

@allure.step("Тест авторизации без данных")
def test_authorization_without_name(authorization):
    authorization.get_token()
    authorization.check_that_status_is_400()
