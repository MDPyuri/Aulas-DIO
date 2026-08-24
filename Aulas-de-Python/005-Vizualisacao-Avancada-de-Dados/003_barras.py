import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Média de gorjeta por dia
media_por_dia = df.groupby("day")["tip"].mean()

media_por_dia.plot(kind="bar", color="skyblue")
plt.title("Média de Gorjetas por Dia")
plt.ylabel("Valor Médio da Gorjeta")
plt.show()

