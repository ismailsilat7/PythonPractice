class Vehicle:
    # self.__ID : STRING
    # self.__MaxSpeed : INTEGER
    # self.__CurrentSpeed : INTEGER
    # self.__IncreaseAmount : INTEGER
    # self.__HorizontalPosition : INTEGER
    def __init__(self,i,ms,ia):
        self.__ID = i
        self.__MaxSpeed = ms
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = ia
        self.__HorizontalPosition = 0


    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__MaxSpeed
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self,cs):
        self.__CurrentSpeed = cs
    def SetHorizontalPosition(self,hp):
        self.__HorizontalPosition = hp
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        
        self.__HorizontalPosition += self.__CurrentSpeed
    
    def OutputDetails(self):
        print(f"Horizontal position: {self.__HorizontalPosition}")
        print(f"CurrentSpeed: {self.__CurrentSpeed}")

class Helicopter(Vehicle):
    # self.__VerticialPosition : INTEGER
    # self.__VerticalChange : INTEGER
    # self.__MaxHeight : INTEGER
    def __init__(self,i,ms,ia,vc,mh):
        Vehicle.__init__(self,i,ms,ia)
        self.__VerticialPosition = 0
        self.__VerticalChange = vc
        self.__MaxHeight = mh
        
    def IncreaseSpeed(self):
        Vehicle.IncreaseSpeed(self)
        self.__VerticialPosition += self.__VerticalChange
        if self.__VerticialPosition > self.__MaxHeight:
            self.__VerticialPosition = self.__MaxHeight
    
    def OutputDetails(self):
        Vehicle.OutputDetails(self)
        print(f"Vertical Position: {self.__VerticialPosition}")


car = Vehicle("Tiger", 100, 20)
heli = Helicopter("Lion", 350, 40, 3, 100)

car.IncreaseSpeed()
car.IncreaseSpeed()
car.OutputDetails()

heli.IncreaseSpeed()
heli.IncreaseSpeed()
heli.OutputDetails()

        
