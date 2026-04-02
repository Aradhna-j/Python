w="hello world"
#w=w[-1::-1] reverse the string
t=len(w)
print(t)
for a in range(t-1,-1,-1):
    print(w[a],end=" ")
