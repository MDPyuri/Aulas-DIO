# Bibliotecas Essenciais para Análise de Dados em Python
>As três bibliotecas mais utilizadas para análise de dados em Python são: **NumPy**, **Pandas** e **Matplotlib**. Cada uma delas possui funcionalidades específicas que facilitam o trabalho com dados.

## NumPy
O **NumPy** (Numerical Python) é uma biblioteca fundamental para computação científica em Python. Ele fornece suporte para arrays multidimensionais e funções matemáticas de alto desempenho. Com o NumPy, é possível realizar operações matemáticas complexas de forma eficiente.
>NumPy documentation: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)

  
### Exemplo de uso do NumPy
```python
import numpy as np
# Criando um array NumPy
array = np.array([1, 2, 3, 4, 5])
# Calculando a média do array
mean = np.mean(array)
print("Média:", mean)
```
>Vide [001_numpy.py](./001_numpy.py)
É necessário instalar o NumPy antes de utilizá-lo. Para isso, utilize o comando:
```bash
pip install numpy
```

## Pandas
O **Pandas** é uma biblioteca poderosa para manipulação e análise de dados. Ele fornece estruturas de dados como DataFrames e Series, que facilitam a leitura, escrita e manipulação de dados tabulares. Com o Pandas, é possível realizar operações como filtragem, agregação e transformação de dados de maneira eficiente.
>Pandas documentation: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

### Exemplo de uso do Pandas
```python
import pandas as pd
# Criando um DataFrame
df = pd.DataFrame({
    'nome': ['Alice', 'Bob', 'Charlie'],
    'idade': [25, 30, 35]
})
# Calculando a média das idades
mean_age = df['idade'].mean()
print("Média das idades:", mean_age)
```
>Vide [002_pandas.py](./002_pandas.py)
É necessário instalar o Pandas antes de utilizá-lo. Para isso, utilize o comando:
```bash
pip install pandas
```

O Pandas também oferece funcionalidades para leitura e escrita de arquivos em diversos formatos, como CSV, Excel e SQL, tornando-o uma ferramenta essencial para análise de dados.

## Matplotlib
O **Matplotlib** é uma biblioteca de visualização de dados em Python. Ele permite criar gráficos estáticos, animados e interativos de forma simples e flexível. Com o Matplotlib, é possível gerar gráficos de linha, barra, dispersão, histogramas e muito mais.
>Matplotlib documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)

### Exemplo de uso do Matplotlib
```python
import matplotlib.pyplot as plt
# Criando um gráfico de linha
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
```
>Vide [003_matplotlib.py](./003_matplotlib.py)
É necessário instalar o Matplotlib antes de utilizá-lo. Para isso, utilize o comando:
```bash
pip install matplotlib
```