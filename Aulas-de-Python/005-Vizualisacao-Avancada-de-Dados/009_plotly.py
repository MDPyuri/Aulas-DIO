import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar dados
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# -----------------------------
# Gráfico com Matplotlib (estático)
plt.figure(figsize=(6,4))
plt.scatter(df["total_bill"], df["tip"], color="purple", alpha=0.6)
plt.title("Conta vs Gorjeta (Matplotlib)")
plt.xlabel("Total da Conta")
plt.ylabel("Gorjeta")
plt.show()

# -----------------------------
# Gráfico com Plotly (interativo)
fig = px.scatter(
    df, 
    x="total_bill", 
    y="tip", 
    color="day", 
    size="size", 
    title="Conta vs Gorjeta (Plotly Interativo)",
    labels={"total_bill":"Total da Conta", "tip":"Gorjeta"}
)
fig.show()
