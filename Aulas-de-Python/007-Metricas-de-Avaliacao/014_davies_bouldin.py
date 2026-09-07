from sklearn.metrics import davies_bouldin_score
from sklearn.cluster import KMeans
import numpy as np

# Dados: características de clientes
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Treinar K-Means para obter os rótulos dos grupos
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X)

# Calcular o índice Davies-Bouldin
db_index = davies_bouldin_score(X, labels)
print(f"Davies-Bouldin Index: {db_index:.4f}")
# Valores baixos indicam melhor agrupamento
