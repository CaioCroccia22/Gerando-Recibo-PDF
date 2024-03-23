from fpdf import FPDF

# Variaveis

cliente = input("Digite o nome do cliente\n")
valor = input("Digite o valor: \n")
# assinatura = input("Digite sua assinatura: \n")
# nome = input("Digite o seu nome:\n")
importância_de = input("Digite o campo a importância de: \n")
#Layout do recibo

pdf = FPDF()
# orientation= 'L' -> gera o arquivo em paisagem
pdf.add_page(orientation='L')
pdf.set_font("Arial", "", 20)
pdf.image("img/recibo.png", x=-10, y=0)
pdf.text(260, 30, valor)
pdf.text(70, 50, cliente)
pdf.text(70, 63, importância_de)
# pdf.text(10, 50, nome)
pdf.output("recibo.pdf")
print("Recibo gerado com sucesso!")