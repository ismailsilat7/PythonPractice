#TASK1 : make a function that takes 2 parameters and returns their sum
def sum(num1,num2):
    return num1 + num2
number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter another number : "))
numSum = sum(number1, number2)
print(numSum)

#TASK2 : make a function that calls another function that takes input of a number and validates if it is positive 
# output multiplication table of the number in the first function
def isPositive(number):
    if (number > 0):
        return number
    else:
        while (number < 1):
            number = int(input("Please enter a poistive number : "))
    return number

def multiplicationTable(number):
    number = isPositive(number)
    for times in range(1,13):
        print(f"{number} x {times} = {number * times}")

num = int(input("Please enter a number for it's multiplication table : "))
multiplicationTable(num)

#TASK3 : make a function pyramid, that calls outputspaces(), updatevalues(), outputsymbols() as required
def outputspaces(pyramidHeight, rowNum):
    print(" " * (pyramidHeight - (rowNum + 1)) , end = "")
    
def outputsymbols(rowNum):
    print("#" *(2 * rowNum + 1), end="")

def updatevalues(rowNum):
    return rowNum + 1

def pyramid(pyramidHeight):
    rowNum = 0
    while (rowNum < pyramidHeight):
        outputspaces(pyramidHeight, rowNum)
        outputsymbols(rowNum)
        rowNum = updatevalues(rowNum)
        print()

pyramid(int(input("Enter pyramid height : ")))
