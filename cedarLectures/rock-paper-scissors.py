#Make a 2 player rock paper scissor game that runs for n rounds
#ask user for n values, add winner for each round

from time import sleep
from random import choice

#function to get choice
def get_weapon(name, mode):
    weapons = ["rock", "paper", "scissors"]
    if (mode == 'ai') and (name == 'AI'):
       weapon = choice(weapons)
       print(f"{name}'s choice is {weapon}") 
    else:
        weapon = ''
        while (weapon not in weapons):
            weapon = input(f"{name}, please enter your choice (rock, paper, scissors): ").lower()
            if weapon not in weapons:   
                print("Choice is not valid. Please choose from rock, paper, or scissors.")  
    return weapon

#game introduction
print("Welcome to Rock Paper Scissors!")
sleep(0.5)
print("You can choose to play against another player or against the AI. Winner is declared at the end of each round.")
sleep(1)

# ask user to select game mode
modes = ['two-player', 'two player', 'ai']
mode = ''
while (mode not in modes):
    mode = input("Please enter a game mode ('two-player', 'AI') : ").lower()
    if mode not in modes:
        print("Choice is not valid. Please choose from 'two-player' or 'AI'")   


# get user's name
if (mode == 'ai'):
    player_one = input("Please enter your name: ")
    player_two = 'AI'
else:
    player_one = input("Player 1, please enter your name: ")
    player_two = input("Player 2, please enter your name: ")

#get number of rounds
rounds = 0
while (rounds < 1) or (rounds > 10):
    rounds = int(input("Please enter the number of rounds for the game (1 - 10): "))
    if (rounds < 1) or (rounds > 10):
        print("Invalid input. Please enter a number between 1 and 10.")
        

# initialize scores
player_one_score = 0
player_two_score = 0

# loop for each round
for current_round in range(rounds):
    if (current_round == 0):
        print()
    if current_round == rounds - 1:
        print("Last Round!")
    else:
        print(f"Round {current_round + 1}!")

    # get user's choice
    choice_one = get_weapon(player_one, mode)
    choice_two = get_weapon(player_two, mode)

    # comparing user choices
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

# display the final scores
print(f"Final Scores - {player_one}: {player_one_score}, {player_two}: {player_two_score}, Draws : {rounds - player_one_score - player_two_score}")

# determine the overall winner
if player_one_score > player_two_score:
    print(f"{player_one} is the overall winner!")
elif player_one_score < player_two_score:
    print(f"{player_two} is the overall winner!")
else:
    print("It's a tie! No overall winner.")
