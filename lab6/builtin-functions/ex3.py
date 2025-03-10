def check(x):
    global a
    global i
    i-=1
    return x==a[i]

a = str(input())
i=len(a)

c=list(filter(check, a))
print("Palindrome") if len(c)==len(a) else print("No")