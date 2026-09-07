from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Carregar dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Treinar modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

# 3. Exportar a lógica da árvore em texto
regras = export_text(modelo, feature_names=iris.feature_names)

# 4. Imprimir regras
print("Regras da Árvore de Decisão:")
print(regras)

# Para impressão gráfica
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plot_tree(modelo, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()