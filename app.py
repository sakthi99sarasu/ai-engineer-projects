user_input=input("Please enter your skills: ")
user_input_lower = {item.lower() for item in user_input.split(", ")}
job_skills = ["Python", "Java", "SQL", "JavaScript", "C++", "HTML", "CSS"]
job_skills_lower = {item.lower() for item in job_skills}
matching_skills = list(set(user_input_lower).intersection(job_skills_lower))
score =len(matching_skills)/len(job_skills) * 100
missed_skills = list(set(job_skills_lower) - set(user_input_lower))
required_skills = [skill.capitalize() for skill in matching_skills]
print("ATS of resume is: ", round(score, 2), "%")
print("Skills you have:", ", ".join(required_skills))
print("Skills you are missing:", ", ".join(missed_skills))