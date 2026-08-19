def num():
    num=1
    while num<=3:
        yield num   
        num+=1
n=num()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
