import requests
from utils.constants import test_user_registered, Urls


def test_positive_register_user():
    payload = {
        "email": test_user_registered.email,
        "password": test_user_registered.password
    }

    response = requests.post(url=Urls.REGISTER, json=payload)

    assert response.status_code == 200
    assert response.json()["id"] == test_user_registered.id
    assert response.json()["token"] == test_user_registered.token


def test_negative_register_user():
    payload = {
        "email": test_user_registered.email
    }

    response = requests.post(url=Urls.REGISTER, json=payload)

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
