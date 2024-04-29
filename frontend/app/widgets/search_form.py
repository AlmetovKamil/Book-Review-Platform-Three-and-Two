import streamlit as st


def search_form():
    with st.sidebar.form("search_form", border=False):
        st.title("Search")
        st.text_input("Name", key="book_name")
        st.text_input("Author", key="book_author")
        st.text_input("Tags", key="book_tags")
        if st.form_submit_button("Search"):
            st.toast(f"Searching {st.session_state['book_name']}, \
                    {st.session_state['book_author']}, \
                        {st.session_state['book_tags']}")
