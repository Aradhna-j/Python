# method is called with object
#constructor automatically created at  tym of objext creation # defined by__init__
#**self ki jagah kuch v but python me generally self hi use krte h
 

class MethodClass:
    a=10
    def __init__(self):#constructor
        
        print("hello")
    def showvalue(self):
        #self.c=self.a*self.a#output 100
        print(self.a)#will give error if print(a)
    def sumvalue(self,a,b):
        print(a+b)
    
obj=MethodClass()
obj.showvalue()#method called
obj.sumvalue(20,20)