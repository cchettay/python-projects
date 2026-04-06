questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 10 + 5?", "answer": "15"},
    {"question": "What color is the sky?", "answer": "blue"},
    {"question": "What is the capital of Japan?", "answer": "tokyo"},
    {"question": "How many days are in a week?", "answer": "7"}
]
score = 0
for i in range(len(questions)):
    print("\nQuestion", [i+1], ":", questions[i]["question"])
    answer = input("Your answer".lower)
    if answer == questions[i]["answer"]:
        print("Correct")
        score = score+1
    else:
        print("Wrong! The answer is: ", questions[i]["answer"])


print("\n Results")
print("Your score is:", score)
