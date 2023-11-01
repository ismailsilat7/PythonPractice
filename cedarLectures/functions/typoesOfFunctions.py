"""
Procedure = VOID FUNCTIONS
Functions = FRUITFUL FUNCTIONS
"""

# void functions
def inputOddNumber():
    number = 0
    while number % 2 == 0:
        number = int(input("Enter an Odd Number : "))
    print("Valid Number entered")
# main program starts here
inputOddNumber()

# void functions with parameters
def outputSymbols(numberOfSymbols,symbol):
    for count in range(numberOfSymbols):
        print(symbol, end="")
    print()
#main program starts here
outputSymbols(10, "$")

# fruitful functions
def inputOddNumber():
    number = 0
    while number % 2 == 0:
        number = int(input("Enter an Odd Number : "))
    return number
# main program starts here
newNumber = inputOddNumber()
print(f"{newNumber} is the returned value :)")

#fruitful functions with parameters
def sumRange(firstValue, lastValue):
    sum = 0
    for thisValue in range(firstValue,lastValue + 1):
        sum = sum + thisValue
    return sum
# main program starts here
newNumber = sumRange(1,10)
print(newNumber)

#byref functions (python do not have byref functions, thus we would try to implement a function that works just like a by reference function)

def adjustValuesForNextBox(spaces,symbols):
    spaces = spaces - 1
    symbols = symbols + 2
    return spaces, symbols
#main program starts here
numberOfSpaces = int(input("Enter number of spaces : "))
numberOfSymbols = int(input("Enter number of symbols : "))
numberOfSpaces, numberOfSymbols = adjustValuesForNextBox(numberOfSpaces,numberOfSymbols)
print(numberOfSpaces)
print(numberOfSymbols) 
