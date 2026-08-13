class parent1:
    def display(self):
        print("hello grand")
class parent2(parent1):
    def show(self):
        print("hello parent")
class child(parent2):
    def res(self):
        print("hello child")

c1=child()

c1.display()
c1.show()
c1.res()