import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Preencher valores ausentes em Age com a média
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Selecionar colunas numéricas
numeric_cols = ['Age', 'Fare']

# Padronização (Z-score)
scaler = StandardScaler()
df_standard = df.copy()
df_standard[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("Antes da padronização:")
print(df[numeric_cols].head())

print("\nDepois da padronização:")
print(df_standard[numeric_cols].head())

