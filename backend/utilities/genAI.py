import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

GOOGLE_API_KEY = os.getenv("API_KEY")
class SubTopic(BaseModel):
    sub_topic_name: str
    refs: list[str]

class Topic(BaseModel):
    topic_name: str
    subtopics: list[SubTopic]

class Subject(BaseModel):
    subject_name: str
    topics: list[Topic]

#return json string representing Subject type
def generateList(topic: str):
    client = genai.Client(api_key=GOOGLE_API_KEY)
    prompt = f'''As a module planner, if I want to learn about {topic},
                outline topics that I must know with subtopics and reference to the tutorial
                '''
    response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents=prompt,config= {
        'response_mime_type': 'application/json',
        'response_schema': Subject
    })
    return response.text