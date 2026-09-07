from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Dados de exemplo com ruído
X = np.array([[50], [100], [150], [200], [250]])  # tamanho em m²
y = np.array([155000, 240000, 360000, 440000, 570000])  # preços com variação


modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)


mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")

from sklearn.metrics import mean_absolute_percentage_error

mape = mean_absolute_percentage_error(y, y_pred)
print(f"MAPE: {mape:.4f}")
# Se MAPE = 0.05, o modelo erra em média 5%