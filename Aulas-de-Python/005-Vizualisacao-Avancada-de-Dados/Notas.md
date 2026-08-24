# Vizualisação de Dados com Python
A vizualisação de dados permite transformar informaações complexas em gráficos fáceis de interpretar. Com gráficos é possível:
- identificar padrões
- comparar valores
- detectar tendências
- comunicar resultados de forma clara
Por isso a vizualisação é uma etapa essencial na análise de dados.

Para os testes desse módulo será utilizado o consumo de um dataset real de gorjetas em restaurantes disponível em [tips.csv]("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv").  
Conteúdo:
- Valor da conta
- Valor da gorjeta
- Dia da semana
- Número de pessoas
- Horário da refeição

Exemplo de uso:
```Python
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df = pd.read_csv(url)

print(df.head())
```
> Vide [001_dataset.py]("./001_dataset.py")

## Bibliotecas para Vizualisação de Dados
As mais utilizadas são:
- **Matplotlib**: gráficos básicos
- **Seaborn**: gráficos estatísticos
- **Plotly**: gráficos interativos

### Matplotlib
O Matplotlib já foi abordado no Módulo [002-Bibliotecas-Essenciais-para-Análise-de-Dados](../002-Bibliotecas-Essenciais-para-Análise-de-Dados/Notas.md), porém segue um exemplo breve de seu uso:

- **Gráfico de Linha Simples:**
  Esse script mostra como criar um gráfico de linha simples com Matplotlib. É útil para visualizar a evolução de valores ao longo de um índice ou tempo, ajudando a identificar tendências gerais rapidamente.

  ```python
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

  ```
  >Vide [002_linhas.py](./002_linhas.py)

- **Gráfico de Barras:**
  Aqui temos um gráfico de barras que apresenta a média de gorjetas por dia. Esse tipo de visualização é essencial para comparar categorias de forma clara e objetiva, sendo muito usado em relatórios e dashboards.

  ```python
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

  ```
  >Vide [003_barras.py](./003_barras.py)

- **Gráfico de Dispersão:**
  O gráfico de dispersão permite analisar a relação entre duas variáveis (neste caso, total da conta e gorjeta). É uma ferramenta poderosa para identificar correlações, padrões e possíveis outliers em dados reais.

  ```python
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

  ```
  >Vide [004_dispercao.py](./004_dispercao.py)

- **Histograma:**
  Esse script cria um histograma da distribuição dos valores da conta. É fundamental para entender como os dados estão distribuídos, identificar concentrações e avaliar a variabilidade, algo muito usado em estatística aplicada.

  ```python
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

  ```
  >Vide [005_histograma.py](./005_histograma.py)

- **Boxplot:**
  O boxplot mostra a variação das gorjetas por dia. Ele é importante para visualizar a dispersão, mediana e possíveis valores extremos, sendo uma técnica prática para análises comparativas entre grupo

  ```python
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

  ```
  >Vide [006_boxplot.py](./006_boxplot.py)

- **Subplots:**
  Aqui são criados múltiplos gráficos lado a lado (subplots). Esse recurso é essencial quando precisamos comparar diferentes visualizações em um único painel, facilitando a análise conjunta de várias perspectivas dos dados.

  ```python
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

  ```
  >Vide [007_subplot.py](./007_subplot.py)

### Seaborn
O Seaborn é uma biblioteca de visualização de dados em Python construída sobre o Matplotlib, mas com foco em tornar os gráficos mais bonitos e informativos de forma simples. Ele oferece uma interface de alto nível para criar visualizações estatísticas, como distribuições, correlações e comparações entre categorias, sem precisar escrever muito código.

A principal diferença em relação ao Matplotlib é que o Seaborn **já vem com estilos prontos e funções otimizadas** para análise estatística. Enquanto o Matplotlib é extremamente flexível e funciona como uma “caixa de ferramentas” para qualquer tipo de gráfico, o Seaborn facilita o dia a dia ao automatizar tarefas comuns, como adicionar cores, legendas e calcular estatísticas automaticamente.

- Segue um código comparativo entre o Matplotlib e o Seaborn:
  ```python
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

  ```
  >Vide [008_seaborn.py](./008_seaborn.py)

### Plotly
O Plotly é uma biblioteca de visualização interativa em Python que se destaca por permitir gráficos dinâmicos e exploráveis diretamente em notebooks ou aplicações web. Diferente do Matplotlib, que gera gráficos estáticos, o Plotly facilita a interação: você pode dar zoom, mover o gráfico, destacar pontos e até exportar visualizações de forma mais rica.  
  
**Principais diferenças em relação ao Matplotlib:**  
  
- **Matplotlib**: gráficos estáticos, altamente personalizáveis, mas exigem mais código para interatividade.
- **Plotly**: gráficos interativos prontos, com menos esforço, ideais para dashboards e aplicações web.

**Exemplo Prático comparando com Matplotlib e Plotly:**
```python
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

```
>Vide [009_plotly.py](./009_plotly.py)