# санның нге дейінгі квадраттарын шығару
N = int(input())
def square_generator(N):
    squares = []
    for i in range(N + 1):
        squares.append(i ** 2)
    return squares
print(square_generator(N))