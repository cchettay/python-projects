import random
number_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("guess a number between 1 and 100: "))
        if guess < number_guess:
            print("too low")
        elif guess > number_guess:
            print("too high")
        else:
            print("congratulations")
            break
    except ValueError:
        print("enter a valid number")
