import streamlit as st
import os
from ml.resume_parser import extract_text_from_pdf
from ml.text_cleaner import clean_text
from ml.matcher import match_resumes
from ml.skill_gap import skill_gap_analysis

SKILLS = [
    "python", "java", "sql", "machine learning",
    "deep learning", "django", "flask",
    "nlp", "data analysis", "html", "css", "javascript"
]

def recruiter_dashboard():
    st.header("🧑‍💼 Recruiter Dashboard")

    jd_file = st.file_uploader(
        "Upload Job Description (PDF)",
        type=["pdf"]
    )

    if jd_file:
        os.makedirs("data/job_descriptions", exist_ok=True)
        jd_path = f"data/job_descriptions/{jd_file.name}"

        with open(jd_path, "wb") as f:
            f.write(jd_file.getbuffer())

        jd_text = clean_text(extract_text_from_pdf(jd_path))

        resumes = []
        resume_dir = "data/resumes"

        if not os.path.exists(resume_dir):
            st.warning("No resumes uploaded yet.")
            return

        for resume_file in os.listdir(resume_dir):
            resume_path = f"{resume_dir}/{resume_file}"
            resume_text = clean_text(
                extract_text_from_pdf(resume_path)
            )
            resumes.append((resume_file, resume_text))

        if st.button("🔍 Match Candidates"):
            results = match_resumes(jd_text, resumes)

            st.subheader("📊 Ranked Candidates")

            for res in results:
                st.markdown(f"### {res['resume']}")
                st.progress(res["score"] / 100)
                st.write(f"Match Score: **{res['score']}%**")

                resume_text = dict(resumes)[res["resume"]]
                gap = skill_gap_analysis(jd_text, resume_text, SKILLS)

                with st.expander("Skill Gap Analysis"):
                    st.write("✅ Matched Skills:", gap["matched_skills"])
                    st.write("❌ Missing Skills:", gap["missing_skills"])
