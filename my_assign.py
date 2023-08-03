file = str(input('ENTER YOR FILE NAME:'))
op = ['!' , '@' ,'#','$','%','^','&','*','(',')','[',']',"'",';',':','<','>','.',',','/','|','+','-','_']
sp=[]
myfile = open(file,"r")
Q=myfile.read()
print(Q)
#str(Q)
print(list(Q))
b=list(Q)
L= len(b)
for i in Q:
    if (i==',' or i== '.' or i=="'" or i== "-" or i==' ') :
        sp.append(i)
print(sp)
print("special characters in quotes:",len(sp))
       
#sp = Q.split(",")
#print(sp)
#d=set(b)
#print(d)
#print('LENGTH OF THE QUOTE IS:',len(b))

    
#print(b)
#print(c)
#for i in b
