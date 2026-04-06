class DemoClass:
    a=10

    def  sumvalue(self):#self act as object in itself ,its a argument,mandatory when making function inside class
        print(20+30)

demoobject=DemoClass()
demoobject1=DemoClass()
print(demoobject.a)
print(demoobject1.a)
demoobject.sumvalue();