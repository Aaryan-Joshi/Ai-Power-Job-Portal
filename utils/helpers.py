import streamlit as st

def login_required(role=None):
    if "user" not in st.session_state:
        st.warning("Please login first.")
        st.stop()

    if role and st.session_state["user"]["role"] != role:
        st.error("Unauthorized access")
        st.stop()
