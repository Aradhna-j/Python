l=[]
while True:
    c=int(input(''' 
     1. Push
    2. Pop
    3. Display
    4. Peek
    5. Exit
                   
    '''))
    if c==1:
      n=int(input("Enter a number: "))
      l.append(n)   
    elif c==2:
     if len(l)==0:
        print("Stack is empty")
     else:
       print("pop item",l.pop())
    elif c==3:
     if len(l)==0:
        print("empty list")
     else:
        print(l)
    elif c==4:
     if len(l)==0:
        print("empty list")
     else:
        print("last element is :",l[-1])
    elif c==5:
      print("exit")
      break;