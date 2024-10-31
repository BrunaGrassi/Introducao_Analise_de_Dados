import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"

novo_cabecalho = ["Mês","Ano 1958","Ano 1959","Ano 1960"]

df = pd.read_csv(url, names=novo_cabecalho, header=0)
print(df.head())