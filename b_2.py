# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('train.csv')

# Разделение данных по полу
male_stats = data[data['Sex'] == 'male'].describe()
female_stats = data[data['Sex'] == 'female'].describe()

print("Статистика для мужчин:\n", male_stats)
print("\nСтатистика для женщин:\n", female_stats)
