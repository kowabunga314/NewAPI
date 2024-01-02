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

data = {
    'grant_type': '',
    'username': email,
    'password': password,
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

    assert response.status_code == 200
    logger.info(f'{response.json()}')

    # # Expected response payload
    # {
    #     "name":"string",
    #     "description":"string",
    #     "profit_margin":0.45,
    #     "sku":"string",
    #     "id":11,
    #     "material_costs":[
    #         {
    #             "name":"mc1",
    #             "description":"Test material cost 1",
    #             "cost":1.0,
    #             "url":"https://example.com/",
    #             "type":"string",
    #             "id":1
    #         }
    #     ]
    # }
    # assert response.json()
