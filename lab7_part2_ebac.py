import requests
from bs4 import BeautifulSoup
import pandas as pd
from numpy.ma.core import append

url='https://books.toscrape.com/'
requisicao=requests.get(url)
requisicao.encoding = 'utf-8'
catalogo=[]
contar_livro=0
extracao=BeautifulSoup(requisicao.text, 'html.parser')

for linha_texto in extracao.find_all('article'):
    contar_livro+=1
    titulo=linha_texto.h3.a['title']
    preco=linha_texto.find('p',class_='price_color').get_text(strip=True)
    lista_livro={
        'Título': titulo,
        'Preço': preco
    }
    catalogo.append(lista_livro)
print(contar_livro)
df_catalogo=pd.DataFrame(catalogo)
print(df_catalogo)

