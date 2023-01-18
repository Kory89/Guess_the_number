import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        guess = int(input("Guess the number:"))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
    print("Correct! The number is", number)

guess_the_number()
