# Processamento e Limpeza de Dados
A análise de dados envolve não apenas a exploração e visualização dos dados, mas também o **processamento e limpeza** dos mesmos. Dados brutos frequentemente contêm inconsistências, valores ausentes ou duplicados, que podem afetar a qualidade da análise. Nesta seção, abordaremos técnicas essenciais para preparar os dados antes da análise.

## Problemas Comuns em Dados
1. **Valores Ausentes (Missing Values)**: Dados incompletos podem levar a conclusões incorretas. É importante identificar e tratar esses valores.
2. **Valores Duplicados**: Registros duplicados podem distorcer estatísticas e análises. É necessário remover ou consolidar esses registros.
3. **Inconsistências de Formato**: Dados podem estar em formatos diferentes (ex.: datas, números, strings), o que dificulta a análise. Padronizar formatos é crucial.
4. **Outliers**: Valores extremos podem influenciar significativamente os resultados da análise. Identificar e tratar outliers é uma etapa importante no processamento de dados.

## Técnicas de Limpeza de Dados
### 1. Tratamento de Valores Ausentes
- **Remoção de Linhas ou Colunas**: Se a quantidade de valores ausentes for pequena, pode-se optar por remover as linhas ou colunas afetadas.
- **Substituição por Valores Estatísticos**: Substituir valores ausentes por média, mediana ou moda da coluna pode ser uma abordagem eficaz.
- **Interpolação**: Para séries temporais, a interpolação pode ser usada para estimar valores ausentes com base nos dados vizinhos.

Segue um exemplo simples de como tratar valores ausentes usando a biblioteca Pandas:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Carregando o dataset
df = pd.read_csv(url)
# Exibindo as primeiras linhas do DataFrame
print(df.head())

df.info()  # Verificando informações do DataFrame, incluindo valores ausentes
```
>Vide [001_limpeza.py](./001_limpeza.py)