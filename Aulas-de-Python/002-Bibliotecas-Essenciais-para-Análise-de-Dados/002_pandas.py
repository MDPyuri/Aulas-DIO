import pandas as pd
# Criando um DataFrame
df = pd.DataFrame({
    'nome': ['Alice', 'Bob', 'Charlie'],
    'idade': [25, 30, 35]
})
# Calculando a média das idades
mean_age = df['idade'].mean()
print("Média das idades:", mean_age)
