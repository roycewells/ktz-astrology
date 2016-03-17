# pip install reportlab

import time
# from reportlab.lib.enums import TA_JUSTIFY
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Frame, Spacer
from datetime import time
from array import array

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
styles.add(ParagraphStyle(name='Centred',
                                   spaceBefore = 0,
								   fontName = "Times-Roman",
								   bulletFontName = "Time-Roman",
								   borderRadius = None,
								   firstLineIndent = 0,
								   leftIndent = 0,
								   underlineProportion = 0.0,
								   rightIndent = 0,
								   wordWrap = None,
								   allowWidows = 1,
								   backColor = None,
								   textTransform = None,
								   alignment = 1,
								   borderColor = None,
								   splitLongWords = 1,
								   leading = 12,
								   bulletIndent = 0,
								   allowOrphans = 0,
								   bulletFontSize = 10,
								   fontSize = 10,
								   borderWidth = 0,
							       bulletAnchor = "start",
								   borderPadding = 0,
								   endDots = None,
								   #textColor = Color(0,0,0,1),
								   spaceAfter = 0
                                  ))
styleC=styles["Centred"]


class Person:
	def __init__(self, name, birthday, chart_path, aspects_path, descriptions, putting_it_all_together):
		self.name=name
		self.birth=birthday
		self.chart=chart_path
		self.aspect=aspects_path
		self.desc=descriptions
		self.pat=putting_it_all_together

p=Person("Sekou Harris", "April 23 1994", "Morinus/Morinus/Res/charts.png", "pics/aspects_bk.png", array('c', 'placeholder array'), "placeholder")

story = []
story.append(Paragraph(" <b>" + p.name + "</b> " ,styleC))
story.append(Paragraph(" " + p.birth + " ",styleC))
story.append(Paragraph(" " + str(time) + " ",styleC))
story.append(Paragraph("Dear " + p.name + " ",styleH))
story.append(Paragraph("Welcome to the astrological journey that is your birth chart. A birth chart is a map of the sky at the time of your birth. In this report, I will analyze the unique combination of the different signs, houses, and planets which make up your birth chart, in order to help you better understand yourself, your strengths, assets, and areas of improvement. Every birth chart is quite complex, just like the human being whom it belongs to. Your personalized birth chart can be seen as a blueprint of your personality and your potential life paths. Enjoy the journey!", styleN))
story.append(Spacer(inch, 1.5*inch))

c = Canvas('form4.pdf')
width, height = letter 
c.setLineWidth(.3)
c.setFont('Helvetica', 12)
c.drawImage(p.aspect, inch, height -  4 * inch, inch, inch)
c.drawImage('pics/houses_bk.png', 3*inch, height -  4 * inch, inch, inch)
c.drawImage('pics/table_bk.png', 5*inch, height - 4 * inch, inch, inch)

table=[]
table.append(Paragraph(" " + p.desc.tostring() + " " ,styleN))

f = Frame(inch, inch, 6*inch, 9*inch, showBoundary=0)
f.addFromList(story,c)
f.addFromList(table,c)
c.save()

#doc = SimpleDocTemplate('form2.pdf', pagesize = letter)
#doc.build(story)

#c = canvas.Canvas("form1.pdf", pagesize=letter)
#w = 612, h = 792, in = 72
#c.setLineWidth(.3)
#c.setFont('Helvetica', 12)
# c.drawImage('pics/aspects_bk.png', inch, height -  2 * inch, inch, inch)
#c.drawString(100,100,"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
#c.showPage()
#c.save()