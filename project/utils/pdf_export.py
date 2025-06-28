# utils/pdf_export.py
from fpdf import FPDF

def save_pdf(report, filename="financial_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in report.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)
