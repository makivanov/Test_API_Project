import allure
import pytest

from test_data.meme_test_data import one_meme_test_data


@allure.step("Тест удаление мема пользователем, который его создал")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
def test_delete_meme_positive(create_meme, delete_meme, create_test_data):
    create_meme.add_meme(payload=create_test_data)
    delete_meme.delete_meme(meme_id=create_meme.meme_id)
    delete_meme.check_that_status_is_200()
    delete_meme.check_missing()


@allure.step("Тест удаление мема не автором")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
def test_delete_meme_no_autor(create_meme, delete_meme, create_test_data):
    create_meme.add_meme(payload=create_test_data)
    delete_meme.set_new_name_and_token()
    delete_meme.delete_meme(meme_id=create_meme.meme_id)
    delete_meme.check_that_status_is_403()
    create_meme.check_upload_data(payload=create_test_data)


@allure.step("Тест удаление мема без авторизации")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
def test_delete_meme_no_autorization(create_meme, delete_meme, create_test_data):
    create_meme.add_meme(payload=create_test_data)
    delete_meme.deleted_authorization()
    delete_meme.delete_meme(meme_id=create_meme.meme_id)
    delete_meme.check_that_status_is_401()
    create_meme.check_upload_data(payload=create_test_data)


@allure.step("Тест удаление мема со случайным токеном")
@pytest.mark.parametrize("create_test_data", one_meme_test_data)
def test_delete_meme_random_token(create_meme, delete_meme, create_test_data):
    create_meme.add_meme(payload=create_test_data)
    delete_meme.deleted_authorization()
    delete_meme.delete_meme(meme_id=create_meme.meme_id)
    delete_meme.check_that_status_is_401()
    create_meme.check_upload_data(payload=create_test_data)
