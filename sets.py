s={"apple","orange","banana",'kiwi','mango'}
for x in s:
    print(x)
s.add('pineapple')
print(s)
s.update(['Dragon fruit','star fruit','strawberry'])
print(s)
a = { 'aston martin','banana','mango','BMW','MERCEDES'}
y=s.difference(a)
print(y)
z=s.intersection(a)
print(z)