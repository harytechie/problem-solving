num=[1,2,3,4,5,6,7]
target=int(input())
result=[]
for i in range (len(num)):
    for j in range(i+1,len(num)):
        for k in range(i+2,len(num)):
            if(num[i]+num[j]+num[k]==target):
                result.append([i,j,k])
print(result)