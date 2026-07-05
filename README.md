## AI Resume ATS Reviewer 
    AI Resume ATS Reviewer is a web application built with Python, Streamlit, and the Google Gemini API that evaluates a candidate's resume against a job description. The application extracts resume content, analyzes skill alignment, calculates an ATS (Applicant Tracking System) compatibility score, identifies missing skills, and generates personalized AI-powered recommendations to improve the resume for better job matching.

## Objective

    To build an AI-powered ATS reviewer that helps job seekers understand how well their resumes match a given job description and provides actionable recommendations for improvement.

## Acknowledgements

    This project was built as part of my journey to learn AI Engineering through hands-on projects using Python, Streamlit, and Google Gemini.

## Version
  ** Current version 1.0 **

## 1. Features

- Extract Resume Text(PDF)
- AI-powered Resume Analysis
- ATS Score Calculation Result
- Skill Gap Analysis
- Personalized Recommendations for the resume
- Error Handling
- Interactive Streamlit UI


## 2. How it works

## Screenshots
![alt text](image/ats_resume_reviewer1.png)
![alt text](image/ats_resume_reviewer2.png)
![alt text](image/ats_resume_reviewer3.png)


Upload Resume

↓

Extract Text

↓

Gemini Analysis

↓

ATS Calculation

↓

Display Result

## 3. Architecture

User
   │
   ▼
Streamlit  --> user interface
   │
   ▼
app.py  -->  Controls the complete workflow
   │
 ├── input_validation.py --> Validates uploaded files and job description
 ├── ai_analyzer.py --> Sends prompt to Gemini and gets structured JSON
 ├── prompts.py --> Holds the prompt that needed for analysing the resume
 └── ats_calculator.py  --> Calculates ATS score using AI response
   │
   ▼
Result

## 4. Tech Stack


- Python

- Streamlit

- Google Gemini API

- PDF Processing (PyPDF)

- python-dotenv

- Git & GitHub

## 5.Folder Structure
```text
resume-ats-reviewer/
│
├── streamlit_app.py
├── app.py
├── ai_analyzer.py
├── ats_calculator.py
├── input_validation.py
├── prompts.py
├── requirements.txt
└── README.md
```

## 6. Installation
```bash
Step by step.

git clone

cd resume-ats-reviewer

pip install -r requirements.txt

streamlit run streamlit_app.py
```

## 7. Environment Variables

Create a .env file

GEMINI_API_KEY=your_api_key

## 8. Learning Outcomes

This project helped me understand the complete lifecycle of building an AI-powered application—from PDF processing and prompt engineering to UI development and error handling.

Through this project, I learned:

- Prompt Engineering

- Modular Python Architecture

- Streamlit Development

- Google Gemini Integration

- Error Handling

- JSON Parsing

- AI-powered Resume Analysis

## 9. Challenges Faced


- Designing a modular Python architecture

- Creating effective prompts for structured JSON responses

- Implementing ATS score calculation using AI output

- Handling PDF parsing and validation

- Building a responsive Streamlit interface

## 10. Future Enhancements

- Resume Rewrite

- Interview Question Generator
 
- Multi-Resume Comparison
 
- Cloud Deployment
 
- AI Career Coach

## 11. License

All rights reserved. A formal open-source license will be added soon.




## Author

**Sivasakthi S**

AI Engineer Aspirant