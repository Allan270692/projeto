
import numpy as np
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas  #aqui estamos importando o tipo canvas
from reportlab.lib.pagesizes import A4  #aqui o tamanho da página que irá aparecer no pdf criado
import pandas as pd

df = pd.read_excel("dados_aids_hiv_excel_1.xlsx")  #foi criado um arquivo excel com os dados que foram retirados do site do DATASUS sobre AIDS/
df = df.dropna()
df = df.drop_duplicates()  #limpeza de dados geral 

cnv = canvas.Canvas("grafico_aids.pdf", pagesize=A4) #começo da criação do pdf

cnv.save()


#1 = sim, 0 = não
