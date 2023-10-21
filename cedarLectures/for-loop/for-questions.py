#Q1. ask a user for a number & print it's multiplication table (1-10)

number = int(input("Please enter a number : "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
print()

#Q2. use for loop to output all odd numbers between 1000 and 10000

for i in range(1001, 10000):
    if (i % 2 == 1):
        print(i)
print()

#Q3. ask user for size of the triangle and print a right angle triangle

triangle_height = int(input("Enter height of the triangle : "))
for i in range(triangle_height):
    for j in range(i + 1):
        print("#", end = "")
    print()
print()

#Q4. ask user for the size of the pyramid and output a pyramid of that height

pyramid_height = int(input("Enter pyramid height : "))
for i in range(pyramid_height):
    for space in range(pyramid_height - (i + 1)):
        print(" ", end = "")
    for hashes in range (i + 1):
        print ("#", end = "")
    for hashes in range(i):
        print("#", end = "")
    print()
print()

#Q5. ask user for the number of fishes and size of the fish & then print that many fishes

num_of_fishes = int(input("Enter the number of fishes : "))
fish_size = int(input("Enter the size of fish : "))
for fishes in range(num_of_fishes):
    for i in range(fish_size):
        for space in range(fish_size - (i + 1)):
            print(" ", end = "")
        for hashes in range (i + 1):
            print ("#", end = "")
        for hashes in range(i):
            print("#", end = "")
        print()
    for i in range(fish_size - 2, -1, -1):
        for space in range(fish_size - (i + 1)):
            print(" ", end = "")
        for hashes in range (i + 1):
            print ("#", end = "")
        for hashes in range(i):
            print("#", end = "")
        print()
    for i in range(1, fish_size):
        for space in range(fish_size - (i + 1)):
            print(" ", end = "")
        for hashes in range (i + 1):
            print ("#", end = "")
        for hashes in range(i):
            print("#", end = "")
        print()
    print()


#Make a 2 player rock paper scissor game that runs for n rounds
#ask user for n values, add winner for each round
from time import sleep

print("Rock Paper Scissors Game!")
sleep(0.5)
print("This is a 2-player game. Each player enters their choice, and the winner is declared at the end of each round.")
sleep(1)
player_one = input("Player 1, please enter your name: ")
player_two = input("Player 2, please enter your name: ")
rounds = int(input("Please enter the number of rounds for the game: "))

# Initialize scores
player_one_score = 0
player_two_score = 0

for current_round in range(rounds):
    if (current_round == 0):
        print()
    if current_round == rounds - 1:
        print("Last Round!")
    else:
        print(f"Round {current_round + 1}!")

    while True:
        choice_one = input(f"{player_one}, please enter your choice (rock, paper, scissors): ").lower()
        if choice_one in ["rock", "paper", "scissors"]:
            break
        print("Choice is not valid. Please choose from rock, paper, or scissors.")

    while True:
        choice_two = input(f"{player_two}, please enter your choice (rock, paper, scissors): ").lower()
        if choice_two in ["rock", "paper", "scissors"]:
            break
        print("Choice is not valid. Please choose from rock, paper, or scissors.")

    if choice_one == choice_two:
        print("It's a draw!")
    elif (
        (choice_one == 'rock' and choice_two == 'scissors') or
        (choice_one == 'paper' and choice_two == 'rock') or
        (choice_one == 'scissors' and choice_two == 'paper')
    ):
        print(f"{player_one} Wins! {choice_one} beats {choice_two}")
        player_one_score += 1
    else:
        print(f"{player_two} Wins! {choice_two} beats {choice_one}")
        player_two_score += 1
    print()
    sleep(1)

# Display the final scores
print(f"Final Scores - {player_one}: {player_one_score}, {player_two}: {player_two_score}")

# Determine the overall winner
if player_one_score > player_two_score:
    print(f"{player_one} is the overall winner!")
elif player_one_score < player_two_score:
    print(f"{player_two} is the overall winner!")
else:
    print("It's a tie! No overall winner.")
