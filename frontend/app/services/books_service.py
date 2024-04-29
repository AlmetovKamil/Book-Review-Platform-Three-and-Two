from typing import List
from app.models.book import Book
from app.services.my_auth import client, MyAuth
import streamlit as st


class BooksService:
    @staticmethod
    def search_books(
        name: str, author: str, tags: List[str], page: int = 1, size: int = 1
    ) -> List[Book]:
        client.auth = MyAuth(st.session_state["token"]["id_token"])
        pass
