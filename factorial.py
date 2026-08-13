#5!=1*2*3*4*5
a=int(input("Enter a number :"))
sum=1

def rev(n):
    global sum
    if n>a:
        return
    sum=sum*n
    rev(n+1)

rev(1)
print(sum)