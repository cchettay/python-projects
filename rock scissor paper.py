import random

emojis = {'r': '🪨', 'p': '📄',  's': '✂️'}

choices = ('r', 'p', 's')

while True:
    user_choice = input("rock, paper, or scissors? r/p/s: ").lower()
    if user_choice not in choices:
        print("invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print("\n----------------------")
    print(f'you chose: {emojis[user_choice]}')
    print(f'computer chose: {emojis[computer_choice]}')
    print("----------------------")

    if user_choice == computer_choice:
        print("Tie")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        print("You win")
    else:
        print("you lose")

    should_continue = input("Do you want to continue (y/n): ").lower()
    if should_continue == "n":
        break
