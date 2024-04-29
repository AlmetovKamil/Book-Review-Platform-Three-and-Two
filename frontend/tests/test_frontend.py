import datetime

import jwt
from streamlit.testing.v1 import AppTest

from app.models.user import User


def create_access_token(payload):
    secret_key = "test_secret_key"
    algorithm = "HS256"

    access_token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return access_token


test_username = "test_user@gmail.com"
test_token = create_access_token({"username": test_username})

test_user = User(username=test_username, created_at=datetime.datetime.today())
at = AppTest.from_file("../app/main.py", default_timeout=5)
at.session_state["user"] = test_user
at.session_state["token"] = {"id_token": test_token}
at.run()


def test_selected_book():
    at.button(key="10000").run()

    assert at.title != "Book Review Platform (BRP)"
