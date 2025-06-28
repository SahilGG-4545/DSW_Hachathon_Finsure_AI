# modules/mistake_sim.py
import streamlit as st
from utils.llm_utils import query_openai

def run():
    st.header("⚠️ Insurance Mistake Simulator")

    st.markdown("""
This module simulates the long-term consequences of common insurance mistakes, helping you understand their financial and protection impact.
Select a mistake or describe your own scenario:
""")

    mistake_type = st.selectbox("❌ Common Mistake Category", [
        "Skipped Term Insurance",
        "Underinsured Health Policy",
        "Relied Only on Employer Insurance",
        "Bought ULIP without Understanding Risks",
        "Did Not Disclose Pre-existing Condition",
        "Lapsed Policy Due to Missed Premium",
        "Custom Scenario"
    ])

    if mistake_type == "Custom Scenario":
        scenario = st.text_area("📝 Describe your insurance mistake or risky decision", 
            placeholder="e.g. I cancelled my life insurance after changing jobs, thinking I didn’t need it.")
    else:
        scenario = mistake_type

    if st.button("🧠 Simulate Consequences"):
        prompt = f"""
        You are a professional GenAI financial advisor focused on insurance risk analysis.
        give a humanised answer. keep it balanced(not too short) and concise.
        The user has made a potential mistake in their insurance planning. Analyze the scenario and respond with:
        1. ⚠️ Key Risks Involved
        2. 📉 Estimated Financial + Protection Impact
        3. ✅ Practical Recovery Advice or Future Precautions

        Scenario:
        {scenario}
"""
        result = query_openai(prompt)
        st.markdown("### 💡 Simulation Results")
        st.markdown(result)
