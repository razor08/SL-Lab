import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('titanic.csv')

df1 = df1.drop(['Ticket'], 1)

df1['Cabin'] = df1.fillna('NOPE')

print("Number of entries,  Attributes:", df1.shape)

print(df1.keys())

print(df1.dtypes)

print('Max Age: ', df1['Age'].max())
print('Min Age: ', df1['Age'].min())
print('Mean Age: ', df1['Age'].mean())

x = df1.plot()
x.set_xlabel('Age')
x.set_ylabel('Number of People')
plt.show(block=True)