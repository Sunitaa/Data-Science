# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list1 = [1,2,3]
print(type(list1))
print (list1)

tuple = (10, "str", 12.2)
print (type(tuple))
print (tuple)

#should give an error as it is read only
#tuple.pop()

dict = {'Height':10, "Age":12.2}
print (type(dict))
print (dict)

print (dict['Height'])
print (dict['Age'])

dict['Age'] = 20

print (dict.keys())
print (dict.items())
print (dict.values())

print (dict)

