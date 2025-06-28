# utils/rag_utils.py
def get_claim_context():
    with open("data/insurance_rules.txt", "r", encoding="utf-8") as f:
        return f.read()
