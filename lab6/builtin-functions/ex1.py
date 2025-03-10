import functools
n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)

print(functools.reduce(lambda x,y: x*y, a))
