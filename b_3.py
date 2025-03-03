# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('train.csv')

# Группировка по порту посадки и вычисление средней выживаемости
port_survival = data.groupby('Embarked')['Survived'].mean().reset_index()

print(port_survival)
