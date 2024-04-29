from typing import List, Optional
from app.models.book import Book
from app.models.review import Review
from app.services.my_auth import client, MyAuth
import streamlit as st


BASE_URL = "http://0.0.0.0:8000"


class BooksService:
    @staticmethod
    def search_books(
        name: Optional[str] = None,
        author: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: int = 1,
        size: int = 16,
    ) -> List[Book]:
        client.auth = MyAuth(st.session_state["token"]["id_token"])
        params = {
            "page": page,
            "size": size,
        }
        if name is not None:
            params["name"] = name
        if author is not None:
            params["author"] = author
        if tags is not None:
            params["tags"] = tags
        response = client.get(
            f"{BASE_URL}/search_books",
            params=params,
        )
        books = []
        for json_book in response.json()["data"]:
            if json_book is None:
                print("NONE!")
            else:
                books.append(Book(**json_book))
        print(books)
        return books

    @staticmethod
    def get_favorites(brief=False):
        client.auth = MyAuth(st.session_state["token"]["id_token"])
        params = {"brief": brief}
        response = client.get(
            f"{BASE_URL}/user/books",
            params=params,
        )
        books = []
        for json_book in response.json():
            if json_book is None:
                print("NONE!")
            else:
                books.append(Book(**json_book))
        print(books)
        return books

    @staticmethod
    def get_by_id(book_id: str):
        client.auth = MyAuth(st.session_state["token"]["id_token"])
        response = client.get(f"{BASE_URL}/book/{book_id}")
        book = Book(**response.json())
        return book

    @staticmethod
    def add_review(book_id: str, review: str, rating: float):
        client.auth = MyAuth(st.session_state["token"]["id_token"])
        client.post(
            f"{BASE_URL}/book/review",
            params={"book_id": book_id, "review": review, "rating": rating},
        )
