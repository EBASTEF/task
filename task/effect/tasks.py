from celery.decorators import task
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
registerFontFamily('Vera', normal='Vera', bold='VeraBd', italic='VeraIt')


@task()
def save_to_pdf(first, last, date, email, number, continent):
    date_tab = date.split('/')
    date = '{d}-{m}-{y}'.format(d=date_tab[1], m=date_tab[0], y=date_tab[2])
    name = '{f} {l}'.format(f=first, l=last)
    pdf_file = canvas.Canvas('static/pdfs/example_file1.pdf')
    
    pdf_file.setFont('VeraIt', 40)
    pdf_file.drawString(170, 700, 'Example PDF')
    pdf_file.setFont('VeraBd', 21)
    pdf_file.drawString(50, 600, 'Name:')
    pdf_file.drawString(50, 500, 'Date of birth:')
    pdf_file.drawString(50, 400, 'E-mail:')
    pdf_file.drawString(50, 300, 'Favourite number:')
    pdf_file.drawString(50, 200, 'Your continent:')
    pdf_file.setFont('Vera', 21)
    pdf_file.drawString(350, 600, name)
    pdf_file.drawString(350, 500, date)
    pdf_file.drawString(350, 400, email)
    pdf_file.drawString(350, 300, number)
    pdf_file.drawString(350, 200, continent)
    
    pdf_file.save()