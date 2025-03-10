# nге дейінгі 3 пен 4 ке бөлінетін сандар функциясы
def meow3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i  
n = int(input())
print(list(meow3_4(n)))  