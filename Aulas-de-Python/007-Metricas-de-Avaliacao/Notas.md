# Métricas de Avaliação de Modelos

> Antes de iniciar este módulo, achei por bem estudar o básico de regressão linear e alguns conceitos iniciais de algebra analítica. Todas as minhas anotações de estudo estão anexadas neste [PDF](./Estudo-preparatorio-para-modelos-de-regressao.pdf).

As métricas de avaliação de modelos em ciência de dados permitem identificar qual modelo apresenta melhor desempenho em cada situação e também revelar falhas, como **overfitting** (superajuste) ou **underfitting** (subajuste).

- Modelos em **overfitting** são aqueles que se ajustam excessivamente aos dados de treino, capturando até ruídos e padrões irrelevantes, o que compromete sua capacidade de generalização.
- Já os modelos em **underfitting** são simples demais e não conseguem identificar padrões relevantes nos dados, resultando em baixo desempenho.

Serão abordadas métricas para três tipos de problemas:

- **Regressão**: prever valores contínuos.
- **Classificação**: prever categorias.
- **Agrupamento (Clustering)**: descobrir padões nos dados.

## **Métricas do modelo de Regressão**

### Teoria Básica de Regressão

A regressão é um modelo de aprendizado supervisionado que busca prever valores **contínuos** (ex: preços, temperaturas, vendas). O objetivo é encontrar uma função matemática que melhor descreva a relação entre as variáveis independentes (features) e a variável dependente (target).

**Tipos principais:**

- **Regressão Linear Simples**: uma variável independente (y = ax + b)
- **Regressão Linear Múltipla**: múltiplas variáveis independentes
- **Regressão Polinomial**: relações não-lineares
- **Regressão Ridge/Lasso**: regressões com regularização

### Métricas de Avaliação em Regressão

1. **Mean Squared Error (MSE) - Erro Quadrático Médio**

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

Mede a média dos quadrados dos erros. Penaliza mais fortemente valores com erros maiores. Varia de 0 a infinito (0 é perfeito).

```python
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Dados de exemplo: preço da casa vs tamanho
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([150000, 250000, 350000, 450000, 550000])  # preço em reais

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_pred = modelo.predict(X)

# Calcular MSE
mse = mean_squared_error(y, y_pred)
print(f"MSE: {mse:.2f}")
```

> Vide [001_MSE.py](./001_MSE.py)

1. **Root Mean Squared Error (RMSE) - Raiz do Erro Quadrático Médio**

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

Versão da MSE na mesma unidade dos dados originais, tornando mais interpretável. Também penaliza erros grandes.

```python
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de exemplo com ruído
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([155000, 240000, 360000, 440000, 570000])  # preços com variação

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_pred = modelo.predict(X)

# Calcular MSE e RMSE
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")

# MSE: 118000000.00
# RMSE: 10862.78
```

> Vide [002_RMSE.py](./002_RMSE.py)

3. **Mean Absolute Error (MAE) - Erro Absoluto Médio**

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

Mede a média dos erros absolutos. Menos sensível a outliers que MSE/RMSE. Tem a mesma unidade dos dados.

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de exemplo com ruído
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([155000, 240000, 360000, 440000, 570000])  # preços com variação

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_pred = modelo.predict(X)

# Calcular MSE e RMSE
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")

# MSE: 118000000.00
# RMSE: 10862.78

mae = mean_absolute_error(y, y_pred)
print(f"MAE: {mae:.2f}")
# Se MAE = 10000, o modelo erra em média R$ 10.000
```

> Vide [003_MAE.py](./003_MAE.py)

4. **R² (Coeficiente de Determinação)**

$$R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$$

Indica a proporção da variância dos dados explicada pelo modelo. Varia de 0 a 1 (1 é perfeito, 0 indica modelo ruim).

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de exemplo com ruído
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([155000, 240000, 360000, 440000, 570000])  # preços com variação


modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)


mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")

from sklearn.metrics import r2_score

r2 = r2_score(y, y_pred)
print(f"R²: {r2:.4f}")
# R² = 1.0 significa que o modelo explica 100% da variância
```

> Vide [004_R2.py](./004_R2.py)

5. **Mean Absolute Percentage Error (MAPE)**

$$MAPE = \frac{100\%}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

Erro percentual médio. Útil quando você quer comparar erros em escala percentual.

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Dados de exemplo com ruído
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([155000, 240000, 360000, 440000, 570000])  # preços com variação


modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)


mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")

from sklearn.metrics import mean_absolute_percentage_error

mape = mean_absolute_percentage_error(y, y_pred)
print(f"MAPE: {mape:.4f}")
# Se MAPE = 0.05, o modelo erra em média 5%
```

> Vide [005_MAPE.py](./005_MAPE.py)

## **Métricas dos modelos de Classificação e Agrupamento**

A classificação é um modelo de aprendizado supervisionado que busca prever **categorias discretas** (ex: spam/não-spam, aprovado/reprovado, gato/cachorro). O objetivo é atribuir cada amostra a uma classe entre as possíveis.

**Tipos principais:**

- **Classificação Binária**: duas classes (sim/não, positivo/negativo)
- **Classificação Multiclasse**: mais de duas classes
- **Classificação Multilabel**: múltiplas classes por amostra

### Métricas de Avaliação em Classificação

**Conceitos Iniciais: Matriz de Confusão**

A matriz de confusão serve para responder:
"Quão bem o modelo está classificando cada categoria?"<br>
Para isso ela compara as previsões do modelo com os dados obsrvados gerando quatro possíveis elementos:
| Predito Positivo | Predito Negativo |
| -- | -- |
| Verdadeiro Positivo (TP) | Falso Negativo (FN) |
| Falso Positivo (FP) | Verdadeiro Negativo (TN) |

A partir da matriz conseguimos calcular **métricas**

```python
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
import numpy as np

# Dados: diagnóstico de doença (1=doente, 0=saudável)
X = np.array([[2.5], [3.2], [1.8], [4.1], [2.9], [3.5], [1.5], [4.3]])
y_true = np.array([0, 1, 0, 1, 0, 1, 0, 1])

# Treinar modelo
modelo = LogisticRegression()
modelo.fit(X, y_true)
y_pred = modelo.predict(X)

# Matriz de confusão
cm = confusion_matrix(y_true, y_pred)
print("Matriz de Confusão:")
print(cm)
# [[TN  FP]
#  [FN  TP]]
```

> Vide [006_confusao.py](./006_confusao.py)

#### 1. **Acurácia (Accuracy)**

$$Acurácia = \frac{TP + TN}{TP + TN + FP + FN}$$

Serve para calcular quantas previsões do modelo estavam corretas. Pode ser enganosa em datasets desbalanceados.

```python
# Importando bibliotecas necessárias
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# 1. Carregar um dataset de exemplo (Iris)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Treinar um modelo simples (Árvore de Decisão)
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# 4. Fazer previsões
y_pred = modelo.predict(X_test)

# 5. Gerar a matriz de confusão
matriz_confusao = confusion_matrix(y_test, y_pred)

# 6. Calcular a acurácia
acuracia = accuracy_score(y_test, y_pred)

# 7. Exibir resultados
print("Matriz de Confusão:")
print(matriz_confusao)
print("\nAcurácia do modelo:", acuracia)
```

> Vide [007_acuracy.py](./007_acuracy.py)<br>
> Uma acurácia perfeita também pode indicar **overfitting**.

#### 2. **Precisão (Precision)**

$$Precisão = \frac{TP}{TP + FP}$$

Responde à pergunta: **entre os casos classificados como positivos, quantos realmente eram positivos?** É importante quando um falso positivo tem um custo alto, como marcar uma pessoa saudável como doente.

Neste exemplo, a classe positiva é `1` (caso de câncer). O `precision_score` calcula a precisão dessa classe.

```python
# Importando as bibliotecas necessárias
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Carregar um dataset de diagnóstico de câncer
dados = load_breast_cancer()
X = dados.data
y = (dados.target == 0).astype(int)  # 1 = maligno, 0 = benigno

# 2. Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Padronizar as features para facilitar o treinamento
padronizador = StandardScaler()
X_train = padronizador.fit_transform(X_train)
X_test = padronizador.transform(X_test)

# 4. Treinar o modelo e fazer previsões
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# 5. Calcular a precisão e exibir os resultados
precisao = precision_score(y_test, y_pred)
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))
print(f"Precisão: {precisao:.4f}")
```

> Vide [008_precisao.py](./008_precisao.py)

Se a precisão for `0.80`, significa que 80% das previsões positivas estavam corretas. Ela não informa quantos positivos reais deixaram de ser encontrados; para isso, usamos o **recall**.

#### 3. **Recall (Sensibilidade)**

$$Recall = \frac{TP}{TP + FN}$$

Responde à pergunta: **entre todos os casos que realmente eram positivos, quantos o modelo encontrou?** É importante quando um falso negativo é perigoso, como deixar de identificar uma doença.

```python
# Importando as bibliotecas necessárias
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Carregar os dados
dados = load_breast_cancer()
X = dados.data
y = (dados.target == 0).astype(int)  # 1 = maligno, 0 = benigno

# 2. Separar dados para treino e teste, mantendo a proporção das classes
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Padronizar os dados sem deixar o conjunto de teste influenciar o treino
padronizador = StandardScaler()
X_train = padronizador.fit_transform(X_train)
X_test = padronizador.transform(X_test)

# 4. Treinar o modelo e fazer previsões
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# 5. Calcular o recall e exibir os resultados
recall = recall_score(y_test, y_pred)
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))
print(f"Recall: {recall:.4f}")
```

> Vide [009_recall.py](./009_recall.py)

Um recall de `0.90` significa que o modelo encontrou 90% dos casos positivos reais. Ele pode, porém, gerar muitos falsos positivos. Por isso, normalmente analisamos recall junto com precisão.

#### 4. **F1-Score**

$$F1 = 2 \times \frac{Precisão \times Recall}{Precisão + Recall}$$

O F1-Score é a média harmônica entre precisão e recall. Ele só será alto quando as duas métricas também forem altas. É uma boa opção quando existe desbalanceamento entre as classes ou quando falsos positivos e falsos negativos são importantes.

```python
# Importando as bibliotecas necessárias
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Carregar os dados
dados = load_breast_cancer()
X = dados.data
y = (dados.target == 0).astype(int)  # 1 = maligno, 0 = benigno

# 2. Separar dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Padronizar as features usando somente os dados de treino
padronizador = StandardScaler()
X_train = padronizador.fit_transform(X_train)
X_test = padronizador.transform(X_test)

# 4. Treinar o modelo e fazer previsões
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# 5. Calcular as três métricas para comparar seus resultados
precisao = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Precisão: {precisao:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
```

> Vide [010_f1_score.py](./010_f1_score.py)

O F1-Score não substitui a análise das outras métricas: ele resume o equilíbrio entre elas, mas não mostra se o modelo está falhando mais por falsos positivos ou por falsos negativos.

#### 5. **ROC-AUC (Area Under the Curve)**

A curva ROC mostra a relação entre a **taxa de verdadeiros positivos** e a **taxa de falsos positivos** quando variamos o limite (threshold) usado pelo modelo. A AUC é a área sob essa curva:

- `1.0`: separação perfeita entre as classes;
- `0.5`: desempenho semelhante ao acaso;
- abaixo de `0.5`: o modelo está fazendo previsões invertidas ou separando mal as classes.

Para construir a curva, usamos probabilidades (`predict_proba`) e não apenas as classes finais retornadas por `predict`.

```python
# Importando as bibliotecas necessárias
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Carregar os dados
dados = load_breast_cancer()
X = dados.data
y = (dados.target == 0).astype(int)  # 1 = maligno, 0 = benigno

# 2. Separar dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Padronizar as features
padronizador = StandardScaler()
X_train = padronizador.fit_transform(X_train)
X_test = padronizador.transform(X_test)

# 4. Treinar o modelo
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# 5. Obter a probabilidade de cada amostra pertencer à classe positiva
y_pred_proba = modelo.predict_proba(X_test)[:, 1]

# 6. Calcular os pontos da curva ROC e o valor da AUC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC: {roc_auc:.4f}")

# 7. Visualizar a curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f"Modelo (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], "k--", label="Classificador aleatório")
plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.title("Curva ROC")
plt.legend()
plt.show()
```

> Vide [011_roc_auc.py](./011_roc_auc.py)

Uma AUC alta indica que o modelo consegue ordenar os exemplos positivos acima dos negativos. Ela avalia a capacidade geral de separação e não escolhe, sozinha, o melhor threshold para a aplicação.

### Exemplo Completo de Classificação

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score, precision_score, recall_score, f1_score)
import pandas as pd

# Carregar dados: classificar tipos de íris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Previsões
y_pred = modelo.predict(X_test)

# Calcular métricas
print("=== MÉTRICAS INDIVIDUAIS ===")
print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precisão (média): {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall (média): {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1-Score (média): {f1_score(y_test, y_pred, average='weighted'):.4f}")

print("\n=== MATRIZ DE CONFUSÃO ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== RELATÓRIO DE CLASSIFICAÇÃO ===")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

> Vide [012_classificacao_completa.py](./012_classificacao_completa.py)

---

### Teoria Básica de Agrupamento (Clustering)

O agrupamento é um modelo de aprendizado **não-supervisionado** que busca dividir dados em grupos similares sem rótulos prédefinidos. O objetivo é encontrar estruturas naturais nos dados.

**Tipos principais:**

- **K-Means**: agrupa baseado em centróides
- **DBSCAN**: agrupa por densidade
- **Hierarchical Clustering**: agrupa hierarquicamente

### Métricas de Avaliação em Agrupamento

Como não há rótulos verdadeiros, as métricas avaliam qualidade interna (coesão e separação).

#### 1. **Silhueta (Silhouette Score)**

$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

Varia de -1 a 1. Valores próximos de 1 indicam clusters bem definidos.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# Dados: características de clientes
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Treinar K-Means
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X)

# Calcular Silhueta
silhueta = silhouette_score(X, labels)
print(f"Silhueta: {silhueta:.4f}")
# Silhueta > 0.5: clusters bem separados
# Silhueta < 0.25: clusters sobrepostos
```

> Vide [013_silhueta.py](./013_silhueta.py)

#### 2. **Davies-Bouldin Index**

Mede a razão média entre a dispersão dentro dos clusters e a separação entre clusters. Valores menores são melhores (0 é perfeito).

```python
from sklearn.metrics import davies_bouldin_score

db_index = davies_bouldin_score(X, labels)
print(f"Davies-Bouldin Index: {db_index:.4f}")
# Valores baixos indicam melhor agrupamento
```

> Vide [014_davies_bouldin.py](./014_davies_bouldin.py)

#### 3. **Calinski-Harabasz Index**

Razão entre dispersão entre clusters e dispersão dentro clusters. Valores maiores indicam melhor agrupamento.

```python
from sklearn.metrics import calinski_harabasz_score

ch_index = calinski_harabasz_score(X, labels)
print(f"Calinski-Harabasz Index: {ch_index:.4f}")
# Valores altos indicam clusters bem separados e compactos
```

> Vide [015_calinski_harabasz.py](./015_calinski_harabasz.py)

#### 4. **Inércia (Within-cluster sum of squares)**

Soma das distâncias de cada ponto ao seu centróide. Valores menores são melhores, mas tende a diminuir com mais clusters.

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

inertia = kmeans.inertia_
print(f"Inércia: {inertia:.4f}")
```

> Vide [016_inercia.py](./016_inercia.py)

### Exemplo Completo de Agrupamento

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Criar dados sintéticos: clientes com renda e gastos
np.random.seed(42)
cluster_1 = np.random.normal([30000, 10000], [5000, 2000], 50)
cluster_2 = np.random.normal([80000, 40000], [10000, 5000], 50)
X = np.vstack([cluster_1, cluster_2])

# Normalizar dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Testar diferentes números de clusters
inercias = []
silhuetas = []
n_clusters_range = range(2, 8)

for n in n_clusters_range:
    kmeans = KMeans(n_clusters=n, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)

    inercia = kmeans.inertia_
    silhueta = silhouette_score(X_scaled, labels)

    inercias.append(inercia)
    silhuetas.append(silhueta)

    print(f"K={n}: Inércia={inercia:.2f}, Silhueta={silhueta:.4f}")

# Escolher K ótimo (onde Silhueta é máxima)
k_otimo = n_clusters_range[np.argmax(silhuetas)]
print(f"\n✓ K ótimo: {k_otimo}")

# Modelo final com K ótimo
kmeans_final = KMeans(n_clusters=k_otimo, random_state=42, n_init=10)
labels_final = kmeans_final.fit_predict(X_scaled)

print(f"\n=== MÉTRICAS COM K ÓTIMO ===")
print(f"Silhueta: {silhouette_score(X_scaled, labels_final):.4f}")
print(f"Davies-Bouldin: {davies_bouldin_score(X_scaled, labels_final):.4f}")
print(f"Calinski-Harabasz: {calinski_harabasz_score(X_scaled, labels_final):.4f}")

# Visualizar clusters
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels_final, cmap='viridis', marker='o')
centroides = scaler.inverse_transform(kmeans_final.cluster_centers_)
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='X', s=200, label='Centróides')
plt.xlabel('Renda')
plt.ylabel('Gastos')
plt.title(f'Agrupamento de Clientes (K={k_otimo})')
plt.legend()
plt.show()
```

> Vide [017_agrupamento_completo.py](./017_agrupamento_completo.py)

---

### Resumo Comparativo: Quando Usar Cada Métrica

| Modelo            | Métrica           | Quando Usar            | Interpretação                          |
| ----------------- | ----------------- | ---------------------- | -------------------------------------- |
| **Regressão**     | RMSE              | Sempre                 | Erro médio em unidades originais       |
|                   | R²                | Sempre                 | Proporção de variância explicada (0-1) |
|                   | MAE               | Dados com outliers     | Erro absoluto médio                    |
| **Classificação** | Acurácia          | Classes balanceadas    | Proporção de acertos                   |
|                   | Precisão          | FP custoso             | Taxa de positivos corretos             |
|                   | Recall            | FN custoso             | Taxa de detecção positiva              |
|                   | F1-Score          | Classes desbalanceadas | Balanço precisão-recall                |
|                   | ROC-AUC           | Comparar modelos       | Capacidade discriminativa              |
| **Agrupamento**   | Silhueta          | Sempre                 | Qualidade de separação (-1 a 1)        |
|                   | Davies-Bouldin    | Sempre                 | Compacidade (menor=melhor)             |
|                   | Calinski-Harabasz | Sempre                 | Separação (maior=melhor)               |
