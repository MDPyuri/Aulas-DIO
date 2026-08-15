# Instalar as bibliotecas se ainda não estiver instalada
# pip install requests pandas matplotlib
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fazer a requisição
url = "https://api.frankfurter.app/latest?from=USD"
response = requests.get(url)

# Verificar se deu certo
if response.status_code == 200:
    data = response.json()
    
    # Extrair as taxas de câmbio
    rates = data["rates"]
    
    # Converter para DataFrame
    df = pd.DataFrame(list(rates.items()), columns=["Moeda", "Taxa"])
    
    # Mostrar as 10 primeiras moedas
    print(df.head(10))

    # Mostrar apenas as moedas BRL, EUR e GBP
    moedas_desejadas = ["BRL", "EUR", "GBP"]
    df_filtrado = df[df["Moeda"].isin(moedas_desejadas)]
    print(f"\nMoedas filtradas:\n{df_filtrado.to_string(index=False)}")

    # Plotar um gráfico de barras das moedas filtradas
    plt.figure(figsize=(10, 6))
    plt.bar(df_filtrado["Moeda"], df_filtrado["Taxa"], color='#6eaa5e')
    plt.xlabel('Moeda')
    plt.ylabel('Taxa de Câmbio')
    plt.title('Taxas de Câmbio - Moedas Filtradas')
    plt.show()
else:
    print("Erro na requisição:", response.status_code)