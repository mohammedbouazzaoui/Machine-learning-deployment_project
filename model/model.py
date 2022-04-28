# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:12:19 2022

@author: bmadmin
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read data
#
df = pd.read_csv("../data/data_homes_cleaned.csv")


df=df[['classified.zip','classified.price','classified.building.constructionYear']]


# prepare
# finalclean
df=df.dropna()

#
X=df[['classified.zip','classified.building.constructionYear']]
y=df[['classified.price']]
#print(X,y)
'''
# How to use `sklearn` now with multiple features ? Well, it's simple, you don't change anything. `sklearn` takes care of everything for you.

1. Import `LinearRegression` from `sklearn`
2. Create a `regressor` variable and instantiate your `LinearRegression` class.
3. Train your model with `X_train` and `y_train`.
4. Display the score of your model with `X_train` and `y_train`.
5. Use the predict method of your model on your test dataset (`X_test`).
6. Display the score of your model with `X_test` and `y_test`.
'''
print(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=33, train_size=0.8)

from sklearn.linear_model import LinearRegression
#X_train=X_train.reshape(-1, 1)
#y_train=y_train.reshape(-1, 1)
regressor=LinearRegression().fit(X_train,y_train)

print("regressor score:",regressor.score(X_train, y_train))


ypred=regressor.predict(X_test)
#X_test
#ypred


plt.scatter(X_test['classified.zip'], ypred,color='green')
plt.scatter(X_test['classified.building.constructionYear'], ypred,color='blue')
plt.xlabel('X Label')
plt.ylabel('Y Label')
