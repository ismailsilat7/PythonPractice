#open(filename, mode)
# w = WRITE (create files/recreates file, store data)
# r = READ (req : The file should exist, fetches data)
# a = APPEND (req: file should exist, adds data at the end of file)

#WRITING THE FILE

FileHandle = open("SampleFile.TXT", "w")
FileHandle.write("Line of text to store\n")
FileHandle.write("This is my second line\n")
FileHandle.close()

#READING THE FILE

FileHandle = open("SampleFile.TXT", "r")
LineOfText = FileHandle.readline()
print(LineOfText)
FileHandle.close()

#APPENDING THE FILE
FileHandle = open("SampleFile.TXT", "a")
LineOfText = "Appended Text\n"
FileHandle.write(LineOfText)
FileHandle.close()
