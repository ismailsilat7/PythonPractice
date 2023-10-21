import getpass

#ask user to think of a number
#your program can ask yes or no questions (max 10)
#your program should tell the correct guess everytime

#initialize the values
lowest_num = 1
highest_num = 100
correct = 'n'

#ask user to think for a number
print(f"Think of a number between {lowest_num} & {highest_num}")
getpass.getpass("Press the enter key to continue ")
while correct == 'n':
    if ((highest_num - lowest_num) != 0):
        mid = int((highest_num + lowest_num)/2)
        answer = input(f"Is the number greater than {mid}? (y/n) : ").lower()
        if (answer == 'y'):
            lowest_num = mid + 1
        elif(answer == 'n'):
            highest_num = mid
        else:
            print("Invalid response, please respond with either 'y' or 'n'.")
    else:
        correct = input(f"Is your number {lowest_num}? (y/n) : ").lower()
        if correct != 'y':
            print("Oh, you're trying to trick me, aren't you?!")
            correct = 'y'
    
