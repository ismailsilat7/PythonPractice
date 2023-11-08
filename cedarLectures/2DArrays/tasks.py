from random import randint
#TASK1: make a 2d array to store sales of 5 salespersons' sales for 12 months
sales = [[0 for col in range(12)] for row in range(5)]


#TASK2: ask user to enter sales for each sales person for each month

for row in range(5):
    for col in range(12):
        #sales[row][col] = input(f"Enter sales for salesperson {row + 1} for month number {col + 1} : ")
        sales[row][col] = randint(15,90)
    print(end="")

#TASK3: calculate the average sales for each salesperson and average sales of all salesperson
for row in range(5):
    sum = 0
    for col in range(12):
        sum += sales[row][col]
    avg = int(sum/12)
    print(f"For salesperson {row}, the average sales is {avg}")

#TASK4: find the highest and lowest sales month for each salesperson
for row in range(5):
    highest = sales[row][0]
    lowest = sales [row][0]
    for col in range(1,12):
        if sales[row][col] > highest:
            highest = sales[row][col]
        elif(sales[row][col] < lowest):
            lowest = sales[row][col]
    print(f"For salesperson {row}, the highest sales for the year is {highest} and the lowest sales for the year is {lowest}")

#TASK5 : make a 1d array bonus, that calculates bonus for each sales person based on the formula
# total of 10% of (sales for the month * month number)
bonus = [0 for i in range(5)]
for row in range(5):
    totalAdjustment = 0
    for col in range(12):
        bonusAdjustment = sales[row][col]*(col + 1)
        totalAdjustment += bonusAdjustment
    bonus[row] = int(0.1 * totalAdjustment)
print(bonus)

#TASK6 : make a 2 player tic tac toe

def printScreen():
    print()
    print('    0   1   2')
    print('  +---+---+---+')
    for row in range(3):
        print(f"{row} | {screen[row][0]} | {screen[row][1]} | {screen[row][2]} |")
        print('  +---+---+---+')
    print()


def notDefault(char):
    if char != initialVar:
        return True
    else:
        return False


def isOver():

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
        emptySpace = 0
        for row in range(3):
            for col in range(3):
                if screen[row][col] == initialVar:
                    emptySpace += 1
        if (emptySpace < 1):
            return True, 'draw'
    return False, 'continue'

def getSymbol(name):
    correctSymbols = ['X', 'O']
    symbol = input(f"{name}, please enter your symbol ('{correctSymbols[0]}' or '{correctSymbols[1]}'): ")
    while symbol not in correctSymbols:
        print("Invalid Symbol Entered")
        symbol = input(f"{name}, please enter your symbol ('{correctSymbols[0]}' or '{correctSymbols[1]}'): ")
    return symbol

def correctPosition(position):
    if position >= 0 and position <= 2:
        return True
    else:
        return False

def getChoice(name):
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
        row, col = getChoice(name)
    return row, col

initialVar = '#'
screen = [[initialVar for i in range(3)] for i in range(3)]
print()
print("A 2 Player Tic Tac Toe Game")

player_one = input("Player 1, please enter your name: ")
player_two = input("Player 2, please enter your name: ")

print()

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
while(over != True):
    row, col = getChoice(current_player)
    screen[row][col] = current_symbol
    printScreen()

    if current_player == player_one:
        current_player = player_two
        current_symbol = symbol_two
    else:
        current_player = player_one
        current_symbol = symbol_one

    over, result = isOver()
    
    

if result == 'draw':
    print('This game is a draw')
elif result == symbol_one:
    print(f'{player_one.upper()} WINS!')
elif result == symbol_two:
    print(f'{player_two.upper()} WINS!')


