import random

# Generate a Random Number
number_to_guess = random.randint(1, 100)

# Prompt the User for Guesses
guess = int(input("Guess the number (between 1 and 100): "))

# Count the Attempts
attempts = 1

while guess != number_to_guess and attempts < 10:
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    attempts += 1
    guess = int(input("Guess the number (between 1 and 100): "))

if attempts == 10:
    print("Game over! Better luck next time.")
else:
    print("Congratulations! You've guessed it in", attempts, "attempts!")