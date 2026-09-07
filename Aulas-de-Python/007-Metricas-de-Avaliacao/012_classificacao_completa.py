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
