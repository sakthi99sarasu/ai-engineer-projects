from skill_extract import resume_text
from ai_analyzer import resume_ai_analyzer
from ats_score_calculator import calculate_ats_score
import streamlit as st

# method is for analyzing the resume and job description skills
def analyze_resume(resume_data):
    user_input= resume_data["resume_text"].lower().replace("\n", " ").strip()
    job_skills = resume_data["job_skills"]
    user_input_data = {"job_skills": job_skills, "resume_text": user_input}
    # ai_result = resume_ai_analyzer(user_input_data)
    ats_data = calculate_ats_score(user_input_data, ai_result)
    return ats_data

