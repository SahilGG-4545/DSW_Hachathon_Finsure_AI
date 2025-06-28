import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
import tempfile
from utils.llm_utils import query_openai

def analyze_spending(breakdown: dict) -> str:
    breakdown_str = "\n".join(f"{cat}: {amt}" for cat, amt in breakdown.items())
    prompt = f"""You're a personal finance advisor focusing on insurance.
all the values are in INR(₹).
make it in a way that is easy to understand and follow.it must be consise and simple. not too much clustering.
Here is a breakdown of user's spending:\n{breakdown_str}

Analyze the user's financial habits, detect overspending or insurance-related risk exposure, and suggest:
- Areas to reduce spending
- Where to allocate savings
- Whether the user might lack insurance coverage (health, life, etc.)
Analyze this user’s spending pattern. Based on their financial behavior, suggest areas for improvement and 
recommend insurance products (health, term, critical illness, etc.) they might be missing or under-covered on
"""
    return query_openai(prompt)




def run():
    st.header("Financial Health Check")

    file = st.file_uploader("Upload Bank Statement (CSV or PDF)", type=["csv", "pdf"])
    chart_data = None
    spending_analysis = ""

    if file:
        if file.name.endswith(".pdf"):
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(file.read())
                pdf_text = ""
                reader = PdfReader(tmp.name)
                for page in reader.pages:
                    pdf_text += page.extract_text()
                st.text_area("📄 Extracted PDF Text", pdf_text, height=200)

        else:
            df = pd.read_csv(file)
            st.subheader("📊 Expense Overview")
            st.dataframe(df)

            chart_data = df.groupby("Category")["Amount"].sum()
            st.bar_chart(chart_data)

            if isinstance(chart_data, pd.Series) and not chart_data.empty:
                if st.button("🧠 Analyze Spending"):
                    with st.spinner("Analyzing..."):
                        spending_analysis = analyze_spending(chart_data.to_dict())
                        st.markdown("### 🧠 Analysis")
                        st.markdown(spending_analysis)

    