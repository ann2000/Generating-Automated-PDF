import numpy as numpy
import pandas as pd
from fpdf import FPDF
import matplotlib as mpl
from matplotlib.ticker import ScalarFormatter

#first page of document
pdf = FPDF(orientation='P', unit='mm', format='A$')
pdf.add_page()
pdf.set_font('helvetica', 'bold', 10)
pdf.set_text_color(255,255,255)
