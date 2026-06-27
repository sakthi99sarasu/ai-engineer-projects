import pdfplumber

with pdfplumber.open("resumes/Sivasakthi_strong_ATS_Resume.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        resume_text = text.lower()
    