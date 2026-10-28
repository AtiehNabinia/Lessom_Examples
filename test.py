a=[15,52,6]
print(list(map(lambda x: x>10,a)))
print(list(map(lambda x:x if x>10 else 0,a)))
print(list(filter(lambda x: x>10,a)))

a=[5,2]
b=[6,9]
print(list(map(lambda x,y:x+y,a,b)))

def f(x):
    return x-1
def g(y):
    return y*2
func=[f,g]
l=[3,4,5]
for i in l:
    print(list(map(lambda a:a(i),func)))

lis=[6,8,[],'',{}]
print(list(filter(None,lis)))

from functools import reduce
k=[5,2,7,6]
def sum(x,y):
    return x+y
print(reduce(sum,k))

student=[
    {id:1,'name':'atieh','score':20},
    {id:5,'name':'elmira','score':17.5},
    {id:9,'name':'maryam','score':14},
    {id:3,'name':'hanieh','score':16}
]
print(sorted(student,key=lambda x:x['name']),end=' ')
student=[
    (1,'atieh',20),
    (5,'elmira',17.5),
    (9,'maryam',14),
    (3,'hanieh',16)
]
from operator import itemgetter
print(sorted(student,key=itemgetter(2)))