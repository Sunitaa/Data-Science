# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:00:29 2019

@author: sunita
"""

def add(a,b):
    return a+b
    
print(add(1,2))

#optional arguments having default values
def add(a,b,c=20,d=40):
    return a+b+c+d

print(add(1,2,3))

def calculateInterest(rate,base):
    return rate*base

print(calculateInterest(0.02,100))