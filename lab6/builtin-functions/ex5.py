def check(x):
    return bool(x)
n=int(input())
a=[]
for i in range(n):
    k=input()
    a.append(k)
a=tuple(a)
b=list(map(check, a))
print("No") if b.count(False) else print("Yes")