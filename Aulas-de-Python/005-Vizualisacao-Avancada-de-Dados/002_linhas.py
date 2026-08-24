import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Plot simples: total da conta por índice
plt.plot(df['total_bill'])
plt.title("Total da Conta (sequência)")
plt.xlabel("Índice")
plt.ylabel("Valor da Conta")
plt.show()

