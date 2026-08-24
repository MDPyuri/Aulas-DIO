import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Histograma do total da conta
plt.hist(df["total_bill"], bins=20, color="orange", edgecolor="black")
plt.title("Distribuição do Total da Conta")
plt.xlabel("Valor da Conta")
plt.ylabel("Frequência")
plt.show()

