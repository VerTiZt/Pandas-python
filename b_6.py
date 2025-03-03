# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('test.csv')

# Предварительная обработка данных
data.ffill(inplace=True)

data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Выбор признаков
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = data[features].copy()

# Нормализация признаков
X.loc[:, 'Age'] = (X['Age'] - X['Age'].mean()) / X['Age'].std()
X.loc[:, 'Fare'] = (X['Fare'] - X['Fare'].mean()) / X['Fare'].std()

# На основе медианных значений
data['Predicted_Survived'] = 0
data.loc[(X['Fare'] > 0) & (X['Sex'] == 1), 'Predicted_Survived'] = 1  # критерий для демо-целей

# Сбор результатов
results = data[['PassengerId', 'Predicted_Survived']]
results.to_csv('predictions.csv', index=False)

print("Предсказания сохранены в файл predictions.csv")
