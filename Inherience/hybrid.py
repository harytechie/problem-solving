
class GrandParent:
    def house(self):
        print("GrandParent owns a house")

class Father(GrandParent):
    def bike(self):
        print("Father owns a bike")

class Mother:
    def car(self):
        print("Mother owns a car")

class Child(Father, Mother):
    def laptop(self):
        print("Child owns a laptop")


c = Child()

c.house()     
c.bike()      
c.car()       
c.laptop()    