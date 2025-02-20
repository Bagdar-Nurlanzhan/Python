# nге дейінгі жұп сандарды алу
def even_numbers(n):
    evens = []
    for i in range(0, n + 1, 2):
        evens.append(i)
    return evens
n = int(input())
for number in even_numbers(n):
    print(number)
