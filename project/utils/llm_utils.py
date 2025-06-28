# utils/llm_utils.py
import openai
import os
from dotenv import load_dotenv

openai.api_key = "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"

print("🔑 Currently loaded key:", openai.api_key[:12], "...", openai.api_key[-6:])

def query_openai(prompt, system="You are a financial advisor."):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']
