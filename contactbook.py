contacts = {}

while True:
    print("\n  CONTACT BOOK")
    print("1. View all contacts")
    print("2. Add contacts")
    print("3. Search contacts")
    print("4. Delete contacts")
    print("5. Quit")
    choice = input("choose an option")
    if choice == "1":
        if contacts == {}:
            print("No contacts Yet")
        else:
            for name in contacts:
                print(name, ".", contacts[name])

    elif choice == "2":
        name = input("Enter name:",)
        number = input("Enter contact number:")
        contacts[name] = number
        print("Contact added successfully")

    elif choice == "3":
        name = input("Enter name of contact to search: ")
        if name in contacts:
            print(name, ".", contacts[name])
        else:
            print(name, "name not found",)
    elif choice == "4":
        name = input("Enter name to be deleted: ")  # asking for input!
        if name == "":
            print("Please enter a name!")
        elif name in contacts:
            contacts.pop(name)
            print(name, "deleted successfully!")
        else:
            print(name, "not found!")

    elif choice == "5":
        print("Good bye")
        break
