from functools import reduce
data =[1,2,3,4,5]
mul=reduce(lambda x,y:x*y,data)
print(mul)