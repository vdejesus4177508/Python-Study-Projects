#guess game
import random

# This is a simple number guessing game where the player has to guess a number between 1 and 20.


guessestaken = 0

print("Hello! What is your name?")
myName = input()

number = random.randint(1,20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

while guessestaken < 6:
    print("Take a guess.")
    guess = input()

    ## Try to convert the input to an integer
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    ## Check if the guess is within the valid range
    if guess < 1 or guess > 20:
        print("Your guess is out of range! Please pick a number between 1 and 20.")
        continue

    guess = int(guess)

    guessestaken += 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess

if guess == number:
    guessestaken = (str(guessestaken))
    print("Good job, " + myName + "! You guessed my number in " + str(guessestaken) + " guesses!")
if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")