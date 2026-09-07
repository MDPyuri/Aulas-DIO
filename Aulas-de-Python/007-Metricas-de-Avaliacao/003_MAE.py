from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de exemplo com ruído
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([155000, 240000, 360000, 440000, 570000])  # preços com variação

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_pred = modelo.predict(X)

# Calcular MSE e RMSE
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")

# MSE: 118000000.00
# RMSE: 10862.78

mae = mean_absolute_error(y, y_pred)
print(f"MAE: {mae:.2f}")
# Se MAE = 10000, o modelo erra em média R$ 10.000