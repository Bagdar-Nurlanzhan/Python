from itertools import permutations
def print_permutations(user_input):
    perm_list = permutations(user_input)
    for perm in perm_list:
        print(''.join(perm))
user_input = input("enter a str: ")
print_permutations(user_input)