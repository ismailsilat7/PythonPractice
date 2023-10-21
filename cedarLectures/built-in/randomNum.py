# TASK 3: Create a reverse number guessing game, ask the user to enter a secret number
# use random to guess the number, output how many tries it takes
from random import randint

secret_number = int(input("Please enter a number between 1 & 10 (computer will try to guess it) : "))
num = randint(1,10)
guess_count = 1
while (num != secret_number):
    num = randint(1,10)
    guess_count += 1
print(f"Computer took {guess_count} guesses.")
