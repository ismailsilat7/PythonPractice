#Q1. ask user for the age and output if the user is an adult, child or teen

age = int(input("Please Enter Your Age : "))
if age >= 18:
    print("You are an adult")
elif age > 6:
    print("You are a teen")
else: 
    print("Hello Buckaro!")

#Q2. ask user for the lucky number & out if it is odd or even & if it is divisible by 10

luckyNumber = int(input("Enter your Lucky Number : "))
if (luckyNumber % 10 == 0):
    print("Even & divisble by 10")
elif (luckyNumber % 2 == 0):
    print("Even")
else:
    print("Odd")