tasks = []

while True:
    print("\n To do list ")
    print("1. view tasks")
    print("2. Add tasks")
    print("3. Remove tasks")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        if tasks == []:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "3":
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])
        num = int(input("Enter the task to remove: "))
        tasks.pop(num - 1)
        print("Task deleted")

    elif choice == "4":
        print("See you later!")
        break
