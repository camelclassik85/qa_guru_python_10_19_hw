import requests
from utils.constants import Urls, test_user_registered, test_user


def test_get_user_success():
    response = requests.get(Urls.USER_URL + f"/{test_user_registered.id}")

    assert response.status_code == 200


def test_create_user_success():
    payload = {
        "name": test_user.name,
        "job": test_user.job
    }

    response = requests.post(url=Urls.USER_URL, json=payload)

    assert response.status_code == 201


def test_delete_user_success():
    response = requests.delete(url=Urls.USER_URL + f"/{test_user_registered.id}")

    assert response.status_code == 204


def test_user_not_found():
    response = requests.get(url=Urls.USER_URL + "/13")

    assert response.status_code == 404


def test_bad_request():
    payload = {
        "email": test_user_registered.email
    }

    response = requests.post(url=Urls.REGISTER, json=payload)

    assert response.status_code == 400
