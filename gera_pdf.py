from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
# Definir fonte
pdf.set_font('Arial', 'B', 16)
# Pdf.cell(Altura, Largura, "Texto para ser escrito")
pdf.cell(40, 10, 'Hello World')
pdf.output('dados/exemplos.pdf')
