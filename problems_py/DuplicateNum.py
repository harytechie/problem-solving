num=[2,33,5,5,6,4,4,33]
l=[]
for i in num:
    if num.count(i)>1 and i not in l:
        l.append(i)
print(l)