from app.services.books_service import BooksService
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

st.session_state.selected_book = BooksService.get_by_id(
    st.session_state.selected_book.id
)
book: Book = st.session_state.selected_book
st.title(book.title)
columns = st.columns([1, 5])
with columns[0]:
    st.image(book.cover_link, caption=book.author_name)
with columns[1]:
    st.write(book.description)
    st.divider()
    if book.reviews is not None and len(book.reviews) > 0:
        stars = st_star_rating(
            "",
            maxValue=5,
            defaultValue=book.get_rating(),
            key="stars",
            size=25,
            read_only=True,
        )
    st.write(f"Author: {book.author_name}")
    if st.checkbox("Favorite",
                   value=book.id in BooksService.get_favorites(True)):
        BooksService.add_to_favorites(book.id)
    else:
        BooksService.delete_from_favorites(book.id)
    # st.write(f"Tags: {book.tags}")
    st.subheader("Reviews")
    for i, review in enumerate(book.reviews):
        with st.container(border=True):
            columns = st.columns(2)
            with columns[0]:
                st.write(review.username)
            with columns[1]:
                stars = st_star_rating(
                    "",
                    maxValue=5,
                    defaultValue=review.rating,
                    key=review.username + " review" + str(i),
                    size=25,
                    read_only=True,
                )
            st.write(review.review)

    st.divider()

    with st.form("Leave review", clear_on_submit=True):
        st.text_input("Review text", key="review_text")
        stars = st_star_rating(
            "",
            maxValue=5,
            defaultValue=0,
            key="new review",
            size=25,
        )
        if st.form_submit_button("Submit"):
            BooksService.add_review(book.id,
                                    st.session_state["review_text"], stars)
            st.rerun()
