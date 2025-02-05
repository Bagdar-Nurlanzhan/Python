import random
def guess_number():
    print("Hello! What is your name?")
    name = input()
    secret_number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses_taken = 0
    # счетчик
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
