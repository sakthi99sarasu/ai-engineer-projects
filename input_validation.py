
from pypdf import PdfReader
import streamlit as st

def validate_pdf(resume_data):
    if resume_data is not None or resume_data: 
        if resume_data.type != "application/pdf" or resume_data.size > 200 * 1024:
            st.write("Please upload valid resume to proceed.")
        extract_data = PdfReader(resume_data)
        raw_text = ""
        for page in extract_data.pages:
            if page.extract_text():
                raw_text += page.extract_text() + "\n"
        st.write("Resume uploaded successfully!")       
    else:
        st.write("Please upload your resume to proceed.")
        raw_text = None
    return raw_text

def validate_job_description(job_skills):
    if job_skills.strip() is None or not job_skills:
        st.write("Please enter the required skills to proceed.")
    else:
        job_skills = job_skills
    return job_skills