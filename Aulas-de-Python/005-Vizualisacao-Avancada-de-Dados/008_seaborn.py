import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# -----------------------------
# Gráfico com Matplotlib (mais manual)
plt.figure(figsize=(6,4))
plt.scatter(df["total_bill"], df["tip"], color="blue", alpha=0.6)
plt.title("Conta vs Gorjeta (Matplotlib)")
plt.xlabel("Total da Conta")
plt.ylabel("Gorjeta")
plt.show()

# -----------------------------
# Gráfico com Seaborn (mais otimizado)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day", size="size", palette="viridis", alpha=0.7)
plt.title("Conta vs Gorjeta (Seaborn)")
plt.show()
