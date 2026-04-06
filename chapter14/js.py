import json
d='{"cname":"Python","fees":2000}'
x=json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a)