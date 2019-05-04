name = "sunita"
surname = 'verma'

print (type(name))
print (type(surname))

#TypeError: 'str' object does not support item assignment
#as string is immutable
#name [0] = 'T' 

name2 = name + 'Hyd'
print(name2)


name = name.upper()

name = name.capitalize()

name = name + surname

name = name.replace('sunita',' Sunita')

print (name)


isinstance(name, str)

isinstance(name, int)


name = 10

isinstance(name, str)

isinstance(name, int)

