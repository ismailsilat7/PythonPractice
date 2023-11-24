from random import randint
from time import sleep

# to print screen
def printScreen():
    print()
    print('    0   1   2')
    print('  +---+---+---+')
    for row in range(3):
        print(f"{row} | {screen[row][0]} | {screen[row][1]} | {screen[row][2]} |")
        print('  +---+---+---+')
    print()

# to ensure that the character is not the initial variable
def notDefault(char):
    if char != initialVar:
        return True
    else:
        return False

#to find if the game is over, returns true if over
# also returns wether it's a draw, the game should continue or the symbol of the winner 
def isOver():

    # if conditions to check if anyone won
    if (screen[0][0] == screen[1][1] == screen[2][2]) or (screen[0][2] == screen[1][1] == screen[2][0]) or (screen[1][0] == screen[1][1] == screen[1][2]) or (screen[0][1] == screen[1][1] == screen[2][1]):
        if(notDefault(screen[1][1])):    
            return True, screen[1][1]
    
    elif(screen[0][0] == screen[0][1] == screen[0][2]):
        if(notDefault(screen[0][1])):
            return True, screen[0][1]
    
    elif(screen[2][0] == screen [2][1] == screen[2][2]):
        if(notDefault(screen[2][1])):
            return True, screen[2][1]
    
    elif(screen[0][0] == screen[1][0] == screen[2][0]):
        if(notDefault(screen[1][0])):
            return True, screen[1][0]
    
    elif(screen[0][2] == screen[1][2] == screen[2][2]):
        if(notDefault(screen[1][2])):
            return True, screen[1][2]
    else:
        #checks for empty spaces
        emptySpace = 0
        for row in range(3):
            for col in range(3):
                if screen[row][col] == initialVar:
                    emptySpace += 1
        # checks if space is filled
        if (emptySpace < 1):
            return True, 'draw'
    return False, 'continue'

# get input of symbol from user
def getSymbol(name):
    correctSymbols = ['X', 'O']
    symbol = input(f"{name}, please enter your symbol ('{correctSymbols[0]}' or '{correctSymbols[1]}'): ")
    while symbol not in correctSymbols:
        print("Invalid Symbol Entered")
        symbol = input(f"{name}, please enter your symbol ('{correctSymbols[0]}' or '{correctSymbols[1]}'): ")
    return symbol

# ensures if the position chosen is correct
def correctPosition(position):
    if position >= 0 and position <= 2:
        return True
    else:
        return False

# get user's legal choice of position to enter symbol on the board
def getChoice(name, mode):
    row = -1
    col = -1
    correct = False
    # checks if it is AI's turn
    if (mode == 'ai') and (name == 'AI'):
        # repeats until the position chosen is not legal
        while (correct != True):
            row = randint(0,2)
            col = randint(0,2)
            if (screen[row][col] == initialVar):
                correct = True
    else:
        # repeats until the position chosen is not legal
        while(correct != True):
            row = int(input(f"{name}, please enter your desired position's row (0, 1 or 2) : "))
            while(correctPosition(row) == False):
                print("Invalid position entered")
                row = int(input(f"{name}, please enter your desired position's row (0, 1 or 2) : "))
            col = int(input(f"{name}, please enter your desired position's colunn (0, 1 or 2) : "))
            while(correctPosition(col) == False):
                print("Invalid position entered")
                col = int(input(f"{name}, please enter your desired position's column (0, 1 or 2) : "))
            if (screen[row][col] != initialVar):
                print(f"The position {row},{col} is already occupied, please enter a different position")
            else:
                correct = True
    return row, col

initialVar = '#'
screen = [[initialVar for i in range(3)] for i in range(3)]
print()
print("Tic Tac Toe Game")

# ask user to select game mode
modes = ['two-player', 'two player', 'ai']
mode = ''
while (mode not in modes):
    mode = input("Please enter a game mode ('two-player', 'AI') : ").lower()
    if mode not in modes:
        print("Choice is not valid. Please choose from 'two-player' or 'AI'")   

player_one = input("Player 1, please enter your name: ").lower()

# if mode is AI, the second user will be AI
if mode == 'ai':
    player_two = 'AI'
else:
    player_two = input("Player 2, please enter your name: ")

print()

# get symbol from each user
symbol_one = getSymbol(player_one)
if (symbol_one == 'X'):
    symbol_two = 'O'
else:
    symbol_two = 'X'
print(f"{player_two}'s symbol is '{symbol_two}'")

print()

print("Let's get started")

printScreen()

over = False
result = ''
current_player = player_one
current_symbol = symbol_one
# until the game is not over, continue with the game
while(over != True):
    print(f"{current_player}'s turn")
    sleep(0.5)
    row, col = getChoice(current_player, mode)
    screen[row][col] = current_symbol
    printScreen()
    sleep(1)
    if current_player == player_one:
        current_player = player_two
        current_symbol = symbol_two
    else:
        current_player = player_one
        current_symbol = symbol_one

    over, result = isOver()
    

winner = ''  

if result == 'draw':
    print('This game is a draw')
elif result == symbol_one:
    winner = player_one
elif result == symbol_two:
    winner = player_two

if winner != '':
    for line in range(3):
        if (line % 2 != 0):
            print(f"* {winner.upper()} WINS! *")
        else:
            for stars in range(len(f"{winner} WINS!") + 4):
                print("*", end='')
            print()
