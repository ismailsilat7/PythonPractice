# run time errors occur for many reasons
# types of exceptions / run time errors in python:
# IOError: library or module can be found
# ValueError : when an argument is of inappropriate value
# KeyboardInterrupt : when u press ctrl + c/d
# EOFError : when end of file is reached
# ZeroDivisionError: when value is divided by zero

num = input("Enter an integer: ")
try:
    n = int(num)
    print(n)
except:
    print("Incorrect input. Should be Integer")


try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    ans = num1/num2
    print(ans)
except ZeroDivisionError:
    print("Number can not be divided by zero")
except ValueError:
    print("Incorrect Value")
except KeyboardInterrupt:
    print()
    print("Interrupt Occured")