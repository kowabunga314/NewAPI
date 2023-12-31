from fastapi.testclient import TestClient
from main import app

from core.test.test_utils import authenticate


client = TestClient(app)
user = None


class ProductTest():
    def __init__(self):
        self.user = authenticate()


print('Beginning tests...')


def test_get_product():
    response = client.get('/api/products')
    print(response.__dir__())

    assert response.status_code == 200


def test_create_product():
    response = client.post('/api/products')

    assert response.status_code == 200
    # assert response.json()
