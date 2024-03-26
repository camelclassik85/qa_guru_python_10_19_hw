from jsonschema import validate
import requests
import json
from utils.constants import Urls, test_user_registered, test_user
from utils.resource import path


def test_schema_validation_get_users():
    response = requests.get(url=Urls.USER_URL)
    schema = json.loads(open(path("schema/list_of_users.json")).read())

    validate(response.json(), schema)


def test_schema_get_validation_single_user():
    response = requests.get(url=Urls.USER_URL, params={"id": test_user_registered.id})
    schema = json.loads(open(path("schema/single_user.json")).read())

    validate(response.json(), schema)


def test_schema_validation_get_list_of_resources():
    response = requests.get(url=Urls.SINGLE_RESOURCE)
    schema = json.loads(open(path("schema/list_of_resources.json")).read())

    validate(response.json(), schema)


def test_schema_validation_get_single_resource():
    response = requests.get(url=Urls.SINGLE_RESOURCE + '/4')
    schema = json.loads(open(path("schema/single_resource.json")).read())

    validate(response.json(), schema)


def test_create_user():
    payload = {
        "name": test_user.name,
        "job": test_user.job
    }

    response = requests.post(url=Urls.USER_URL, json=payload)
    schema = json.loads(open(path("schema/created_user.json")).read())

    validate(response.json(), schema)
