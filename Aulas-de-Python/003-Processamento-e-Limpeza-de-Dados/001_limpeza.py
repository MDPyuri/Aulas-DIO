import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Carregando o dataset
df = pd.read_csv(url)

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Informações gerais
df.info()

# Contando valores ausentes por coluna
print(df.isnull().sum())
