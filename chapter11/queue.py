l=[]
while True:
 c=int(input('''
   1.enqueue
   2.dequeue
   3.rear
   4.front
   5.exit
     '''))
 
 if c==1:
    n=int(input("enter digit:"))
    print(l.append(n))
 elif c==2:
   if len(l)==0:
     print("empty")
   else:
     m=int(input("index to be deleted"))
     del l[m]
     print(l)
 elif c==3:
   if len(l)==0:
     print("empty ")
   else:
    print("element is :",l[-1]) 
 elif c==4:
   print(l[0])
 elif c==5:
   print("exit")
   break;