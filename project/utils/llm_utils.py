import os
import openai
import streamlit as st
from openai.error import AuthenticationError, OpenAIError

# Get API key from environment (set this in Streamlit Cloud under Secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(prompt, system_prompt="You are a helpful financial advisor."):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["message"]["content"]

    except AuthenticationError:
        st.error("❌ Authentication failed. Please check your OpenAI API key in Streamlit secrets.")
        return "Error: Authentication failed."

    except OpenAIError as e:
        st.error(f"❌ OpenAI Error: {str(e)}")
        return "Error: OpenAI API failed."

    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
        return "Error: Something went wrong."
