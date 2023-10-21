# TASK 2 : Ask user for a string, convert and store it in reverse

userStr = input("Please enter a string : ")
newStr = ''
for i in range(len(userStr)):
    newStr = newStr + userStr[len(userStr) - 1 - i]

print(newStr)

