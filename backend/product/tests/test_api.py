from datetime import timedelta
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
import json
import logging

from core.security import create_access_token
from core.test.test_utils import TestUtility
from database.session import SessionLocal
from main import app
from product.schema import MaterialCostById, MaterialCostOutJSON, ProductCreate, ProductOut, ProductOutJSON


logger = logging.getLogger('abacus.product.tests')
client = TestClient(app)
utility = TestUtility()


def test_get_product():
    response = client.get('/api/products', headers={'Authorization': utility.get_auth_header()})
    
    assert response.status_code == 200


def test_create_product():
    product_create = ProductCreate(
        name="TestProduct1",
        description="This is a test product.",
        profit_margin=0.45,
        sku="TP001",
        material_costs=[],
    )
    logger.info(f'Creating product with data: {product_create.model_dump()}')

    response = client.post(
        '/api/products',
        headers={
            'accept': 'application/json',
            'Authorization': utility.get_auth_header(),
            'Content-Type': 'application/json'
        },
        json=product_create.model_dump()
    )

    assert response.status_code == 200

    product_out = ProductOut(**product_create.model_dump(), id=response.json()['id'])
    assert response.json() == product_out.model_dump()


def test_create_product_with_material_costs():
    from product.crud import material_cost

    try:
        mc = material_cost.get_any(db=SessionLocal())
    except LookupError as e:
        logger.warn(f'Got error fetching MaterialCost: {e}')
        return
    except:
        raise

    product_create = ProductCreate(
        name="TestProduct1",
        description="This is a test product.",
        profit_margin=0.45,
        sku="TP001",
        material_costs=[MaterialCostById(id=mc.id)],
    )

    response = client.post(
        '/api/products',
        headers={
            'accept': 'application/json',
            'Authorization': utility.get_auth_header(),
            'Content-Type': 'application/json'
        },
        json=product_create.model_dump()
    )

    assert response.status_code == 200

    product_out = ProductOut(**product_create.model_dump(), id=response.json()['id'])
    product_out.material_costs = [MaterialCostOutJSON(**mc.__dict__)]
    assert response.json() == product_out.model_dump()
