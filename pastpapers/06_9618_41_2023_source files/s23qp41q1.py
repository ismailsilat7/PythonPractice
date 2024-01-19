
#Q1ai
DataArray = [] #ARRAY[0:24] OF INTEGER

#Q1aii
try:
    fileHandle = open("Data.txt","r")
    for i in range(25):
        oneline = fileHandle.readline()
        DataArray.append(int(oneline))
    fileHandle.close()
except IOError:
    print("File doesn't exist")

#Q1bi
def PrintArray(DataArray):
    for i in range(len(DataArray)):
        print(DataArray[i], end=" ")

#Q1bii
PrintArray(DataArray)
print()
#Q1c
def LinearSearch(DataArray, SearchItem):
    count = 0
    for i in range(len(DataArray)):
        if DataArray[i] == SearchItem:
            count += 1
    return count

#Q1d
searchItem = int(input("Enter a number between 0 & 100 to search: "))
while searchItem < 0 and searchItem > 100:
    searchItem = int(input("Enter a number between 0 and 100 to search: "))
count = LinearSearch(DataArray, searchItem)
print(f"The number {searchItem} is found {count} times.")


