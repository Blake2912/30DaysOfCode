# Today is day two, today I will be revising the control flow statements in python3 Today I am developing a guessing
# game where we will have a random number be generated from 1-100 and we need to guess that
import random

print("Day2")
print("Hi-Lo Game")
RandomNumber = random.randint(1, 100)
numberOfGuesses = 5
while True:
    if numberOfGuesses == 0:
        print("Game Over")
        break
    else:
        number = int(input("Enter your guess, hint the number is in-between 1 and 100: "))
        if number == RandomNumber:
            print("Excellent you guessed it correctly")
            print("You guessed the correct number is {} guesses".format(numberOfGuesses))
            break
        elif number > RandomNumber:
            numberOfGuesses = numberOfGuesses - 1
            print("Guess Lower!, lives left - {}".format(numberOfGuesses))
        elif number < RandomNumber:
            numberOfGuesses = numberOfGuesses - 1
            print("Guess Higher!, lives left - {}".format(numberOfGuesses))
