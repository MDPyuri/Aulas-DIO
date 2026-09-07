from sklearn.cluster import KMeans
import numpy as np

# Dados: características de clientes
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Treinar K-Means
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Obter a soma das distâncias aos centróides
inertia = kmeans.inertia_
print(f"Inércia: {inertia:.4f}")
