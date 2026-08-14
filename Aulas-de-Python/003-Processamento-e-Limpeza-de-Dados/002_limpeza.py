import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df.info()  # Verificando informações do DataFrame, incluindo valores ausentes

print(df.isnull().sum())

df_cleaned = df.dropna() # Removendo linhas com valores ausentes
print(df_cleaned.head())