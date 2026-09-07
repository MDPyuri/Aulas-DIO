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
