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
