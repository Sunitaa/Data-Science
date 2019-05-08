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

#for decesion tree
from sklearn import tree


#for i/o operations
import io

#used for visualizations
import pydot

print (pd.__version__)

titanic_train = pd.read_csv("C:/Data Science/Titanic_disaster/train.csv") 

#build the decision tree model
x_titanic_train = titanic_train[['Pclass', 'SibSp', 'Parch' ]]
y_titanic_train = titanic_train[['Survived']]
dt = tree.DecisionTreeClassifier()
dt.fit(x_titanic_train, y_titanic_train)


# visulaize the decision tree
objStringIO = io.StringIO()
tree.export_graphviz(dt, out_file = objStringIO, feature_names = x_titanic_train.columns)
graph = pydot.graph_from_dot_data(objStringIO.getvalue()) 
os.chdir("C:/Data Science/Titanic_disaster/");
graph[0].write_pdf("DecisionTree.pdf")

# pdf contains the decision tree diagram has nodes based on the feature names 
# with all possible combinations based on their values 
# with following information in every node:
# condition based on column values (SipSp <= 1.5)
# gini (gini = 0.451)
# total numnber of rows (sample = 891)
# result having non_survived, survived value => 400 non-survived, 491 survived (value = [400,491])

# leaves will have either (0,non_zero) in one of the survived/non-survived category or
# there is no enough data to go further from this node, and thats why the result is 0.68 and not 1
# more data with more combination gives better results

