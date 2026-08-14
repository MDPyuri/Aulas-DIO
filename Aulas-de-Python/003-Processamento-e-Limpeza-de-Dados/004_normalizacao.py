import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['Age_norm'] = scaler.fit_transform(df[['Age']])
print(df[['Age', 'Age_norm']].head(20))

