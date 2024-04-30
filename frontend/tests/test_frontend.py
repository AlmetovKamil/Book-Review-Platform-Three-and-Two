import datetime
import json
from unittest.mock import patch

from app.services.books_service import BASE_URL, BooksService
import jwt
from streamlit.testing.v1 import AppTest

from app.models.user import User
from app.models.book import Book
from tests.sample_books import sample_books_json
import httpx
from app.widgets.sidebar_user_info import sidebar_user_info


def create_access_token(payload):
    secret_key = "test_secret_key"
    algorithm = "HS256"

    access_token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return access_token


test_username = "test_user@gmail.com"
test_token = create_access_token({"username": test_username})

test_user = User(username=test_username, created_at=datetime.datetime.today())
books = [Book(**json_book) for json_book in sample_books_json]


@patch("streamlit.session_state")
@patch("httpx.Client.get")
def test_get_favorites(get, session_state):
    session_state["token"] = {"id_token": "mock"}
    get.return_value = httpx.Response(200, json=sample_books_json)
    assert BooksService.get_favorites() == books


@patch("streamlit.session_state")
@patch("httpx.Client.post")
def test_add_review(post, session_state):
    session_state["token"] = {"id_token": "mock"}
    BooksService.add_review("book_id", "review", 3)
    post.assert_called_once_with(
        f"{BASE_URL}/book/review",
        params={"book_id": "book_id", "review": "review", "rating": 3},
    )


@patch("streamlit.session_state")
@patch("httpx.Client.post")
def test_add_to_favorites(post, session_state):
    session_state["token"] = {"id_token": "mock"}
    BooksService.add_to_favorites("book_id")
    post.assert_called_once_with(
        f"{BASE_URL}/user/books",
        data=json.dumps(["book_id"]),
    )


def test_sidebar_user_info():
    at = AppTest.from_function(sidebar_user_info)
    at.session_state["user"] = test_user
    at.session_state["auth"] = ""
    at.session_state["token"] = ""
    at.run()
    assert at.title[0].value == "User"
    assert at.markdown[0].value == test_user.username

    at.button[0].click().run()
    assert "user" not in at.session_state
    assert "auth" not in at.session_state
    assert "token" not in at.session_state


@patch("app.services.books_service.BooksService.search_books")
def test_main_page(search_books):
    search_books.return_value = books
    at = AppTest.from_file("../app/main.py", default_timeout=5)
    at.session_state["user"] = test_user
    at.session_state["token"] = {"id_token": test_token}
    at.session_state["books"] = books
    at.session_state["selected_book"] = books[0]
    at.run()
    assert at.header[0].value == "Books"
    for i in range(len(books)):
        assert at.subheader[i].value == books[i].title


@patch("streamlit.switch_page")
@patch("streamlit.sidebar.page_link")
@patch("app.services.books_service.BooksService.get_by_id")
def test_selected_book(get_by_id, page_link, switch_page):
    get_by_id.return_value = books[0]
    page_link.return_value = ""
    switch_page.return_value = ""
    at = AppTest.from_file("../app/pages/book_page.py", default_timeout=5)
    at.session_state["user"] = test_user
    at.session_state["token"] = {"id_token": test_token}
    at.session_state["books"] = books
    at.session_state["selected_book"] = books[0]
    at.run()
    assert at.title[0].value == at.session_state["books"][0].title
