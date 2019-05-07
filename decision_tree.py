# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:08:14 2019

@author: sunita
"""

import os

#for data frames
import pandas as pd

#for decesion tree
from sklearn import tree

print (pd.__version__)
# =============================================================================
# multi line comment ctrl+4
# THis is a multi line comment
# Would be commented out using
# ctrl+f4
# =============================================================================

titanic_train = pd.read_csv("C:/Data Science/Titanic_disaster/train.csv") 

#build the decision tree model
x_titanic_train = titanic_train[['Pclass', 'SibSp', 'Parch' ]]
y_titanic_train = titanic_train[['Survived']]
dt = tree.DecisionTreeClassifier()
dt.fit(x_titanic_train, y_titanic_train)

#predict the Survived column values in the test data
titanic_test = pd.read_csv("C:/Data Science/Titanic_disaster/test.csv") 
x_titanic_test = titanic_test[['Pclass', 'SibSp', 'Parch']]
titanic_test['Survived'] = dt.predict(x_titanic_test)

#write the results to submission_titanic.csv file
os.chdir("C:/Data Science/Titanic_disaster")
os.getcwd()
titanic_test.to_csv("submission_titanic.csv", columns=['PassengerId', 'Survived'], index=False)