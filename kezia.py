import pandas as pd
import streamlit as st
from reportlab.pdfgen import canvas  #aqui estamos importando o tipo canvas
from reportlab.lib.pagesizes import A4  #aqui o tamanho da página que irá aparecer no pdf criado


tabela_aids = pd.read_csv("dados_aids_hiv.csv")  #foi criado um arquivo csv com os dados que foram retirados do site do DATASUS sobre AIDS/HIV

#e criamos uma váriavel que irá ler os dados do arquivo

tabela_aids.dropna() #aqui é para retirar os dados nulos do arquivo

cnv = canvas.Canvas("tabela_aids.pdf", pagesize=A4) #começo da criação do pdf

cnv.save()

