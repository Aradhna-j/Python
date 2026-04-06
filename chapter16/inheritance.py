# min 2 class ka role  when one want to inherit all properties of othe class
#agr a ko inherit b to b ka object bna k b k obj ko v call ar a k v object ko call krste h

#3 types  single(a to b),(a to b to c)       multilevel,multiple(a and b to c)
# self is object ek arg v h class k kisi v var ko func me use kr skte h
#single inherti..
class A:
    def displayA(self):
        print("hello a")
class B(A):# b inherited a
    def displayB(self):
        print("hello b")
class C(B):# multilevel
    def displayC(self):
        print("heloo c")
obj=C()#obj of b
obj.displayA()
obj.displayB()
obj.displayC()

