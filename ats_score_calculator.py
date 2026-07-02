# method is for calculating the ATS score based on the matching skills and missing skills
def calculate_ats_score(user_data, ai_result):
    candidate_skills_raw = ai_result['candidate_skills']['language'] + ai_result['candidate_skills']['framework'] + ai_result['candidate_skills']['database'] + ai_result['candidate_skills']['deployment_tools'] + ai_result['candidate_skills']['version_control'] + ai_result['candidate_skills']['business_skills']
    candidate_skills = {item.lower() for item in candidate_skills_raw}
    missed_skills =  ai_result['missing_skills']
    matching_skills = []
    for skill in user_data['job_skills']:
        if skill.lower() in candidate_skills:
            matching_skills.append(skill)

    score =len(matching_skills)/len(user_data['job_skills']) * 100
    print(matching_skills)
    ats_data = {"ats_score":round(score, 2), "candidate_skills": candidate_skills, "missed_skills": missed_skills, "recommendations": ai_result['recommendations'] }
    return ats_data
    