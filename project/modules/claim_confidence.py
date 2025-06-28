# modules/claim_confidence.py
import streamlit as st
from utils.llm_utils import query_openai
from utils.rag_utils import get_claim_context
import re
from PIL import Image
import pytesseract

# Set tesseract path if not in system PATH
# Example: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def run():
    st.header("🛡️ Claim Confidence Advisor")
    st.markdown("""
    Describe your situation below, and this GenAI assistant will:
    - Predict claim eligibility
    - Estimate approval confidence
    - Suggest documents required
    - Highlight risks or red flags
    """)

    user_input = st.text_area("🗣️ What happened?", height=150, placeholder="e.g. My car was hit while parked outside my office...")

    uploaded_file = st.file_uploader("📎 Optional: Upload FIR / Medical Bill", type=["png", "jpg", "jpeg"])
    ocr_text = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        ocr_text = pytesseract.image_to_string(image)

        st.markdown("📝 Extracted Text from Upload:")
        st.code(ocr_text)

    if st.button("🔍 Analyze My Claim") and user_input:
        with st.spinner("Analyzing claim..."):
            context = get_claim_context()
            prompt = f"""
You are an intelligent insurance assistant.

Based on the rules below, analyze the user's situation, determine claim eligibility, and respond with:
1. ✅ Claim Eligibility (Yes/No with reason)
2. 📊 Confidence Score (out of 100)
3. 📋 Required Documents (bulleted list)
4. ⚠️ Tips or Warnings

Insurance Rules:\n{context}\n\nUser Situation:\n{user_input}
"""
            if ocr_text:
                prompt += f"\n\nAdditional User Evidence:\n{ocr_text}"
            result = query_openai(prompt)
            st.markdown("### 🧠 AI Analysis")
            st.markdown(result)

            # Extract and display confidence score as progress bar
            score_match = re.search(r"(\d{1,3})/100", result)
            if score_match:
                score = int(score_match.group(1))
                st.markdown("### 📊 Visual Confidence Score")
                st.progress(min(score, 100) / 100.0)

            st.download_button("📥 Download Report", result, file_name="claim_advice.txt")