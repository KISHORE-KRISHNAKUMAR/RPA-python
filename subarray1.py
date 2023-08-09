a = [-2, -3, 4, -1, -2, 1, 5, -3]
res=[]
subarray=[]
for i in range(len(a)):
    for  j in range(len(a)):
        res.append(sum(a[i:j]))
        subarray.append(a[i:j])
        

print(subarray)
print((max(res)))
print(res.index(max(res)))
print(subarray[res.index(max(res))])
print(max(res))
