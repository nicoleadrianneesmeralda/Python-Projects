import random

print("Welcome to the Number Guessing Game!")

name = input("What's your name? ")
print(f"Hello, {name}! Type in your desired smaller and larger numbers.")

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
print("You can guess a number within the range you've entered. You will only have 5 attempts.")

answer = random.randint(smaller, larger)

for count in range(1, 6):
    guess = int(input("Enter your guess: "))
    if guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")
    else:
        print(f"Congratulations, {name}! You've got it in {count} attempt(s).")
        break
else:
    print(f"Sorry, {name}, you ran out of guesses. The correct number was: {answer}")
