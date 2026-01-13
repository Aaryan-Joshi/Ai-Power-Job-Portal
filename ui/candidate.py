import streamlit as st
import os

def candidate_dashboard():
    st.header("📄 Candidate Resume Upload")

    uploaded_file = st.file_uploader(
        "Upload your resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:
        os.makedirs("data/resumes", exist_ok=True)
        file_path = f"data/resumes/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("✅ Resume uploaded successfully!")
        st.write("Filename:", uploaded_file.name)
