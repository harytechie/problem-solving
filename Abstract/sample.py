from abc import ABC,abstractmethod

class Parent(ABC):
    def show(c):
        pass
class Child(Parent):
    def show(c):
        print()
        print("Abstract class run succeccfully")
        print()
c=Child("hello")
c.show()