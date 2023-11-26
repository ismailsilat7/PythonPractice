
def recursivefunction(num):
    print(num)
    print("naam bataiye")
    print("Bhupender Jogi")
    print("Ap US mai kahan kahan gaye hein")
    print("Mai US mai boht jagah gaya hoon")
    if num < 5: #BASE CASE :)
        recursivefunction(num + 1)
recursivefunction(1)

#TASK 1: make a recursive function that counts down from the parameter given
def countdown(num): 
    if num > -1:
        print(num)
        countdown(num-1)
countdown(10)

#TASK 2: make a recursive function that returns the sum of all values from 1 to parameter number
def countsum(num):
    if num > 1:
        return countsum(num-1) + num
    else:
        return 1

print(countsum(5))

#TASK 3: Make a recursive function that takes a position number value as input and outputs fibonacci sequence till that position

def fib(pos):
    if pos == 1 or pos == 2:
        return 1
    else:
        temp = fib(pos-1) + fib(pos-2)
        return temp

pos = int(input("Please enter the position for the fibonacci sequence : "))
for i in range(1, pos + 1):
    print(fib(i), end=" ")

