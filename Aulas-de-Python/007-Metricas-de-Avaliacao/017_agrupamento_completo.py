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
