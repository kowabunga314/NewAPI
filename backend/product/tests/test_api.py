from datetime import timedelta
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
import json
import logging
from main import app

from core.security import create_access_token
from core.test.test_utils import authenticate


logger = logging.getLogger('abacus.product.tests.test_api')
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

def login_utility():
  response = client.post("/api/login/access-token", data=data)
  assert response.status_code == 200
  token = response.json()["access_token"]
  assert token is not None
  return token
token = login_utility()
auth_header = f'Bearer {token}'


def test_get_product():
    response = client.get('/api/products', headers={'Authorization': auth_header})
    
    assert response.status_code == 200


def test_create_product():
    payload = {
        "name": "string",
        "description": "string",
        "profit_margin": 0.45,
        "sku": "string",
        "material_costs": [
            {
            "id": 1
            }
        ]
    }
    
    response = client.post(
        '/api/products',
        headers={
            'accept': 'application/json',
            'Authorization': auth_header,
            'Content-Type': 'application/json'
        },
        json=payload
    )
    print(f'Got response: {response.text}')

    assert response.status_code == 200
    # assert response.json()
