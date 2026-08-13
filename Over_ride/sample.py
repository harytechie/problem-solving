class Parent:
    def display(self):
        print("hi")

class Child1(Parent):
    def display(self):
        print("hello")

class Child2(Parent):
    def display(self):
        print("hey")

c1 = Child1()
c2 = Child2()

c1.display()
c2.display()
c1.display()
c2.display()