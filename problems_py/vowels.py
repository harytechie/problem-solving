a="hello every one"
v=0
c=0
ch=(list(a))
for i in ch:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v+=1
    elif(i==' '):
        pass
    else:
        c+=1
    
print("vowels : ",v)
print("consonets : ",c)
