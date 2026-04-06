
guests = []  # empty list

while True:
    name = input("Enter the name of guest: ")

if name in guests:
    print("Guest alreday existes")
else:
    guests.append(name)
    print("Guest added")

print("Total Guests", len(guests))
