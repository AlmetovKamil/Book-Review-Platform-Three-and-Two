from typing import List, Optional
from app.models.book import Book
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
        size: int = 50,
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
        # print(response.json()["data"])
        books = [Book(**json_book) for json_book in response.json()["data"]]
        print(books)
        return books
