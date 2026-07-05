from pypdf import PdfReader
from typing import Union, Tuple

MAX_FILE_SIZE_BYTES = 200 * 1024  # 200KB

def validate_pdf(resume_file) -> Tuple[bool, Union[str, None]]:
    """
    Validates the uploaded file and extracts its text.
    Returns: (is_valid, text_content_or_none)
    """
    if resume_file is None:
        return False, ("❌ Please upload your resume to proceed.")
        
    if resume_file.type != "application/pdf":
        return False, ("❌ Please upload a valid PDF resume to proceed.")  
        
    if resume_file.size > MAX_FILE_SIZE_BYTES:
        return False, ("❌ Please upload a resume file smaller than 200KB to proceed.")

    try:
        reader = PdfReader(resume_file)
        raw_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"
        
        if not raw_text.strip():

            return False, ("❌ The PDF appears to be empty or unreadable.")
            
        return True, raw_text      
    except Exception as e:
        return False, ("❌ Failed to parse PDF: {str(e)}")


def validate_job_description(job_skills: str) -> Tuple[bool, Union[str, None]]:
    """
    Validates the job skills input string.
    Returns: (is_valid, cleaned_skills_string_or_none)
    """
    if not job_skills or not job_skills.strip():
        return False, ("❌ Please enter the required skills to proceed.")
        
    return True, job_skills.strip()