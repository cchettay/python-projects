import random  # imprting random numbers
# computer chooses random numbers between 1 and 100
secret_number = random.randint(1, 100)
print("Welcome to the number guessing game")
print("I have chosen a number for you, Can you guess it")
while True:
    guess = int(input("Enter a guess"))  # user enter a number
    if guess < secret_number:
        print("Too low.Enter a different number")
    elif guess > secret_number:
        print("Too high. Enter a different number")
    else:
        print("Congratu;ations you guessed right.")
    break
