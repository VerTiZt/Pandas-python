import pandas as pd

data = pd.read_csv('train.csv')

statistic = data.groupby(['Pclass', 'Sex'])['Survived'].value_counts().unstack().fillna(0)
print(statistic)
