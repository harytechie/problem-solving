class GrandParent:
    def house(self):
        print("GrandParent owns a house")

class Parent(GrandParent):
    def bike(self):
        print("Parent owns a bike")

class Child(Parent):
    def laptop(self):
        print("Child owns a laptop")



c = Child()

c.house()    
c.bike()     
c.laptop()    