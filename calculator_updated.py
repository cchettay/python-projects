def addition(a, b):
    print(f'result:{a+b}')


def substraction(a, b):
    print(f'result:{a-b}')


def multiplication(a, b):
    print(f'result:{a*b}')


def division(a, b):
    if (b == 0):
        print("we cannot divide by zero")
    else:
        print(f'result:{a/b}')


while True:
    print("choose an operation:")
    print("1. \n Addition")
    print("2. \n Substraction")
    print("3. \n multiplication")
    print("4. \n division")
    print("5. \n exit")

    choice = input("enter your choice: ")

    if choice == "5":
        print("\n Thank You")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first  number: "))
        num2 = float(input("enter the second number: "))
        if choice == "1":
            addition(num1, num2)
        elif choice == "2":
            substraction(num1, num2)
        elif choice == "3":
            multiplication(num1, num2)
        elif choice == "4":
            division(num1, num2)
    else:
        print("Invalid choice!")
