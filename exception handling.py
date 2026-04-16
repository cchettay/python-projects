# try:
#   num = int(input("Enter a number"))
#    print("you entered a number", num)
# except ValueError:
#   print("That's not a number")
# try:
#   result = 10/0
# except ZeroDivisionError:
#   print("cannot divide by zero")
# try:
#   with open("missing.txt", "r")as f:
#      print(f.read())
# except FileNotFoundError:
#   print("file not found")
# try:
#   num = int(input("Enter a number"))
# result = 10/num
#   print("Result:", result)
# except ValueError:
#   print("that's not a number")
# except ZeroDivisionError:
#   print("cannot divide by zero")
# try:
#   num = int(input("Enter a number: "))
# except ValueError:
#   print("That's not a number!")
# else:
#   print("Success! You entered:", num)  # runs if NO error
# finally:
#   print("This always runs!")  # runs no matter what
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print("Result:", result)
        break
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
