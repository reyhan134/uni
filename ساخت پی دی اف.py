from fpdf import FPDF

pdf = FPDF('P','mm','A4')

pdf.add_page('1')

pdf.set_font("Arial", size = 15)

pdf.cell(200, 10, txt = "Hello everyone",ln = 1, align = 'C')

pdf.cell(200, 10, txt = "ashrafi univercity",ln = 2, align = 'C')

pdf.cell(200, 10, txt = "create pdf by python",ln = 3, align = 'L')


pdf.add_page('2')

pdf.set_font("times",'B', size = 20)
pdf.cell(200, 10, txt = "create pdf with python is easy",ln = 1, align = 'R')


pdf.add_page('3')
pdf.set_font("Arial",'UI', size = 20)
pdf.cell(200, 10, txt = "Reyhane")
pdf.cell(200, 10, txt = "Heydarian")

pdf.output("uni2.pdf")
