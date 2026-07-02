import time
import requests
import streamlit as st
from pypdf import PdfReader
from app import analyze_resume
from input_validation import validate_pdf, validate_job_description

st.title("Upload the resume here!!!!")
# for initializing the form submission state
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
# for disabling the button after submission
disable_inputs = st.session_state.form_submitted
# Render input elements (they lock automatically when disable_inputs is True)
resume = st.file_uploader("Upload your resume", type=["pdf", "docx"],  disabled=disable_inputs)
job_skills = st.text_area("Enter the required skills:", value=" ", height="content", max_chars=500, help="None", label_visibility="visible", width="stretch",  disabled=disable_inputs)
button_placeholder = st.empty()  # Placeholder for the button
#  Handle the button visibility state
if not st.session_state.form_submitted:
    if button_placeholder.button("Analyze Resume"):
        st.session_state.form_submitted = True
        st.rerun()
#  Execute the API task, show the spinner, and display results
if st.session_state.form_submitted:
    button_placeholder.empty() 
    if resume is not None and len(job_skills.strip()) > 0:
        resume_data = validate_pdf(resume)
        job_skill_data_raw = validate_job_description(job_skills)
        job_skill_data = {item.strip().lower() for item in job_skill_data_raw.split(",")}
        values = {"resume_text": resume_data, "job_skills": job_skill_data}
        with st.spinner("\U000023F3Analyzing the resume..."):
            try:
                time.sleep(3)
                outputs = analyze_resume(values)

                # Using the unicode method cleanly inside your loop
                score = round(outputs["ats_score"], 2)
                missed_skills = "\n\n".join(f"\u274C {skill.title()}" for skill in  outputs["missed_skills"])
                candidate_skills = "\n\n".join(f"\u2714 {skill.title()}" for skill in  outputs["candidate_skills"])
                # Construct the formatted string
                recommendations = ""
                for priority, recs in outputs['recommendations'].items():
                    recommendations += f"{priority}\n\n"
                    for rec in recs:
                        recommendations += f"- {rec}\n\n"
                    # Add an extra newline between sections (except the last one)
                    recommendations += "\n"
                st.markdown(":material/check_circle: ATS Score: \n")
                st.markdown(f"{score}%" )
                st.progress(min(score, 1.0))
                st.text_area(":material/edit: Candidate Skills", value= candidate_skills, disabled=True, height="content", label_visibility="visible", width="stretch", bind=None)
                st.text_area(":material/edit: Missed Skills", value= missed_skills, disabled=True, height="content", label_visibility="visible", width="stretch", bind=None)
                st.markdown(":material/check_circle: Recommendations")
                st.text_area("", value=recommendations.title(), disabled=False, height="content", label_visibility="collapsed", width="stretch", bind=None)
            except requests.exceptions.RequestException as e:
                st.error(f"API Connection Failed: {e}")
    else:
    # Show an error on the screen if they clicked button without a file
        st.error("Please upload a resume file and job skills!")
