#creating and using functions

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
