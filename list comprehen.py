numbers = [i for i in range(6)]
print(numbers)
doubled = [i*2 for i in range(6)]
print(doubled)
names = ["john", "smith"]
upper_names = [name.upper() for name in names]
print(upper_names)
evens = [i for i in range(10) if i % 2 == 0]
print(evens)
squares = [i*i for i in range(1, 11)]
print(squares)
words = ["hi", "hello", "good morning", "god is love and truth"]
long_words = [word for word in words if len(word) > 3]
print(long_words)
