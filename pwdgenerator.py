import random
import string

print("PASSWORD GENERATOR")

length = 10

print("What the password must include")

use_letters = input("Inlude letters? (Yes/No)").lower()
use_numbers = input("Inlude numbers? (Yes/No)").lower()
use_symbols = input("Inlude symbols? (Yes/No)").lower()

characters = ""

if use_letters == "Yes":
    characters = characters+string.ascii_letters
if use_numbers == "yes":
    characters = characters+string.digits
if use_symbols == "yes":
    characters = characters+string.punctuation

if characters == "":
    print("you must choose atleast one option")
else:
    password = ""
for i in range(length):
    password = password+random.choice(characters)
print("Your password is :", password)
