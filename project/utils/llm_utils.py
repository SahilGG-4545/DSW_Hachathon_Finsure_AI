# utils/llm_utils.py
import openai
import os
from dotenv import load_dotenv

# Load .env file in local development (ignored on Streamlit Cloud)
load_dotenv()

# Read key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(prompt, system="You are a financial advisor."):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']
