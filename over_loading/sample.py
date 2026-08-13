class A:
    def add(self,*num):
        return sum(num)

c=A()
print(c.add(1,2))
print(c.add(1,2,3))
print(c.add(1,2,3,4))