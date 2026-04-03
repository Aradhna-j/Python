import random
choice=int(input("enter a num between 1 and 100:"))
n=random.randint(1,100)
print("computer guessed no is:",n)
if choice==n:
     print("Bang on!")
elif choice>50 and choice<75:
    print("Your choice is high")
elif choice>75 and choice <=100:
    print("too far")
elif choice>25 and choice<50:
    print("low")
elif choice>1 and choice<25:
    print("you are far")
else:
    print("out of range")
