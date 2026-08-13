#inheritence
class Parent:
    def d(self):
        print("hello")
    def s(self):
        print("hi")
class Child(Parent):
    def res(self):
        print("hi hello")

c1=Child()

c1.d()
c1.s()
c1.res()