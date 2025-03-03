# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('train.csv')

# Выбор только числовых столбцов
numeric_data = data.select_dtypes(include=['number'])

# Заполнение отсутствующих значений медианой по числовым столбцам
data[numeric_data.columns] = numeric_data.fillna(numeric_data.median())
