from skill_extract import resume_text
from ai_analyzer import resume_ai_analyzer

# method is for analyzing the resume and job description skills
def analyze_resume():
    user_input=resume_text.lower().replace("\n", " ").strip()
    job_skills = input("Enter the job description skills seperated by comma:")
    job_skills_lower = {item.lower() for item in job_skills.split(",")}
    return {"job_skills": job_skills_lower, "resume_text": user_input}

user_data = analyze_resume()
ai_result = resume_ai_analyzer(user_data)
# method is for calculating the ATS score based on the matching skills and missing skills
def calculate_ats_score(user_data, ai_result):
    matching_skills = []
    missed_skills = []
    for skill in user_data['job_skills']:
        if skill.lower() in user_data['resume_text']:
            matching_skills.append(skill)
        else:
            missed_skills.append(skill)
    print(matching_skills)
    score =len(matching_skills)/len(user_data['job_skills']) * 100
    required_skills = [skill.capitalize() for skill in matching_skills]
    print("ATS of resume is: ", round(score, 2), "%")
    print("Skills you have:", ", ".join(required_skills))
    print("Skills you are missing:", ", ".join(missed_skills))
    print ("reason", ai_result['summary'])

calculate_ats_score(user_data, ai_result)