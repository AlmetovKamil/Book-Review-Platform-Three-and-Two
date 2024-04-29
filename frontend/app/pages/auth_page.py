from app.services.auth_service import AuthService
import streamlit as st
from streamlit_oauth import OAuth2Component
import os
import base64
import json
from dotenv import load_dotenv

load_dotenv()

# create an OAuth2Component instance
CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"


def decode_email(id_token):
    # verify the signature is an optional step for security
    payload = id_token.split(".")[1]
    # add padding to the payload if needed
    payload += "=" * (-len(payload) % 4)
    payload = json.loads(base64.b64decode(payload))
    email = payload["email"]
    print(f"Payload: {payload}")
    return email


if "auth" not in st.session_state:
    # create a button to start the OAuth2 flow
    oauth2 = OAuth2Component(
        CLIENT_ID,
        CLIENT_SECRET,
        AUTHORIZE_ENDPOINT,
        TOKEN_ENDPOINT,
        TOKEN_ENDPOINT,
        REVOKE_ENDPOINT,
    )
    result = oauth2.authorize_button(
        name="Continue with Google",
        icon="https://www.google.com.tw/favicon.ico",
        redirect_uri="http://localhost:8501/auth/",
        scope="openid email",
        key="google",
        extras_params={"prompt": "consent", "access_type": "offline"},
        use_container_width=True,
        pkce="S256",
    )

    if result:
        st.write(result)
        # decode the id_token jwt and get the user's email address
        id_token = result["token"]["id_token"]
        email = decode_email(id_token)
        st.session_state["auth"] = email
        st.session_state["token"] = result["token"]
        user = AuthService.get_or_create_user(
            email, st.session_state["token"]["id_token"]
        )

        st.session_state["user"] = user
        st.rerun()
else:
    st.switch_page("main.py")
