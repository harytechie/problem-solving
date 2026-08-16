num=[2,7,4,3,5,3]
target=int(input())
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if(num[i]+num[j]==target):
            print(i,j)