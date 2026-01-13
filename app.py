import streamlit as st
from utils.auth import login_user, register_user
from database.db import init_db
from ui.recruiter import recruiter_dashboard
from ui.candidate import candidate_dashboard

init_db()

st.set_page_config(page_title="AI Job Portal", layout="wide")
st.title("🤖 AI-Powered Job Portal")

if "user" not in st.session_state:
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state["user"] = {
                    "id": user[0],
                    "role": user[1]
                }
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        role = st.selectbox("Role", ["candidate", "recruiter"])

        if st.button("Register"):
            if register_user(new_user, new_pass, role):
                st.success("User registered successfully")
            else:
                st.error("Username already exists")

else:
    st.sidebar.success(
        f"Logged in as {st.session_state['user']['role']}"
    )

    if st.sidebar.button("Logout"):
        del st.session_state["user"]
        st.rerun()

    if st.session_state["user"]["role"] == "candidate":
        candidate_dashboard()
    else:
        recruiter_dashboard()
