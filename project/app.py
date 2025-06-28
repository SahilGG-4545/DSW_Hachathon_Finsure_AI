# app.py
import streamlit as st
from modules import health_check, mistake_sim, claim_confidence,coverage_gap

st.set_page_config(page_title="Financial Fitness Assistant", layout="wide")
st.title("FinSure AI: Blending Financial Wellness & Insurance Clarity")

option = st.sidebar.radio("Select Module", [
    "1️⃣ Financial Health Check",
    "2️⃣ coverage gap",
    "3️⃣ Mistake Simulator",
    "4️⃣ Insurance Claim Advisor"
])

if option == "1️⃣ Financial Health Check":
    health_check.run()
elif option == "2️⃣ coverage gap":
    coverage_gap.run()
elif option == "3️⃣ Mistake Simulator":
    mistake_sim.run()
elif option == "4️⃣ Insurance Claim Advisor":
    claim_confidence.run()
