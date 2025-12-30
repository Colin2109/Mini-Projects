import random

while True:
    choice = input("Roll the dice? (y/n): ").strip().lower()
    if choice == "y":
        try:
            roll_amount = int(input("How often?: "))
            if roll_amount <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        for i in range(roll_amount):
            num1 = random.randint(1, 6)
            num2 = random.randint(1, 6)
            print(f'({num1}, {num2})')
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice")
          
