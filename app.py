from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

titulo = input('informe o titulo: ')
frase = input('Informe o texto: ')
autor = input('Nome do autor: ')


def create_pdf(filename, text):

    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica", 12)

    linhas = text.split('\n')

    x = 100
    y = 750

    for linha in linhas:
        c.drawString(x, y, linha)

        y -= 15

    c.save()


texto = f"{titulo}\n\n{frase}\n\n{frase}\n\n{frase}\n\n{
    frase}\n\n{frase}\n\n{frase}\n\nAutor: {autor}\n\n"


nome_arquivo = "exemplo.pdf"


create_pdf(nome_arquivo, texto)
