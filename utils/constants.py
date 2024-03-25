from dataclasses import dataclass
import os
from dotenv import load_dotenv
from utils.resource import path

dotenv_path = path('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Urls:
    DOMAIN_URL = 'https://reqres.in/api'
    USER_URL = DOMAIN_URL + '/users'
    REGISTER = DOMAIN_URL + '/register'
    SINGLE_RESOURCE = DOMAIN_URL + '/unknown'


@dataclass
class User:
    name: str
    job: str
    email: str
    password: str
    id: int
    token: str = ''


test_user = User(name="test", job="tester", email="test@test.ru", password="toster", id=11)
test_user_registered = User(
    name="test",
    job="tester",
    email=os.getenv("EMAIL_REGISTER_USER"),
    password=os.getenv("PASSWORD_REGISTER_USER"),
    id=int(os.getenv("ID_REGISTERED_USER")),
    token=os.getenv("TOKEN_REGISTERED_USER"))


test_data_with_answer = {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    }