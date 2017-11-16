import pandas as pd

dataset = pd.read_csv('titanic_dataset.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

print(X)
print(y)