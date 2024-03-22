from fpdf import FPDF

#Layout

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("img/recibo.png", x=0, y=0)
pdf.output("recibo.pdf")
print("Recibo gerado com sucesso!")