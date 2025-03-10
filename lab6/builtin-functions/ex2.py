a = str(input())
b = sum(map(str.isupper, a))
c = sum(map(str.islower, a))
print(f"Number of upper case: {b}",f"\nNumber of lower case: {c}")