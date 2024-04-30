def sidebar_user_info():
    import streamlit as st

    st.sidebar.title("User")
    st.sidebar.write(st.session_state["user"].username)
    # st.sidebar.write(st.session_state["token"]["id_token"])
    if st.sidebar.button("Logout"):
        del st.session_state["auth"]
        del st.session_state["token"]
        del st.session_state["user"]
        st.rerun()
