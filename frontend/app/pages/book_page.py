from app.widgets.sidebar_user_info import sidebar_user_info
import streamlit as st
from streamlit_star_rating import st_star_rating
from app.models.book import Book


if "user" not in st.session_state:
    st.switch_page("pages/auth_page.py")

if "selected_book" not in st.session_state or \
      st.session_state.selected_book is None:
    st.switch_page("main.py")

sidebar_user_info()
st.sidebar.divider()
st.sidebar.page_link("main.py", label="Home")


book: Book = st.session_state.selected_book
st.title(book.title)
columns = st.columns([1, 5])
with columns[0]:
    st.image(book.cover_image_url, caption=book.author)
with columns[1]:
    st.write(book.description)
    st.divider()
    st.write(f"Author: {book.author}")
    st.write(f"Genre: {book.genre.name}")
    stars = st_star_rating(
        "",
        maxValue=5,
        defaultValue=book.rating,
        key=book.title,
        size=25,
        read_only=True,
    )
