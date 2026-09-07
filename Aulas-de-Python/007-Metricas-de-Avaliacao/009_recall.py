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
