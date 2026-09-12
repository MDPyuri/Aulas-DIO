import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
import shap

df = pd.read_csv("./Complementos/creditcard.csv")

# print(df.head)

print("\n\033[34mBalance:\033[0m")
print(df["Class"].value_counts(normalize=True))

df["Amount_log"] = np.log1p(df["Amount"])

scaler = StandardScaler()
df["Amount_scaled"] = scaler.fit_transform(df[["Amount"]])

x = df.drop("Class", axis=1)
y = df["Class"]

x_train, x_test, y_train, y_test = train_test_split(
  x, y, stratify=y, test_size=0.3, random_state=42
)

# Modelo de regressão Logistica 
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("\n\033[34mClassificantion Report:\033[0m")
print(classification_report(y_test, y_pred))

y_probs = model.predict_proba(x_test)[:,1]

fpr, tpr, _ = roc_curve(y_test, y_probs)

plt.plot(fpr, tpr)
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

print("AUC:", roc_auc_score(y_test, y_probs))

#Precision Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_probs)

plt.plot(recall, precision)
plt.title("Precision-Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()

# Balanceamento Undersampling
fraudes = df[df["Class"] == 1]
normais = df[df["Class"] == 0].sample(len(fraudes), random_state=42)

df_under = pd.concat([fraudes, normais])

# Balanceamento Oversampling
# Aplicando SMOTE para balancear os dados
smote = SMOTE(random_state=42)
x_res, y_res = smote.fit_resample(x, y)

# Divisão treino/teste no dataset balanceado
x_train_res, x_test_res, y_train_res, y_test_res = train_test_split(
    x_res, y_res, stratify=y_res, test_size=0.3, random_state=42
)

# Treinando novamente o modelo
model_res = LogisticRegression(max_iter=1000)
model_res.fit(x_train_res, y_train_res)
y_pred_res = model_res.predict(x_test_res)

# Relatório de classificação
print("\n\033[34mClassification Report (com SMOTE):\033[0m")
print(classification_report(y_test_res, y_pred_res))

# Probabilidades para métricas
y_probs_res = model_res.predict_proba(x_test_res)[:,1]

# Curva ROC
fpr_res, tpr_res, _ = roc_curve(y_test_res, y_probs_res)
plt.plot(fpr_res, tpr_res)
plt.title("ROC Curve (com SMOTE)")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

print("AUC (com SMOTE):", roc_auc_score(y_test_res, y_probs_res))

# Curva Precision-Recall
precision_res, recall_res, _ = precision_recall_curve(y_test_res, y_probs_res)
plt.plot(recall_res, precision_res)
plt.title("Precision-Recall Curve (com SMOTE)")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()


# Modelo com Random Forest
rf = RandomForestClassifier(
  n_estimators=50,
  max_depth=10,
  class_weight="balanced",
  n_jobs=-1,
  random_state=42
)

rf.fit(x_train, y_train)

y_pred_rf = rf.predict(x_test)

print("\n\033[34mClassification Report (Random Forest):\033[0m")
print(classification_report(y_test, y_pred_rf))

estimator = rf.estimators_[0]

plt.figure(figsize=(20,10))
plot_tree(estimator, filled=True, feature_names=x.columns, class_names=["Normal","Fraude"])
plt.show()

# Utilizando pipeline
pipeline = Pipeline([
  ("scaler", StandardScaler()),
  ("model", LogisticRegression(max_iter=1000))
])

pipeline.fit(x_train, y_train)

y_pred = pipeline.predict(x_test)
y_probs_pipeline = pipeline.predict_proba(x_test)[:, 1]

threshold = 0.3

y_pred_custom = (y_probs_pipeline > threshold).astype(int)

print("\n\033[34mClassification Report (Pipeline com threshold 0.3):\033[0m")
print(classification_report(y_test, y_pred_custom))

# Utilizando XGBoost
xgb = XGBClassifier(
  scale_pos_weight=10, # Ajuda com desbalanceamento
  use_label_encoder=False,
  eval_metric="logloss"
)

xgb.fit(x_train, y_train)

y_pred_xgb = xgb.predict(x_test)

print("\n\033[34mClassification Report (XGBoost):\033[0m")
print(classification_report(y_test, y_pred_xgb))

# Exposição da importância das variáveis envolvidas
importancias = xgb.feature_importances_

plt.bar(range(len(importancias)), importancias)
plt.title("Importâmcia das Variáveis")
plt.show()

# ajustando hiperparâmetros
param_grid = {
  "max_depth": [3, 5],
  "n_estimators": [50, 100]
}

grid = GridSearchCV(
  XGBClassifier(eval_metric="logloss"),
  param_grid,
  scoring="recall",
  cv=3
)

grid.fit(x_train, y_train)
print("Melhor Modelo:", grid.best_params_)

# SHAP
explainer = shap.Explainer(xgb)
shap_values = explainer(x_test[:100])

shap.plots.bar(shap_values)