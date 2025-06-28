import streamlit as st
import pandas as pd
import re
from utils.llm_utils import query_openai

def run():
    st.header("🛡️ Insurance Coverage Gap Analyzer")

    st.markdown("""
This tool evaluates your current insurance protection and helps identify:

- ❌ Missing or insufficient coverage  
- ✅ Important insurance types based on your profile  
- ⚠️ Risk exposure based on your lifestyle and expenses  
    """)

    age = st.slider("🎂 Age", 18, 65, 30)
    income = st.number_input("💼 Annual Income (₹)", step=10000)
    dependents = st.slider("👨‍👩‍👧‍👦 Number of Dependents", 0, 10, 2)

    existing_insurance = st.text_area("📋 What insurance policies do you currently have?",
        placeholder="e.g., health insurance (₹5L), term life (₹50L), vehicle insurance")

    uploaded_csv = st.file_uploader("📎 Upload Bank Statement CSV (optional)", type=["csv"])
    expense_summary = ""

    if uploaded_csv is not None:
        df = pd.read_csv(uploaded_csv)
        summary = df.groupby("Category")["Amount"].sum().to_dict()
        expense_summary = "\n".join([f"{k}: ₹{v}" for k, v in summary.items()])
        st.markdown("### 📊 Expense Summary")
        st.json(summary)

    if st.button("🔍 Analyze My Coverage"):
        with st.spinner("Evaluating coverage gaps..."):
            prompt = f"""
You are an expert insurance advisor.

Based on the user's information, evaluate the sufficiency of their current insurance coverage and identify missing or inadequate areas.

User Profile:
- Age: {age}
- Annual Income: ₹{income}
- Number of Dependents: {dependents}
- Existing Insurance: {existing_insurance}

Monthly Spending Breakdown:\n{expense_summary}

Provide a concise report with:
1. ✅ Essential insurance the user already has (and whether coverage is adequate)
2. ❌ Missing coverage types or gaps
3. 📈 Suggested improvements (e.g., increase sum insured, add disability cover)
4. ⚠️ Risk warnings (if applicable)
5. 📊 Risk Score (out of 100, based on user's exposure)

Use bullet points and a professional tone. Keep it under 300 words.
Include the line: Risk Score: [XX]/100
"""
            result = query_openai(prompt)

            st.markdown("### 🧠 Coverage Gap Report")
            st.markdown(result)

            score_match = re.search(r"Risk Score:\s*(\d{1,3})/100", result)
            if score_match:
                score = int(score_match.group(1))
                st.markdown("### 📊 Risk Exposure Score")
                st.progress(min(score, 100) / 100.0)
