x = int(input("Enter a number : "))
if x < 0:
    print("Negative")
elif x > 0:
    print("Positive")
else:
    print("Zero")

#Q1. Ask user for the age and output if the user is an adult or not
#Q2. Ask user if monkey A and Monkey B are smiling, if either or both are smiling you are in trouble
#Q3. Ask user if he/she is on vacation & if it's a weekday. Output if the user can sleep late
#q4. Ask user for their lucky number & output if the Lucky Number is odd or even

age = int(input("Please Enter your Age : "))
if age >= 18:
    print("You are an adult")
else:
    print("Hello buckaro!")

monkeyA = input("Is Monkey A smiling? (yes/no) : ")
monkeyB = input("Is Monkey B smiling? (yes/no) : ")
if (monkeyA != "yes" and monkeyB != "yes"):
    pass
else:
    print("You are in trouble")

onVacation = input("Are you on a vacation? (yes/no) : ")
isWeekDay = input("Is today a weekday? (yes/no) : ")
if (onVacation == "yes" or isWeekDay == "no"):
    print("You can sleep late")
else:
    print("SLEEP EARLY!")



luckyNumber = int(input("Enter your Lucky Number"))
if luckyNumber%2 == 0:
    print("even")
else:
    print("odd")
    
