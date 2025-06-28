import streamlit as st, openai, os

st.write("🔑 Key Loaded:", bool(os.getenv("OPENAI_API_KEY")))
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key:
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        st.success("✅ Success: " + resp["choices"][0]["message"]["content"])
    except Exception as e:
        st.error("❌ Error: " + str(e))
