from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

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
