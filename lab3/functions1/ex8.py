def spy_game(nums):
    code = [0, 0, 7]  
    for num in nums:  
        if num == code[0]:  
            code.pop(0)  
        if not code: 
            return True
    return False  
user_input = input("enter nums: ")  
nums = list(map(int, user_input.split()))  
# Преобразуем строку в список целых чисел
if spy_game(nums):
    print("True")
else:
    print("False")

print(spy_game([1, 2, 4, 0, 0, 7, 5]))    
