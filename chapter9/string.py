w="hello"
print(w[0:4])
w="hello world"
print(w[-1::-1])

w="hello world"
#w=w[-1::-1] reverse the string
t=len(w)
print(t)
for a in range(t-1,-1,-1):
    print(w[a],end=" ")

