# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

# Фильтруем данные по выживаемости
survived = data[data['Survived'] == 1]['Age'].dropna()
not_survived = data[data['Survived'] == 0]['Age'].dropna()

plt.figure(figsize=(10, 6))
plt.hist(survived, bins=30, alpha=0.5, label='Выжили', color='g')
plt.hist(not_survived, bins=30, alpha=0.5, label='Не выжили', color='r')

plt.title('Гистограмма зависимости возраста от выживаемости')
plt.xlabel('Возраст (в годах)')
plt.ylabel('Количество пассажиров')
plt.legend()
plt.show()
