class men:
    def Human(self):
        print("mens are brave")
class boy(men):
    def Human(self):
        print("Boys are brave")
class child(men):
    def Human(self):
        print("child are not brave")


c1=boy()
c2=child()

c1.Human()
c2.Human()