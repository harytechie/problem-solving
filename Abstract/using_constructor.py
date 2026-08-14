from abc import ABC,abstractmethod

class Parent(ABC):
    
    def __init__(self,name):
        self.name=name
    def show(self):
        pass

class Child(Parent):
    def show(self):
        print()
        print(self.name,"bro")
        print()
c=Child("Hi")
c.show()