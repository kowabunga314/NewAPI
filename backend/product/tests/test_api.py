from datetime import timedelta
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
import json
from main import app

from core.security import create_access_token
from core.test.test_utils import authenticate


client = TestClient(app)
email = 'a@b.c'
password = 'password'


# class ProductTest():
#     def __init__(self):
#         access_token = create_access_token(1)
#         self.access_token = access_token
#         self.token_type = 'Bearer'

#     def get_auth_header(self):
#         return f'Authorization: {self.token_type.capitalize()} {self.access_token}'


# print('Beginning tests...')
# user = ProductTest()


def test_user():
    return {"email": "a@b.c", "password": "password"}
user = OAuth2PasswordRequestForm(username=email, password=password)
data = {
    'grant_type': '',
    'username': 'a@b.c',
    'password': 'password',
    'scope': '',
    'client_id': '',
    'client_secret': '',
}

def test_login():
  response = client.post("/api/login/access-token", data=data)
  assert response.status_code == 200
  token = response.json()["access_token"]
  assert token is not None
  return token
token = test_login()
auth_header = f'Bearer {token}'


def test_get_product():
    print(f'Using auth header: {auth_header}')
    response = client.get('/api/products', headers={'Authorization': auth_header})
    print(response.__dir__())

    assert response.status_code == 200


def test_create_product():
    payload = {
    'name': 'string',
    'description': 'string',
    'profit_margin': 0.45,
    'sku': 'string',
    'material_costs': [
        {
            'id': 0,
        },
    ],
}
    response = client.post('/api/products', headers={'Authorization': auth_header}, data=payload)

    assert response.status_code == 200
    # assert response.json()
