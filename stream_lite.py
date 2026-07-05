import time
import requests
import streamlit as st
from pydantic_core import ValidationError

# Assuming analyze_resume is imported correctly from your local app module
from app import analyze_resume 
from input_validation import validate_pdf, validate_job_description

st.title("Resume Analytics Dashboard")

# Initialize persistent Streamlit session states
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
if "analysis_payload" not in st.session_state:
    st.session_state.analysis_payload = {}

disable_inputs = st.session_state.form_submitted

# UI Elements
resume = st.file_uploader("Upload your resume", type=["pdf"], disabled=disable_inputs)
job_skills = st.text_area(
    "Enter the required skills (comma-separated):", 
    value="", 
    max_chars=500, 
    disabled=disable_inputs
)

button_placeholder = st.empty()

# Handle Form Processing
if not st.session_state.form_submitted:
    if button_placeholder.button("Analyze Resume"):
        try:
            # Unpack the fixed validation tuple contracts
            resume_valid, resume_data = validate_pdf(resume)
            job_skill_valid, job_skill_data_raw = validate_job_description(job_skills)

            if resume_valid and job_skill_valid:
                # Clean and parse comma-separated skills into a set
                job_skill_data = {item.strip().lower() for item in job_skill_data_raw.split(",") if item.strip()}
                
                if job_skill_data:
                    # Persist across the upcoming script rerun via session_state
                    st.session_state.analysis_payload = {
                        "resume_text": resume_data, 
                        "job_skills": list(job_skill_data)  # JSON/API friendly list
                    }
                    st.session_state.form_submitted = True
                    st.rerun()
                else:
                    st.error("❌ Please provide at least one valid skill.")
            elif not resume_valid and not job_skill_valid:
                st.error(resume_data)
                st.error(job_skill_data_raw)
            elif not resume_valid:
                st.error(resume_data)
            elif not job_skill_valid:
                st.error(job_skill_data_raw)
        except ValidationError as e:
            st.error(f"Validation Error: {str(e)}")

# Process and Display API results
if st.session_state.form_submitted:
    button_placeholder.empty() 
    
    with st.spinner("⏳ Analyzing the resume..."):
        try:
            # Simulating payload handling or an external API processing lag safely
            # time.sleep(1.5) 
            
            # Fetch the persisted values from the session state
            payload = st.session_state.analysis_payload
            outputs = analyze_resume(payload)

            # Extract and format metrics Safely
            score = round(outputs.get("ats_score", 0), 2)
            # Standardizing display format to individual line-items
            missed_skills = "\n".join(f"❌ {skill.title()}" for skill in outputs.get("missed_skills", []))
            candidate_skills = "\n".join(f"✔️ {skill.title()}" for skill in outputs.get("candidate_skills", []))
            
            # Formulating Markdown Text recommendations efficiently
            recommendations = ""
            for priority, recs in outputs.get('recommendations', {}).items():
                recommendations += f"### {priority.title()}\n"
                for rec in recs:
                    recommendations += f"- {rec}\n"
                recommendations += "\n"

            # Display Outputs
            st.subheader("📊 Assessment Results")
            st.markdown(f"**ATS Match Score:** {score}%")
            
            # Streamlit progress bar expects a float value between 0.0 and 1.0
            st.progress(min(score / 100.0, 1.0))
            
            col1, col2 = st.columns(2)
            with col1:
                st.text_area("Candidate Skills", value=candidate_skills, disabled=True, height=200)
            with col2:
                st.text_area("Missed Skills", value=missed_skills, disabled=True, height=200)
            
            st.markdown("### 💡 Recommendations")
            st.markdown(recommendations)
            
            # Add a reset button to allow users to evaluate another file
            if st.button("Analyze Another Resume"):
                st.session_state.form_submitted = False
                st.session_state.analysis_payload = {}
                st.rerun()

        except requests.exceptions.RequestException as e:
            st.error(f"API Connection Failed: {e}")
            if st.button("Reset Application"):
                st.session_state.form_submitted = False
                st.rerun()  