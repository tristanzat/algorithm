# 1. Name: 
#    Tristan Zatylny
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program lets the user play a guessing game where they try to guess a random number between 1 and a user-defined limit.
#    The game give hints based on whether the user's guess was too high or too low. When the user wins, the program returns the amount of
#    guesses that were required to win and what the guesses were.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of the assignment was remembering how a try-catch (or rather, try-except) works in python. Once I looked it up,
#    I was able to implement the error handling and write the whole program very easily.
# 5. How long did it take for you to complete the assignment?
#    1 hour

'''
Test cases:
1. At the first prompt, select the value 1. Guess 1 on your first attempt.
2. At the first prompt, select the value 1. Guess 0, then 2, then 1.
3. At the first prompt, select the value 10 and play the game the best you can.
4. At the first prompt, select the value 50 and play the game the best you can.
'''

import random

# Game introduction.
print("This is the \"guess a number\" game.\nYou try to guess a random number in the smallest number of attempts.\n")

# Prompt the user for how difficult the game will be. Ask for an integer.
while True:
    # Error handling
    try:
        value_max = int(input("Pick a positive integer: "))
        if value_max > 0:
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}.")

# Initialize the sentinal and the array of guesses.
guesses = []
guess = 0

# Play the guessing game.
while True:
    # Prompt the user for a number.
    while True:
        # Error handling
        try:
            guess = int(input("> "))
            if guess > 0 and guess <= value_max:
                break
            else:
                print("Invalid guess. Please try again.")
        except ValueError:
            print("Invalid guess. Please try again.")

    # Store the number in an array so it can be displayed later.
    guesses.append(guess)

    # Make a decision: was the guess too high, too low, or just right.
    if guess == value_random:
        # If the user is correct, show how many guesses it took and print the array of guessed numbers.
        print(f"You were able to find the number in {len(guesses)} guesses.\nThe numbers you guessed were: {guesses}")
        break
    
    elif guess >= value_random:
        print("\tToo high!")
    
    else:
        print("\tToo low!")