arr=[1,2,3,4,5,6]
k=3
n=len(arr)

temp=[0]*n
for i in range(n):
    temp[(i-k%n)]=arr[i]
print(temp)