import pandas as pd

data = {
    'ID': [1, 2, 2, 3, 4, 4],
    'Nome': ['Ana', 'Bruno', 'Bruno', 'Carlos', 'Daniela', 'Daniela'],
    'Idade': [23, 35, 35, 40, 29, 29]
}

df = pd.DataFrame(data)

# Função para processar dados
def process_data(df):
    # Remover duplicatas
    df = df.drop_duplicates()
    # Preencher valores ausentes com a média
    df['Idade'] = df['Idade'].fillna(df['Idade'].mean())
    return df

# Aplicando a função de processamento
df_processed = process_data(df)

print("DataFrame processado:")
print(df_processed)