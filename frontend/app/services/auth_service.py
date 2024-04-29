from app.models.user import User
from app.services.my_auth import client, MyAuth
import streamlit as st

BASE_URL = "http://0.0.0.0:8000"


class AuthService:
    @staticmethod
    def get_or_create_user(username: str, token: str) -> User:
        client.auth = MyAuth(st.session_state["token"]["id_token"])
        url = f"{BASE_URL}/user"
        response = client.post(url)
        response.raise_for_status()
        user = User(**response.json())
        return user
