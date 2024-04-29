import streamlit as st


def sidebar_user_info():
    st.sidebar.title("User")
    st.sidebar.write(st.session_state["user"].username)
    if st.sidebar.button("Logout"):
        del st.session_state["auth"]
        del st.session_state["token"]
        del st.session_state["user"]
        st.rerun()
