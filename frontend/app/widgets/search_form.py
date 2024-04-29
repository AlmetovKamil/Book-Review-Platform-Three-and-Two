import streamlit as st
from app.services.books_service import BooksService


def search_books(append=False):
    books = BooksService.search_books(
        st.session_state["book_title"]
        if len(st.session_state["book_title"]) > 0
        else None,
        st.session_state["book_author"]
        if len(st.session_state["book_author"]) > 0
        else None,
        st.session_state["book_tags"].split(",")
        if len(st.session_state["book_tags"]) > 0
        else None,
        st.session_state["page_number"],
    )
    if append:
        st.session_state["books"] += books
    else:
        st.session_state["books"] = books


def search_form():
    with st.sidebar.form("search_form", border=False):
        st.title("Search")
        st.text_input("Name", key="book_title")
        st.text_input("Author", key="book_author")
        st.text_input("Tags", key="book_tags")
        if st.form_submit_button("Search"):
            search_books()
