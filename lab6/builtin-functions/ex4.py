import time
n=int(input("Positive integer to take a square root: "))
m=float(input("Amount of milliseconds to take a root: "))
m/=1000.0
time.sleep(m)
print(f"Square root of {n} after {m} miliseconds is {n**0.5}")