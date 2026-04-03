import random
n=random.randint(3,20)#it will start from 3 qnd give between 20 inc both
print(n)

n=random.randrange(3,20)#it will start from 3 qnd give between 20 excluding 20
n1=random.randrange(3,20)
print(n1)

n3=[1,2,3,4]
#n4=random.choice(n3)#list pass krna hota h
random.shuffle(n3)#random seq return alg se var bnhi lena hota h
print(n3)

n4=random.random()#0 se 1 k bech ak akoi bhi value
print(n4)

n5=random.uniform(3,8)
print(n5)#float dega