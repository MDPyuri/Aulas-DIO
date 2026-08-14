import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Carregar dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" 
df = pd.read_csv(url)
# Preencher valores ausentes em Age com a média
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Visualização de outliers usando boxplot
plt.boxplot(df['Age'])
plt.title("Boxplot de Idade - Outliers")
plt.show()

# Calcular Z-score para a coluna 'Age'
z_scores = stats.zscore(df['Age'])

# Identificar outliers (Z-score > 3 ou < -3)
outliers = df[(z_scores > 3) | (z_scores < -3)]

print("Outliers identificados:")
print(outliers[['PassengerId', 'Name', 'Age']])