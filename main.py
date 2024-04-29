from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
client_groq = Groq(api_key=os.getenv('GROQ_API_KEY'))

app=FastAPI()

@app.get('/')
def homeAPI():
    return "API is working"

@app.get('/chat')
def chatComplete(prompt):
    openaiOutput = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user', 'content': prompt}
        ],
        max_tokens=100
    )

    return openaiOutput.choices[0].message.content

# the above function can be called as
# http://127.0.0.1:8000/chat?prompt=ENTER_PROMPT_HERE


@app.get('/chat-groq')
def chatCompleteGroq(prompt:str):
    groqOutput = client_groq.chat.completions.create(
    model='llama3-8b-8192',
    messages=[
        {'role':'user', 'content':prompt}
    ],
    max_tokens=500)

    return groqOutput.choices[0].message.content

