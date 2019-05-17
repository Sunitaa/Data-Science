# -*- coding: utf-8 -*-
"""
Model tuning
@author: Sunita
"""

import pandas as pd
from sklearn import tree
from sklearn import model_selection
import io
import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#returns current working directory
os.getcwd()

#changes working directory
os.chdir("C:/Data Science/Titanic_disaster")

titanic_train = pd.read_csv("train.csv")
print(type(titanic_train))

titanic_train.shape
titanic_train.info()

#Apply one hot encoding
titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.info()
x_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket', 'Name','Survived'], 1)
y_train = titanic_train['Survived']

# creating a decison tree
dt1 = tree.DecisionTreeClassifier()

# fit with result column in train data
dt1.fit(x_train,y_train)

# Apply K-fold technique and find out the Cross Validation(CV) score.
cv_scores1 = model_selection.cross_val_score(dt1, x_train, y_train, cv=10)
print(cv_scores1) #Return type is a [List] of score
print(cv_scores1.mean()) #Find out the mean of CV scores
print(dt1.score(x_train,y_train))

#tune model manually by passing differnt values for decision tree arguments
dt2 = tree.DecisionTreeClassifier(max_depth=4) #Here we passed max-depth as argument to the tree
dt2.fit(x_train,y_train)
cv_scores2 = model_selection.cross_val_score(dt2, x_train, y_train, cv=10)
print(cv_scores2) #Return type is a [List] of scores
print(cv_scores2.mean())

print(dt2.score(x_train,y_train))

#Automate model tuning process. Use Grid search method
dt3 = tree.DecisionTreeClassifier()
param_grid = {'max_depth':[5,8,10], 'min_samples_split':[2,4,5], 'criterion':['gini','entropy']} 
print(param_grid)
#max_depth means: Max depth of the tree to child nodes
#min_samples_split means: sample shown in a particular node should be >= min sample size
dt3_grid = model_selection.GridSearchCV(dt3, param_grid, cv=10, n_jobs=5)
dt3_grid.fit(x_train, y_train)

print(dt3_grid.cv_results_) 
final_model = dt3_grid.best_estimator_ #This is the estimator of max_depth and min_sample_split combination
print(dt3_grid.best_score_)
#.score gives the score on full train data
print(dt3_grid.score(x_train, y_train))

dot_data = io.StringIO() 
tree.export_graphviz(final_model, out_file = dot_data, feature_names = x_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("Tuned_DT.pdf")