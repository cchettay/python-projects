user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number:"))


def addition(user_input1, user_input2):
    sum_num = user_input1+user_input2
    print(f"The sum is : {sum_num}")


def substraction(user_input1, user_input2):
    sub_num = user_input1-user_input2
    print(f"The substraction is:{sub_num}")


def multiplication(user_input1, user_input2):
    multi_num = user_input1*user_input2
    print(f"The multiplication is :{multi_num}")


addition(user_input1, user_input2)
substraction(user_input1, user_input2)
multiplication(user_input1, user_input2)
