import requests
from bs4 import BeautifulSoup

url='https://python.org.br/web/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text,'html.parser')

# Exibir o texto
print('--------EXTRAÇAO--------')
print(extracao.text.strip()[:2000])

# Filtar a exibição pela tag e contagem

for linha_texto in extracao.find_all('h2'):
    titulo=linha_texto.text.strip()
    print('titulo',titulo)


#contagem paragrafo 'p'
print('----------PARAGRAFO0========')
contagemparagrafo=0
for linha_texto in extracao.find_all('p'):
    paragrafo= linha_texto.text.strip()
    contagemparagrafo=contagemparagrafo+1
    print('paragrafo:  ',paragrafo)

print('contagem paragrafo',contagemparagrafo)

# desafio
# filtar tags ['h2','p']

#contagem correçao
contagem_titulo=0
contagem_paragrafo=0
#
# for linha_texto in extracao.find_all('h2'):
    if linha_texto.name == 'h2':
        contagem_titulo+=1  #contagem

for linha_texto in extracao.find_all('p'):
    if linha_texto.name =='p':
        contagem_paragrafo+=1


print('CORREÇAO TITULO   ',contagem_titulo)
print('CORREÇAO PARAGRAFO  ',contagem_paragrafo)

# exibindo o tecto de h2

print('============texto de h2============')
for linha_texto in extracao.find_all('h2'):
    titulosh2=linha_texto.text.strip()
    print(titulosh2)
#
# #exibindo texto de p

print('==========texto de p=========')
for linha_texto in extracao.find_all('p'):
    paragrafo_conteudo = linha_texto.text.strip()
    print(paragrafo_conteudo)

#exibir tags aninhadas
print('===========tags aninhadas ===============')
for titulo in extracao.find_all('h2'):
   print('titulo: ',titulo.text.strip())
   for link in titulo.find_next_siblings('p'):
       print('paragrafos:  ', link.text.strip())
       for a in link.find_all('a', href=True):
           print('texto link: ',a.text.strip(), ' ] url:,' ,a["href"])




