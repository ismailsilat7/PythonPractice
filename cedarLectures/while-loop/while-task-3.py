#ask user for their name & output a decorated sign
"""
eg : name = ismail
**********
* ismail *
**********
"""

name = input("Please enter your name : ")
print("Here is a decorated sign for you")
for line in range(3):
    if (line % 2 != 0):
        print(f"* {name} *")
    else:
        for stars in range(len(name) + 4):
            print("*", end='')
        print()

