# nге дейінгі 3 пен 4 ке бөлінетін сандар функциясы
def meow3_4(n):
    result = []
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            result.append(i)
    return result
n = int(input())
print(meow3_4(n))