# TASK 2: Create a number guessing game, use random to create secret number
# output how many tries user takes to guess a number
from random import randint

secret_number = randint(1,20)
print("The number is between 1 & 20 inclusive, try to guess the number in as few tries as possible.")
print("Following are two hints;")

if (secret_number % 2 == 0):
    print("1. The number is Even")
else:
    print("1. The number is Odd")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(secret_number):
    print("2. The number is a Prime number")
else:
    print("2. The number is not a Prime number")


guess_count = 1
user_num = int(input("Please Enter your Guess : "))
while (user_num != secret_number):
    print("Invalid Guess.")
    user_num = int(input("Please enter another Guess : "))
    guess_count += 1

print("Correct!")
print(f"You took {guess_count} guesses.")
