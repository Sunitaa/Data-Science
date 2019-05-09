# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:08:14 2019

@author: sunita
"""
#for os operations , csw, change directory
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#for data frames
import pandas as pd

print (pd.__version__)

titanic_train = pd.read_csv("C:/Data Science/Titanic_disaster/train.csv") 

titanic_train.shape
titanic_train.info()
titanic_train.describe()

# we need to use one hot encoding: 
# -in order to neutralize the data
# -if the data is not in numbers (categorical)

#Transformation of non numneric cloumns to 1-Hot Encoded columns
#Transform categoric to One hot encoding using get_dummies
titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.head(10)
titanic_train1.info()
titanic_train1.describe()
