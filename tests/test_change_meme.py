import allure
import pytest

from test_data.meme_test_data import meme_positive_test_data, one_meme_test_data, meme_negative_test_data, \
    one_change_mem_test_data


@allure.feature("Тесты для изменения мема")
@allure.step("Тест изменения мема с корректными данными")
@allure.title("Тест изменения мема с корректными данными")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
@pytest.mark.parametrize("change_test_data", meme_positive_test_data)
def test_change_meme_positive(create_meme, change_meme, create_test_data, change_test_data):
    create_meme.add_meme(payload=create_test_data)
    change_meme.update_put_meme(payload=change_test_data, meme_id=create_meme.meme_id)
    change_meme.check_that_status_is_200()
    create_meme.check_upload_data(payload=change_test_data)


@allure.step("Тест изменения мема с некорректными данными")
@allure.title("Тест изменения мема с некорректными данными")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
@pytest.mark.parametrize("change_test_data", meme_negative_test_data)
def test_change_meme_negative(create_meme, change_meme, create_test_data, change_test_data):
    create_meme.add_meme(payload=create_test_data)
    change_meme.update_put_meme(payload=change_test_data, meme_id=create_meme.meme_id)
    change_meme.check_that_status_is_400()
    create_meme.check_upload_data(payload=create_test_data)


@allure.step("Тест изменения мема без авторизации")
@allure.title("Тест изменения мема без авторизации")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
@pytest.mark.parametrize("change_test_data", one_change_mem_test_data)
def test_change_meme_without_authorization(create_meme, change_meme, create_test_data, change_test_data):
    create_meme.add_meme(payload=create_test_data)
    change_meme.deleted_authorization()
    change_meme.update_put_meme(payload=change_test_data, meme_id=create_meme.meme_id)
    change_meme.check_that_status_is_401()
    create_meme.check_upload_data(payload=create_test_data)


@allure.step("Тест изменения мема со случайным токеном")
@allure.title("Тест изменения мема со случайным токеном")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
@pytest.mark.parametrize("change_test_data", one_change_mem_test_data)
def test_change_meme_with_random_token(create_meme, change_meme, create_test_data, change_test_data):
    create_meme.add_meme(payload=create_test_data)
    change_meme.set_randon_token()
    change_meme.update_put_meme(payload=change_test_data, meme_id=create_meme.meme_id)
    change_meme.check_that_status_is_401()
    create_meme.check_upload_data(payload=create_test_data)


@allure.step("Тест изменения мема пользователем с другим именем")
@allure.title("Тест изменения мема пользователем с другим именем")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
@pytest.mark.parametrize("change_test_data", one_change_mem_test_data)
def test_change_meme_with_different_name(create_meme, change_meme, create_test_data, change_test_data):
    create_meme.add_meme(payload=create_test_data)
    change_meme.set_new_name_and_token()
    change_meme.update_put_meme(payload=change_test_data, meme_id=create_meme.meme_id)
    change_meme.check_that_status_is_403()
    create_meme.check_upload_data(payload=create_test_data)
