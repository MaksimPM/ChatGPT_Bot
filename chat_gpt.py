import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('openai_api_key'))


def gpt(text):
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a bot assistant imitating a real person."},
            {"role": "user", "content": f"{text}"}
        ],
        temperature=1.0
    )
    english_text = completion.choices[0].message.content
    return english_text
