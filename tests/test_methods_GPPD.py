from utils.constants import Urls, test_user, test_user_registered
import requests


def test_get_list_of_users():
    response = requests.get(Urls.USER_URL)

    assert response.json()["page"] == 1
    assert response.status_code == 200


def test_get_2nd_list_of_users():
    response = requests.get(Urls.USER_URL, params={"page": 2})

    assert response.json()["page"] == 2
    assert response.status_code == 200


def test_create_user():
    payload = {
        "name": test_user.name,
        "job": test_user.job
    }

    response = requests.post(url=Urls.USER_URL, json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == test_user.name
    assert response.json()["job"] == test_user.job


def test_register_user():
    payload = {
        "email": test_user_registered.email,
        "password": test_user_registered.password
    }

    response = requests.post(url=Urls.REGISTER, json=payload)

    assert response.status_code == 200
    assert response.json()["id"] == test_user_registered.id
    assert response.json()["token"] == test_user_registered.token


def test_update_user():
    payload = {
        "name": test_user.name,
        "job": test_user.job
    }
    response = requests.put(url=Urls.USER_URL + '/12', json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == test_user.name
    assert response.json()["job"] == test_user.job


def test_delete_user():

    response = requests.delete(url=Urls.USER_URL + '/2')

    assert response.status_code == 204
