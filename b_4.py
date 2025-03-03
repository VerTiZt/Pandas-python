# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('train.csv')

top_names = data['Name'].str.split(', ').str[1].str.split(' ').str[1].value_counts().head(10)
print("Топ 10 популярных имён:")
print(top_names)

top_surnames = data['Name'].str.split(', ').str[0].value_counts().head(10)
print("\nТоп 10 популярных фамилий:")
print(top_surnames)
