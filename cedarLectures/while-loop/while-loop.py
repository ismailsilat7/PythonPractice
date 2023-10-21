Answer = ''
while Answer != 'Y':
    Answer = input("Enter Y : ")
print("Outside the loop")

#Q1. convert the triangle code to only use while loop
#Q2. convert the pyramid code to only use while loop
#Q3. rock paper scissors : include validation for input

#Q1
triangle_height = int(input("Enter height of the triangle : "))
i = 0
j = 0
while (i < triangle_height):
    while (j < i + 1):
        print("#", end = "")
        j  += 1
    print()
    j = 0
    i += 1
print()

#Q2
pyramid_height = int(input("Enter pyramid height : "))
i = 0
space = 0
hashes = 0
while (i < pyramid_height):
    while (space < (pyramid_height - (i + 1))):
        print(" ", end = "")
        space += 1
    space = 0
    while (hashes < i + 1):
        print ("#", end = "")
        hashes += 1
    hashes = 0
    while (hashes < i):
        print ("#", end = "")
        hashes += 1
    hashes = 0
    print()
    i += 1
print()