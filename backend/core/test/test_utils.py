from fastapi.testclient import TestClient
import logging

from main import app


email = 'a@b.c'
password = 'password'
logger = logging.getLogger('abacus.core.test')


class TestUtility():
  
    def __init__(self) -> None:
        self.client = TestClient(app)
        self.data = {
            'grant_type': '',
            'username': email,
            'password': password,
            'scope': '',
            'client_id': '',
            'client_secret': '',
        }
        self.token = self._get_token()

    def _get_token(self):
        response = self.client.post("/api/login/access-token", data=self.data)
        logger.debug(f'Response: {response.json()}')
        assert response.status_code == 200
        token = response.json()["access_token"]
        assert token is not None
        return token

    def get_auth_header(self) -> str:
        return f'Bearer {self.token}'
