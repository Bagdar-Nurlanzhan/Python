# а дан бға дейінгі сандардыңі квадратын шығару
def squares(a, b):
    for i in range(a, b+1):
        yield i
a = int(input())
b = int(input())

for i in squares(a, b):
    print(i)
print(squares(a, b))