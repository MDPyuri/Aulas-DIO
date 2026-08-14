import pandas as pd

# Criando um pequeno DataFrame com duplicatas
data = {
    'ID': [1, 2, 2, 3, 4, 4],
    'Nome': ['Ana', 'Bruno', 'Bruno', 'Carlos', 'Daniela', 'Daniela'],
    'Idade': [23, 35, 35, 40, 29, 29]
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

# Removendo duplicatas
df_no_duplicates = df.drop_duplicates()

print("\nDataFrame sem duplicatas:")
print(df_no_duplicates)

