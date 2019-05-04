#understanding basic types
#types are inferred in runtime automatically

a = 10
print(a)
print(type(a))

b = 13.6
print(type(a))

c = 'abc'
print(type(a))

e = False 
print(a)
print(type(a))


#Basic List containers

#For lists use [] brackets
list1 = [10,20,30]
print(type(list1))

list2=['abc', 10, True]
print(type(list2))

#access list elements by slicing
print(list1[0])
print(list1[0:2])
print(list1[2:3])

list1[2] = 100
print(list1)

list1.append(1) 
print(list1)

#extend expects a value/collection of values
list1.extend([10, 20])
list1.extend(list2)

#pop is for removing by index
list1.pop(1)
print(list1)
list3 = [list1, 60, list2]
len(list3)

#Tuples (Read only list)
test = [10,20,30]

tuple1 = (3,4,6)
print(type(tuple1))

#access tuple elements by slicing
print(tuple1[0])
print(tuple1[0:5])
print(tuple1[2:3])

#TypeError: 'tuple' object does not support item assignment being it is READ ONLY
tuple1[2] = 100 
print(tuple1)

tuple2 = (10, 20, (40,50), True)
len(tuple2)

#should give an error as it is read only
#tuple2.pop()


#Dictionaries are Key Value pairs
#Dictionary will be represented using {flower brackets} 

dict1 =  {'Height':10, 'Width':20}
type(dict1)

#access elements by key
print(dict1['Height'])
print(dict1['Width'])

#Alternate way to access elements by key
print(dict1.get('Height'))
print(dict1.get('Width'))

#Replace width value
dict1['Width'] = 50

#Access keys
print(dict1.keys())

#Access both key values pairs
print(dict1.items())
