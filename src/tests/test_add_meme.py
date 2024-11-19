import allure
import pytest

from test_data.meme_test_data import meme_positive_test_data, meme_negative_test_data, \
    one_meme_test_data


@allure.step("Тест создания мема с корректными данными")
@pytest.mark.parametrize("test_data", meme_positive_test_data)
def test_add_meme_positive(test_data, create_meme):
    create_meme.add_meme(payload=test_data)
    create_meme.check_that_status_is_200()
    create_meme.check_returned_data(payload=test_data)
    create_meme.check_upload_data(payload=test_data)


@allure.step("Тест создания мема с некорректными данными")
@pytest.mark.parametrize("test_data", meme_negative_test_data)
def test_add_meme_negative(test_data, create_meme):
    create_meme.add_meme(payload=test_data)
    create_meme.check_that_status_is_400()


@allure.step("Тест создания мема без авторизации")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_add_meme_without_authorization(test_data, create_meme):
    create_meme.deleted_authorization()
    create_meme.add_meme(payload=test_data)
    create_meme.check_that_status_is_401()


@allure.step("Тест создания мема со случайным токеном")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_add_meme_with_random_token(test_data, create_meme):
    create_meme.set_randon_token()
    create_meme.add_meme(payload=test_data)
    create_meme.check_that_status_is_401()
