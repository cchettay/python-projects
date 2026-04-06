
guests = []  # empty list

while True:
    name = input("Enter the name of guest: ")

    if name.lower() == "exit":
        break

    if name in guests:
        print("Guest alreday existes")
    else:
        guests.append(name)
        print("Guest added")
print("\nGuest List:")
for g in guests:
    print("-", g)
print("Total Guests", len(guests))
