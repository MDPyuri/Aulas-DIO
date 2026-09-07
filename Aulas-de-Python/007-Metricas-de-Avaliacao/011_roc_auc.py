# Importando as bibliotecas necessárias
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Carregar os dados
dados = load_breast_cancer()
X = dados.data
y = (dados.target == 0).astype(int)  # 1 = maligno, 0 = benigno

# 2. Separar dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Padronizar as features
padronizador = StandardScaler()
X_train = padronizador.fit_transform(X_train)
X_test = padronizador.transform(X_test)

# 4. Treinar o modelo
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# 5. Obter a probabilidade de cada amostra pertencer à classe positiva
y_pred_proba = modelo.predict_proba(X_test)[:, 1]

# 6. Calcular os pontos da curva ROC e o valor da AUC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC: {roc_auc:.4f}")

# 7. Visualizar a curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f"Modelo (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], "k--", label="Classificador aleatório")
plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.title("Curva ROC")
plt.legend()
plt.show()
