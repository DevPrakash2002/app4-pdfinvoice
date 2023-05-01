from pathlib import Path
import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoice/*.xlsx")

for file in filepaths:
    df = pd.read_excel(file, sheet_name="Sheet 1")
    print(df)
    pdf = FPDF(orientation="P", unit="mm", format='A4')
    pdf.add_page()
    filename = Path(file).stem
    invoice_no = file.split('-')[0]
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt="Invoice nr.")
    pdf.output(f'PDFs/{filename}.pdf')

