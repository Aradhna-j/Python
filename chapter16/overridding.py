class OverLoadA:
    def display(self):
        print("hello")
class OverLoadB(OverLoadA):
    def display(self):
        super().display()#used to call when same function name same name same parameter
        print("dog")

obj=OverLoadB()
obj.display()