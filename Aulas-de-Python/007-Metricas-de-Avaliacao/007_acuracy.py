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
