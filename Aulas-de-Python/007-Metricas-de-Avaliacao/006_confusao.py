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