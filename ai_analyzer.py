import json

from dotenv import load_dotenv
from dotenv import dotenv_values
from google import genai
# for connecting to the Gemini API, this class provides methods for creating and managing interactions with the API.
def resume_ai_analyzer(user_data):
    load_dotenv()
    prompt = f"As a resume analyzer, analyze the following resume text and provide a summary of the candidate's skills, experience, and qualifications. Also, compare the candidate's skills with the job description skills provided and highlight any gaps or areas for improvement. Resume Text: {user_data['user_input']} Job Description Skills: {', '.join(user_data['job_skills'])}, share the response as JSON object with keys 'summary', 'matching_skills', 'missing_skills'"
    client= genai.Client()
    interaction = client.interactions.create(model="gemini-3-flash-preview", input=prompt,   response_format={
        "type": "text",
        "mime_type": "application/json"
    })
    print("Gemini:", interaction.output_text)
    result = json.loads(interaction.output_text)
    return result
