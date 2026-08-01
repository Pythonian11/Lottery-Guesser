import random

print()
print("Generate as many random lottery guesses as you want by running the program multiple times.")

X = int(input("What is the lowest number you can pick in your lottery? "))
Y = int(input("What is the highest number you can pick in your lottery? "))
lottery_number = random.randint(X, Y)
print(f"Lottery number: {lottery_number}")