def unique_elements(listt):
    unique_list = []
    for element in listt:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

inputt = input()
my_list = list(map(int, inputt.split()))
print("исходный список", my_list)
print("список c уникальными элементами", unique_elements(my_list))
