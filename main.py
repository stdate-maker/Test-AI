import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

try:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please make sure you have set your OPENAI_API_KEY in the .env file.")
