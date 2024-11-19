import random

import allure
import pytest

from endpoints.add_meme import AddMeme
from endpoints.autorization import Authorization
from endpoints.delete_meme import DeleteMeme
from endpoints.get_one_meme import GetMeme
from endpoints.update_put_meme import PutMeme
from test_data.authorization_test_data import AUTHORIZATION_NAME


@pytest.fixture(scope="session")
def authorization(names=AUTHORIZATION_NAME):
    name = random.choice(names)
    return Authorization(name)


@pytest.fixture()
def token(authorization):
    return authorization.get_token()


@pytest.fixture()
def create_meme(token):
    meme = AddMeme(token=token)
    yield meme
    meme_for_delete = DeleteMeme(token=token)
    if meme.meme_id:
        meme_for_delete.delete_meme(meme.meme_id)


@pytest.fixture()
def get_meme(token):
    meme = GetMeme(token=token)
    yield meme
    meme_for_delete = DeleteMeme(token=token)
    if meme.meme_id:
        meme_for_delete.delete_meme(meme.meme_id)


@pytest.fixture()
def change_meme(token):
    meme = PutMeme(token=token)
    yield meme
    meme_for_delete = DeleteMeme(token=token)
    if meme.meme_id:
        meme_for_delete.delete_meme(meme.meme_id)


@pytest.fixture()
def delete_meme(token):
    meme = DeleteMeme(token=token)
    yield meme
    if meme.meme_id:
        meme.delete_meme(meme.meme_id)
