import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: histograma
axs[0].hist(df["total_bill"], bins=15, color="blue", edgecolor="black")
axs[0].set_title("Distribuição do Total da Conta")

# Subplot 2: dispersão
axs[1].scatter(df["total_bill"], df["tip"], alpha=0.6, c="red")
axs[1].set_title("Conta vs Gorjeta")
axs[1].set_xlabel("Total da Conta")
axs[1].set_ylabel("Gorjeta")

plt.tight_layout()
plt.show()
