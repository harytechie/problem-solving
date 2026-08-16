arr = [1, 2, 3, 4, 5]
k=2
n=len(arr)
temp=[0]*n
for i in range(n):
    temp[(i+k)%n]=arr[i]
print("Rotate",temp)
