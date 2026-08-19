def num():
    yield 10
    yield 20
    yield 30
    yield 40
n=num()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
