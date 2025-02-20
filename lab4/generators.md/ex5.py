# nнен 0ге дейінгі сандарды шығару
def countdown(n):
    numbers = []
    for i in range(n, -1, -1):
        numbers.append(i)
    return numbers
n = int(input())
print(countdown(n))