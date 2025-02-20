# а дан бға дейінгі сандардыңі квадратын шығару
def squares(a, b):
    square_value = []
    for i in range(a, b+1):
        square_value.append(i ** 2)
    return square_value
a = int(input())
b = int(input())
print(squares(a, b))