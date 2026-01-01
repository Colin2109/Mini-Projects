import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1-100: "))
        if guess == number:
            number_notguessed = False
            print("Correct!! The number is:", number)
            break
        elif guess <= 0:
            print("Enter a positive number between 1-100")
        elif guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
    except ValueError:
        print("Enter a positive number between 1-100")
        continue