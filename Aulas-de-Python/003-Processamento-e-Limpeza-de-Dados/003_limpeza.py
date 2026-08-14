import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df[['PassengerId', 'Name', 'Age']].head(10))

print("-" * 30)

# Calculando a média
mean_age = df['Age'].mean()
# Preenchendo valores ausentes com a média
df['Age'] = df['Age'].fillna(mean_age)

print(df[['PassengerId', 'Name', 'Age']].head(10))



