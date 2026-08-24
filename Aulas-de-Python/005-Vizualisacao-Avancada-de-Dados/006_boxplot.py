import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Boxplot de gorjetas por dia
df.boxplot(column="tip", by="day", grid=False)
plt.title("Boxplot de Gorjetas por Dia")
plt.suptitle("")  # remove título automático
plt.xlabel("Dia")
plt.ylabel("Gorjeta")
plt.show()

