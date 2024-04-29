import httpx
from app.models.user import User

BASE_URL = "http://0.0.0.0:8000"


class MyAuth(httpx.Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = self.token
        yield request


class AuthService:
    @staticmethod
    def get_or_create_user(username: str, token: str) -> User:
        url = f"{BASE_URL}/user"
        with httpx.Client(auth=MyAuth(token)) as client:
            response = client.post(url)
            response.raise_for_status()
            user = User(**response.json())
            return user
