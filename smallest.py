count = int(input("EHow many numbers do you want to enter"))
numbers = []
for i in range(count):
    num = int(input(f"enter a number,{i+1}:"))
    numbers.append(num)
    smallest = min(numbers)
    print("\nthe smallest number is \n ", smallest)
