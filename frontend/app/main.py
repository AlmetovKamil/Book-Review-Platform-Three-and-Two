# Import necessary libraries
from app.widgets.search_form import search_books, search_form
from app.widgets.sidebar_user_info import sidebar_user_info
from app.services.books_service import BooksService
import streamlit as st


if "user" not in st.session_state:
    st.switch_page("pages/auth_page.py")


st.set_page_config(page_title="BRP", page_icon="📚", layout="wide")
st.session_state.selected_book = None

# Streamlit app layout
st.title("Book Review Platform (BRP)")

# Sidebar widgets
sidebar_user_info()
st.sidebar.divider()
search_form()
if st.sidebar.checkbox("Favorites", key="show_favorites"):
    books = BooksService.get_favorites()
    st.session_state["books"] = books
    st.session_state["favorite"] = True
elif "favorite" in st.session_state:
    del st.session_state["books"]
    del st.session_state["favorite"]
    st.rerun()

if "books" not in st.session_state:
    st.session_state["page_number"] = 1
    st.session_state["books"] = BooksService.search_books(
        "a",
        page=st.session_state["page_number"],
    )
books = st.session_state["books"]


n_columns = 4
# Display filtered book reviews
st.header("Books")
for i, book in enumerate(books):
    if i % n_columns == 0:
        columns = st.columns(n_columns)
    with columns[i % n_columns]:
        # Book Tile
        with st.container(border=True):
            if len(book.cover_link) > 0:
                st.image(
                    book.cover_link,
                    caption=book.author_name,
                    use_column_width=True,
                )
            st.subheader(book.title)
            if st.button("Details", key=i + 10000):
                st.session_state.selected_book = BooksService.get_by_id(
                    book.id
                )
                st.switch_page("pages/book_page.py")
if st.button("Load more"):
    st.session_state["page_number"] += 1
    search_books(append=True)
    st.rerun()
