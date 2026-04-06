count = int(input("How many numbers do you want to enter"))
numbers = []
for i in range(count):
    num = int(input(f"enter a numer , {i+1}:"))
    numbers.append(num)
    largest = max(numbers)
    print("the largest number is", largest)
