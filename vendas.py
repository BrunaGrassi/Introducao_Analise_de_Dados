import pandas as pd

#url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
#novo_cabecalho = ["Mês","Ano 1958","Ano 1959","Ano 1960"]

#df = pd.read_csv(url, names=novo_cabecalho, header=0)
#print(df.head())

novo_cabecalho2 = ["REF","PRODUTO","QTD","PREÇO","DATA"]

df = pd.read_csv(r"C:\Users\brude\OneDrive\Área de Trabalho\Projetos Pessoais Programação\Python\vendas.csv", names=novo_cabecalho2, header=0)
print(df.head())