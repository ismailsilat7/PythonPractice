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
screen = [[0 for i in range(3)] for i in range(3)]
print("A 2 Player Tic Tac Toe Game")