n=int(input("enter n"))
for i in range(1,n+1):
    for j in range(2*i-1):
        print("*",end=" ")
    print()



n=int(input("enter n"))
i=1
for i in range(n,0,-1):
 print(i)
i=i*n
n = int(input("Enter n: "))

for i in range(10, 0, -1):
    print(n, "x", i, "=", n*i)