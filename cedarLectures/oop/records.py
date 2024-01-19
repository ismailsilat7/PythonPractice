# records are just classes without methods
# all attributes will be public and can be used without the methods

class carRecord:
    def __init__(self):
        self.vehicleID = ""
        self.registration = ""
        self.DateOfRegitration = ""
        self.engineSize = 0
        self.purchasePrice = 0.0

myCar = carRecord()
myCar.engineSize = 1000
print(myCar.engineSize)
# arrayName = [initialValue/class objects for i in range(totalSize)]
allCars = [carRecord() for i in range(100)]
for i in range(100):
    allCars[i].engineSize = 100 * (i+1)
for i in range(100):
    print(i, ":", allCars[i].engineSize)



# binary files are used to store data in binary
# records/objects/classes will be stored in files as binary so that the data can be retreived directly in the class
#pickle is required to create binary files
import pickle
#open file for binary write
fileHandle = open("Carfile.DAT", "wb")
for i in range(100):
    pickle.dump(allCars[i],fileHandle)
fileHandle.close()

fileHandle = open("Carfile.DAT", "rb")
myCars = []
fileFlag = True
while fileFlag:
    try:
        myCars.append(pickle.load(fileHandle))
    except EOFError:
        fileFlag = False
        print("End of File")
fileHandle.close()
for i in range(100):
    print(myCars[i].engineSize)