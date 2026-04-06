class A:
    def displayA(self):
        print("hello a")
class B:
    def displayB(self):
        print("hello b")
class C(A,B):
    def displayC(self):
        print("hello c")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
