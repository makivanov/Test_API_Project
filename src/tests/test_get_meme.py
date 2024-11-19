import allure
import pytest

from test_data.meme_test_data import one_meme_test_data, incorrect_id_test_data


@allure.step("Тест получения мема")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_get_meme_positive(test_data, create_meme, get_meme):
    create_meme.add_meme(payload=test_data)
    get_meme.get_meme(meme_id=create_meme.meme_id)
    get_meme.check_that_status_is_200()
    get_meme.check_upload_data(payload=test_data)

@allure.step("Тест получения мема с некорректным id")
@pytest.mark.parametrize("test_data", incorrect_id_test_data)
def test_get_meme_incorrect_id(test_data, create_meme, get_meme):
    create_meme.add_meme(payload=test_data)
    get_meme.get_meme(meme_id=create_meme.meme_id)
    get_meme.check_that_status_is_404()


@allure.step("Тест получения мема не авторорм")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_get_meme_difference_author(test_data, create_meme, get_meme):
    create_meme.add_meme(payload=test_data)
    get_meme.set_new_name_and_token()
    get_meme.get_meme(meme_id=create_meme.meme_id)
    get_meme.check_that_status_is_200()
    get_meme.check_upload_data(payload=test_data)


@allure.step("Тест получения мема без авторизации")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_get_meme_without_authorization(test_data, create_meme, get_meme):
    create_meme.add_meme(payload=test_data)
    get_meme.deleted_authorization()
    get_meme.get_meme(meme_id=create_meme.meme_id)
    get_meme.check_that_status_is_401()


@allure.step("Тест получения мема со случайным токеном")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_get_meme_with_random_token(test_data, create_meme, get_meme):
    create_meme.add_meme(payload=test_data)
    get_meme.set_randon_token()
    get_meme.get_meme(meme_id=create_meme.meme_id)
    get_meme.check_that_status_is_401()

@allure.step("Тест получения мема с несуществующим id")
@pytest.mark.parametrize("test_data", one_meme_test_data)
def test_get_meme_with_nonexistent_id(test_data, create_meme, delete_meme, get_meme):
    create_meme.add_meme(payload=test_data)
    delete_meme.delete_meme(meme_id=create_meme.meme_id)
    get_meme.get_meme(meme_id=create_meme.meme_id)
    get_meme.check_that_status_is_404()