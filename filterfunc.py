a=[1,2,3,4,5,6,7,8,9,10,45]
def data(x):
      if x>20:
        return x 
result = filter(data,a)
print(list(result))