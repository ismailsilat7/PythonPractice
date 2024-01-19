Animal = [''] * 20
Colour = [''] * 10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer, Animal
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True
    

def PopAnimal():
    global AnimalTopPointer, Animal
    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer = AnimalTopPointer - 1
        return Animal[AnimalTopPointer]
"""
def ReadData():
    try:
        FileHandle = open("AnimalData.txt", "r")
    except:
        print("File Doesn't Exist")
        return
    spaceAvailable = True
    while spaceAvailable:
        try:
            name = FileHandle.readline()
            spaceAvailable = PushAnimal(name)
        except EOFError:
            break
"""
def PushColour(DataToPush):
    global ColourTopPointer, Colour
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global ColourTopPointer, Colour
    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer = ColourTopPointer - 1
        return Colour[ColourTopPointer]

def ReadData():
    FileHandle = None
    try:
        FileHandle = open("AnimalData.txt", "r")
        while True:
            name = FileHandle.readline().strip()
            if not name:
                break
            spaceAvailable = PushAnimal(name)
            if not spaceAvailable:
                break
    except FileNotFoundError:
        print("File 'AnimalData.txt' Doesn't Exist")

    if FileHandle != None:
        FileHandle.close()

    FileHandle = None
    try:
        FileHandle = open("ColourData.txt", "r")
        while True:
            name = FileHandle.readline().strip()
            if not name:
                break
            spaceAvailable = PushColour(name)
            if not spaceAvailable:
                break
    except FileNotFoundError:
        print("File 'ColourData.txt' Doesn't Exist")

    if FileHandle != None:
        FileHandle.close()


def OutputItem():
    colourString = PopColour()
    animalString = PopAnimal()
    if colourString == "":
        print("No colour")
        PushAnimal(animalString)
    if animalString == "":
        print("No animal")
        PushColour(colourString)
    if animalString != "" and colourString != "":
        print(f"{colourString} {animalString}")

ReadData()
for _ in range(4):
    OutputItem()