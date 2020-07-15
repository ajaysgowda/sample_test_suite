#%%
# functions
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm

def coord(x, y, unit=1):
    x, y = x * unit, y * unit
    return x, y

#%%
# hello_reportlab.py


c = canvas.Canvas("docs/reporting/hello.pdf", bottomup=0)

c.drawString(*coord(15, 20, mm), text="Welcome to Reportlab!")
c.showPage()
c.save()

#%%
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def font_demo(my_canvas, fonts):
    pos_y = 750
    for font in fonts:
        my_canvas.setFont(font, 12)
        my_canvas.drawString(30, pos_y, font)
        pos_y -= 10

#%%
my_canvas = canvas.Canvas("docs/reporting/fonts.pdf",
                            pagesize=letter)
fonts = my_canvas.getAvailableFonts()
font_demo(my_canvas, fonts)
my_canvas.save()

#%%
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
def rotate_demo():
    my_canvas = canvas.Canvas("docs/reporting/rotated.pdf",
    pagesize=letter)
    my_canvas.translate(inch, inch)
    my_canvas.setFont('Helvetica', 14)
    my_canvas.drawString(inch, inch, 'Normal')
    my_canvas.line(inch, inch, inch+100, inch)
    my_canvas.rotate(45)
    my_canvas.drawString(inch, -inch, '45 degrees')
    my_canvas.line(inch, inch, inch+100, inch)
    my_canvas.rotate(45)
    my_canvas.drawString(inch, -inch, '90 degrees')
    my_canvas.line(inch, inch, inch+100, inch)
    my_canvas.save()
rotate_demo()
