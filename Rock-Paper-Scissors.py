import random
times_won = 0
options = ["r", "p", "s"]
emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
while True:
    choice = input("rock, paper or scissors? (r/p/s): ").strip().lower()
    if choice not in options:
        print("Invalid choice")
        continue
    computer_choice = random.choice(options)
    print(f'You chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')
    if choice == computer_choice:
        print("Tie!")
    elif (
        (choice == "r" and computer_choice == "s") or
        (choice == "p" and computer_choice == "r") or
        (choice == "s" and computer_choice == "p")):
        print("You win!!")
        times_won += 1
        print(f'You have won {times_won} times!!')
    else:
        print("You lose!")
    should_continue = input("Press any key to continue or n to end: ").strip().lower()
    if should_continue == "n":
        break