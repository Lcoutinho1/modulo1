import pandas as pd


#Lista: uma coleçao ordenada de elementos que podem ser de qualquer tipo
lista_nomes= ['Ana','Marcos','Carlos']
print('Lista de nomes: \n', lista_nomes)
print('o primeiro nome: \n', lista_nomes[0])

#Dicionario: estrutura composta de pares chave-valor
dicionario_pessoa={
    'nome': 'Ana',
    'idade': 28,
    'cidade': 'Sao paulo'
}
print('Dicionario  de uma pessoa: \n',dicionario_pessoa)
print('Atributo do dicionario: \n', dicionario_pessoa.get('nome'))

#Lista de dicionarios: estrutura de dados que combina lista e dicionarios
dados=[
    {'nome':'ana', 'idade':20 , 'cidade':'Sao paulo'},
    {'nome':'Marcos', 'idade':25 , 'cidade':'Sao Jose dos Campos'},
    {'nome':'Carlos', 'idade':35 , 'cidade':'Rio de Janeiro'}
]

#Dataframe: estrutura de dados bidimensional
df= pd.DataFrame(dados)
print('DataFrame \n',df)
print('nomes \n',df['nome'])

#selecionar colunas
print('colunas \n',df[['nome','idade','cidade']])

#selecionar linhas pelo indice
print('linhas ',df.iloc[0])

#Adicinar uma nova coluna
df['salario']=[4100,3600,5200]
print('com a nova coluna: \n',df)

#Adicionar novo registro
df.loc[len(df)]={
    'nome': 'joao',
    'idade': 38,
    'cidade': 'taubate',
    'salario': 4800
}
print('DataFrame atual \n',df)


#removendo uma coluna
df.drop('salario',axis=1,inplace=True)
print('aqui \n',df)

#Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade']>=30]
print('Filtro \n', filtro_idade)

#salvando o dataframe em um arquivo CSV
df.to_csv('dados.csv',index=False)

#Lendo um arquivo CSV em um dataframe
df_lido = pd.read_csv('dados.csv')
print('\n leitura do csv \n',df_lido)