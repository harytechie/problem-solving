class Parent:
    def display(self):
        print("hi")

class Child1(Parent):
    def display(self):
        print("hello")

class Child2(Parent):
    def display(self):
        print("hey")

Parent = [Child1(), Child2()]

for i in Parent:
    i.display()