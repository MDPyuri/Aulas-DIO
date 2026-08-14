# Processamento e Limpeza de Dados
A análise de dados envolve não apenas a exploração e visualização dos dados, mas também o **processamento e limpeza** dos mesmos. Dados brutos frequentemente contêm inconsistências, valores ausentes ou duplicados, que podem afetar a qualidade da análise. Nesta seção, abordaremos técnicas essenciais para preparar os dados antes da análise.

## Problemas Comuns em Dados
1. **Valores Ausentes (Missing Values)**: Dados incompletos podem levar a conclusões incorretas. É importante identificar e tratar esses valores.
2. **Valores Duplicados**: Registros duplicados podem distorcer estatísticas e análises. É necessário remover ou consolidar esses registros.
3. **Inconsistências de Formato**: Dados podem estar em formatos diferentes (ex.: datas, números, strings), o que dificulta a análise. Padronizar formatos é crucial.
4. **Outliers**: Valores extremos podem influenciar significativamente os resultados da análise. Identificar e tratar outliers é uma etapa importante no processamento de dados.

## Técnicas de Limpeza de Dados
### Tratamento de Valores Ausentes
- **Remoção de Linhas ou Colunas**: Se a quantidade de valores ausentes for pequena, pode-se optar por remover as linhas ou colunas afetadas.
- **Substituição por Valores Estatísticos**: Substituir valores ausentes por média, mediana ou moda da coluna pode ser uma abordagem eficaz.
- **Interpolação**: Para séries temporais, a interpolação pode ser usada para estimar valores ausentes com base nos dados vizinhos.

Segue um exemplo simples de como identificar e tratar valores ausentes usando a biblioteca Pandas:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Carregando o dataset
df = pd.read_csv(url)

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Informações gerais
df.info()

# Contando valores ausentes por coluna
print(df.isnull().sum())
```
>Vide [001_limpeza.py](./001_limpeza.py)

### Removendo linhas com valores ausentes:
```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df.info()  # Verificando informações do DataFrame, incluindo valores ausentes

print(df.isnull().sum())

df_cleaned = df.dropna() # Removendo linhas com valores ausentes
print(df_cleaned.head())
```
>Vide [002_limpeza.py](./002_limpeza.py)

### Preenchendo valores ausentes com a média da coluna:
```python
import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df[['PassengerId', 'Name', 'Age']].head(10))

print("-" * 30)

# Calculando a média
mean_age = df['Age'].mean()
# Preenchendo valores ausentes com a média
df['Age'] = df['Age'].fillna(mean_age)

print(df[['PassengerId', 'Name', 'Age']].head(10))
```
>Vide [003_limpeza.py](./003_limpeza.py)

## Tratamento de Valores Duplicados
Valores duplicados podem distorcer análises e estatísticas. A remoção de duplicatas é uma etapa importante no processamento de dados. A biblioteca Pandas oferece métodos para identificar e remover duplicatas de forma eficiente.

```python
import pandas as pd

# Criando um pequeno DataFrame com duplicatas
data = {
    'ID': [1, 2, 2, 3, 4, 4],
    'Nome': ['Ana', 'Bruno', 'Bruno', 'Carlos', 'Daniela', 'Daniela'],
    'Idade': [23, 35, 35, 40, 29, 29]
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

# Removendo duplicatas
df_no_duplicates = df.drop_duplicates()

print("\nDataFrame sem duplicatas:")
print(df_no_duplicates)

```
>Vide [006_duplicatas.py](./006_duplicatas.py)

## Normalização e Padronização de Dados
A normalização e padronização são técnicas utilizadas para ajustar a escala dos dados, tornando-os comparáveis e melhorando o desempenho de algoritmos de aprendizado de máquina.
- **Normalização**: Ajusta os valores para um intervalo específico, geralmente entre 0 e 1. É útil quando os dados possuem diferentes escalas.
  ```python
  import pandas as pd

  url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
  df = pd.read_csv(url)

  mean_age = df['Age'].mean()
  df['Age'] = df['Age'].fillna(mean_age)

  from sklearn.preprocessing import MinMaxScaler

  scaler = MinMaxScaler()
  df['Age_norm'] = scaler.fit_transform(df[['Age']])
  print(df[['Age', 'Age_norm']].head(20))

  ```
  >Vide [004_normalizacao.py](./004_normalizacao.py)

- **Padronização**: Transforma os dados para que tenham média zero e desvio padrão igual a um. É útil quando os dados seguem uma distribuição normal.
  ```python
  import pandas as pd
  from sklearn.preprocessing import StandardScaler

  # Carregar dataset
  url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
  df = pd.read_csv(url)

  # Preencher valores ausentes em Age com a média
  mean_age = df['Age'].mean()
  df['Age'] = df['Age'].fillna(mean_age)

  # Selecionar colunas numéricas
  numeric_cols = ['Age', 'Fare']

  # Padronização (Z-score)
  scaler = StandardScaler()
  df_standard = df.copy()
  df_standard[numeric_cols] = scaler.fit_transform(df[numeric_cols])

  print("Antes da padronização:")
  print(df[numeric_cols].head())

  print("\nDepois da padronização:")
  print(df_standard[numeric_cols].head())

  ```
  >Vide [005_padronizacao.py](./005_padronizacao.py).
  > É necessário instalar a biblioteca `scikit-learn` para utilizar o `StandardScaler`. Você pode instalar usando o comando:
  ```bash
  pip install scikit-learn
  ```

## Outliers
Outliers são valores que se desviam significativamente da maioria dos dados. Eles podem distorcer análises estatísticas e afetar modelos de aprendizado de máquina. Existem várias técnicas para identificar e tratar outliers, incluindo métodos estatísticos e visuais.

Um breve exemplo de como identificar outliers usando o método do Z-score:

```python
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Carregar dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" 
df = pd.read_csv(url)
# Preencher valores ausentes em Age com a média
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Visualização de outliers usando boxplot
plt.boxplot(df['Age'])
plt.title("Boxplot de Idade - Outliers")
plt.show()

# Calcular Z-score para a coluna 'Age'
z_scores = stats.zscore(df['Age'])

# Identificar outliers (Z-score > 3 ou < -3)
outliers = df[(z_scores > 3) | (z_scores < -3)]

print("Outliers identificados:")
print(outliers[['PassengerId', 'Name', 'Age']])
```
>Vide [007_outliers.py](./007_outliers.py)

## Automação, Documentação e Validação
### Automação de Pré-processamento
Automatizar o pré-processamento de dados é essencial para garantir consistência e eficiência, especialmente quando lidamos com grandes volumes de dados. Scripts e pipelines podem ser criados para realizar tarefas repetitivas de limpeza e transformação de dados.
- **Pipelines de dados:**
  1. Carregar dados brutos.
  2. Limpar dados.
  3. Transformar dados.
  4. Gerar dataset final.
   
```python
import pandas as pd

data = {
    'ID': [1, 2, 2, 3, 4, 4],
    'Nome': ['Ana', 'Bruno', 'Bruno', 'Carlos', 'Daniela', 'Daniela'],
    'Idade': [23, 35, 35, 40, 29, 29]
}

df = pd.DataFrame(data)

# Função para processar dados
def process_data(df):
    # Remover duplicatas
    df = df.drop_duplicates()
    # Preencher valores ausentes com a média
    df['Idade'] = df['Idade'].fillna(df['Idade'].mean())
    return df

# Aplicando a função de processamento
df_processed = process_data(df)

print("DataFrame processado:")
print(df_processed)

```
>Vide [008_automacao.py](./008_automacao.py)

### Documentação e Validação
Documentar o processo de limpeza e transformação de dados é crucial para garantir a reprodutibilidade e a compreensão do fluxo de trabalho. Além disso, validar os dados após o processamento ajuda a identificar possíveis erros ou inconsistências que possam ter sido introduzidos durante a limpeza.  
  
- **Reprodutibilidade**: Manter registros detalhados das etapas de processamento, incluindo scripts, parâmetros e decisões tomadas.
- **Validação**: Implementar verificações para garantir que os dados processados atendam aos critérios esperados, como ausência de valores ausentes, consistência de formatos e conformidade com regras de negócio.

[Voltar ao índice](../../README.md)

