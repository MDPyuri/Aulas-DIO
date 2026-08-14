import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Carregando o dataset
df = pd.read_csv(url)
# Exibindo as primeiras linhas do DataFrame
print(df.head())

df.info()  # Verificando informações do DataFrame, incluindo valores ausentes
