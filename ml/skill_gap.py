def extract_skills(text: str, skill_list: list):
    found_skills = set()
    text = text.lower()
    for skill in skill_list:
        if skill.lower() in text:
            found_skills.add(skill)
    return found_skills


def skill_gap_analysis(job_desc_text: str, resume_text: str, skill_list: list):
    jd_skills = extract_skills(job_desc_text, skill_list)
    resume_skills = extract_skills(resume_text, skill_list)

    missing_skills = jd_skills - resume_skills

    return {
        "matched_skills": list(resume_skills),
        "missing_skills": list(missing_skills)
    }
