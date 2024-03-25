import requests
from utils.constants import Urls, test_data_with_answer


def test_without_answer():
    response = requests.get(url=Urls.SINGLE_RESOURCE + '/23')

    assert response.json() == {}


def test_with_answer():
    response = requests.get(url=Urls.SINGLE_RESOURCE + '/2')

    assert response.json()["data"]["name"] == "fuchsia rose"
    assert response.json()["data"] == test_data_with_answer
    assert (response.json()["support"]["text"] ==
            "To keep ReqRes free, contributions towards server costs are appreciated!")
