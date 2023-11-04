#TASK1: create an array and ask user to enter 10 names in array
names = []
for i in range(3):
    name = input("Please enter a name : ").lower()
    names.append(name)

#TASK2: from TASK1 ask user for a name in the array & output the index of where it was found or output not found
searchName = input("Enter a name to find it's index in the array : ").lower()
found = False
for i in range(len(names)):
    if searchName == names[i]:
        print(i)
        found = True
if found == False:
    print("Name not Found")


#TASK3: create an array to store CS marks for CSC4 which has 65 students, take input for all marks for students

CSmarks = []
classSize = 5
print(f"Input marks for CS - CSC4 (class size = {classSize} students)")
for i in range(classSize):
    marks = -1
    while(marks < 0):
        marks = int(input("Marks : "))
    CSmarks.append(marks)

#TASK4: from TASK3, calculate class average, highest marks, lowest marks
highest = CSmarks[i]
lowest = CSmarks[i]
sum = CSmarks[i]
for i in range(1, len(CSmarks)):
    sum += CSmarks[i]
    if CSmarks[i] > highest:
        highest = CSmarks[i]
    elif CSmarks[i] < lowest:
        lowest = CSmarks[i]

average = sum/classSize
print(f"Highest Marks : {highest}, Lowest Marks : {lowest}, Class Average : {average}")

#TASK5: create an array to store names of all students in CSC4, same index for names as marks
CSnames = []
print(f"Input student names for CS - CSC4 (class size = {classSize} students)")
for i in range(classSize):
    name = input("Name : ").lower()
    CSnames.append(name)

#TASK6: output the names of all the students who scored highest & lowest marks
highestNames = []
lowestNames = []
for i in range(classSize):
    if CSmarks[i] == highest:
        highestNames.append(CSnames[i])
    if CSmarks[i] == lowest:
        lowestNames.append(CSnames[i])

print("Highest Marks scored by")
for i in range(len(highestNames)):
    print(highestNames[i])

print("Lowest Marks scored by")
for i in range(len(lowestNames)):
    print(lowestNames[i])

print(CSmarks)
print(CSnames)
#TASK7: sort the marks array & accordingly names array from highest to lowest marks

for i in range(classSize):
    for j in range(classSize - i):
        if CSmarks[j] < CSmarks[j + 1]:
            temp = CSmarks[j]
            CSmarks[j] = CSmarks[j+1]
            CSmarks[j+1] = temp
            tempName = CSnames[j]
            CSnames[j] = CSnames[j+1]
            CSnames[j+1] = tempName

print("Sorted")
print(CSmarks)
print(CSnames)