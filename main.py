from pathlib import Path
import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoice/*.xlsx")


for file in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format='A4')
    pdf.add_page()


    filename = Path(file).stem
    invoice_no, Date = filename.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_no}", ln=1)


    pdf.cell(w=50, h=8, txt=f'Date: {Date}', ln=1)

    df = pd.read_excel(file, sheet_name="Sheet 1")
    column = list(df.columns)
    column = [item.replace('_', ' ').title() for item in column]

    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=column[0], border=1)
    pdf.cell(w=50, h=8, txt=column[1], border=1)
    pdf.cell(w=30, h=8, txt=column[2], border=1)
    pdf.cell(w=30, h=8, txt=column[3], border=1)
    pdf.cell(w=30, h=8, txt=column[4], border=1, ln=1)
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=50, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    total_sum = df['total_price'].sum()
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=10, txt=f'The Total Price is {total_sum}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=10, txt=f'PythonHow')
    pdf.image('pythonhow.png', w= 10)



    pdf.output(f'PDFs/{filename}.pdf')

