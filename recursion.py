def factorial(x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=9
print("The factorial of",num,"is",factorial(num))