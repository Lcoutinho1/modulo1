import requests
from numpy.ma.core import filled


def enviar_arquivos():
    # Caminho do arquivo para upload
    caminho= 'C:/Users/leandro/Downloads/Git/modulo1/coleta_dados'

    #Enviar o arquivos
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file': open(caminho,'rb')})
    saida_requisicao=requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado, link para acesso:",url)



