'''💡 Project Idea

You will create a program where user can:

Add student
View all students
Search student
Delete student
Exit

'''

l={}
while True:
   print("""
    1.Add student
    2.View all students
    3.Search student
    4.delete student
    5.exit
   """)
   c=int(input("enter choice"))
   if c==1:
       n=input("entername")
       a=int(input("enter age"))
       co=input("entername")
       student={'name':n,'age':a,'course':co}
       l.append(student)
   elif c==2:
       if len(student)==0:
        print("empty")
       else:
        for s in student:
         print(s)
   elif c==3:
      if d.get(name):
       print(student[name])
      else:
       print("notfound")
   elif c==4:
       del d[student]
   elif c==5:
      print("exit")
      break;