class A:
    def display(self):
        print("hi")

class B:
    def display(self):
        print("hello")

class C:
    def display(self):
        print("hey")

D = [A(), B(), C()]
for i in D:
    i.display()  # duck typing
