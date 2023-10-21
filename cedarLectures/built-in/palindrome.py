# TASK 1 - Ask user for a string and output if the string is palindrome

userStr = input("Please enter a string : ").lower()

is_palindrome = True

for i in range(len(userStr)):
    if (userStr[i] != userStr[len(userStr) - 1 - i]):
        is_palindrome = False
        break

if (is_palindrome == True):
    print(f"{userStr} is a palindrome")
else:
    print(f"{userStr} is not a palindrome")

