"""
#TASK : Create a file called "names.txt"
#ask user to store 10 names in the file

FileHandle = open("names.txt", "w")

for line in range(10):
    name = input("Enter a name : ")
    FileHandle.write(f"{name}\n")

FileHandle.close()


#TASK : Read file"names.txt" and copy all names with less than 5 characters in a newfile namely 'favNames.TXT'

FileHandle = open("names.txt", "r")
FavNames = open("favNames.TXT", "w")
for i in range(10):
    oneline = FileHandle.readline().strip()
    if len(oneline) < 5:
        FavNames.write(oneline + "\n")

FileHandle.close()
FavNames.close()
"""
# TASK: Read file "names.txt" and copy names which are not currently in the file "newNames.txt"
# assuming max lines = 87

names = open('names.txt', 'r')
new = open('newNames.txt', 'r')
NewNames = []

for i in range(14):
    oneline = names.readline()
    notfound = True

    for j in range(10):
        newline = new.readline()
        if oneline.lower() == newline.lower():
            notfound = False
            break

    if notfound:
        NewNames.append(oneline.strip())

names.close()
new.close()

new = open('newNames.txt', 'a')
for name in NewNames:
    new.write(f"{name}\n")
new.close()
