d={
    'name':'python',
    'class': 3,
    'section':'a'
}
n=d.get('name')
print(n)

for k,v in d.items():
     print(k,v)
del d['class']
print(d)
a=d.pop('section')
print(a)

d = {
    'name': 'python',
    'class': 3,
    'section': 'a'
}

d.update({'class':4})
print(d)