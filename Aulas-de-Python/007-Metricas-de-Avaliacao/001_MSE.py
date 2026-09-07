from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Dados de exemplo: preço da casa vs tamanho
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([150000, 250000, 350000, 450000, 550000])  # preço em reais

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_pred = modelo.predict(X)

# Calcular MSE
mse = mean_squared_error(y, y_pred)
print(f"MSE: {mse:.2f}")