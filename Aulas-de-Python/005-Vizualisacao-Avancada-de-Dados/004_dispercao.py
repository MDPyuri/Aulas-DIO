import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Dispersão: total da conta vs gorjeta
plt.scatter(df["total_bill"], df["tip"], alpha=0.7, c="green")
plt.title("Dispersão: Conta vs Gorjeta")
plt.xlabel("Total da Conta")
plt.ylabel("Gorjeta")
plt.show()

