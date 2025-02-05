def histogram(numbers):
    for num in numbers:
    # Перебираем числа из списка
        print('*' * num)
input_numbers = input()
my_list = list(map(int, input_numbers.split()))
print(my_list)
histogram(my_list)