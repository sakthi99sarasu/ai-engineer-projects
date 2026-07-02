import json

from dotenv import load_dotenv
from dotenv import dotenv_values
from google import genai
from prompts import ATS_REVIEWER_PROMPT_TEMPLATE
# for connecting to the Gemini API, this class provides methods for creating and managing interactions with the API.
def resume_ai_analyzer(user_data):
    load_dotenv()
    prompt = ATS_REVIEWER_PROMPT_TEMPLATE.format(
    resume_text=user_data["resume_text"],
    job_skills=", ".join(user_data["job_skills"]))
    client= genai.Client()
    interaction = client.interactions.create(model="gemini-3-flash-preview", input=prompt,   response_format={
        "type": "text",
        "mime_type": "application/json"
    })
    result = json.loads(interaction.output_text)
    return result
