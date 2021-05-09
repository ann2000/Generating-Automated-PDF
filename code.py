import numpy as np
import pandas as pd
from fpdf import FPDF
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

#first page of PDF
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('helvetica', 'bold', 10)
pdf.set_text_color(255, 255, 255)

def bar_chart(credit, debit, balance):

    x = [x[0:6] for (x,y) in balance]
    y1 = [y for (x,y) in credit]
    y2 = [y for (x,y) in debit]
    y3 = [y for (x,y) in balance]
    n = len(x)
    index = np.arange(n)

