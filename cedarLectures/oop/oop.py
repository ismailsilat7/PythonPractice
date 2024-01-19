#OBJECT ORIENTED PROGRAMMING

#Class Attributes and methods

#Class definition is a bluearánt

#Cam: Attributes id, registration, engine size, purchase price. Methods accel, brake, turn right...

#Private: Hidtien From the user/programmer. All attributes private

#Public: Visible for everyone. 811 methods public

#Getter method: return attribute

#Setter method: assign value to attribute

#DOP features: Encapsulation, Inheritance, Polymerahiom, Containment (aggregation)

#Encapsulation: Hading attributes from users

#CAR CLASS
class car:
#Constructor: в преслат Туре of methed that is called to anate a new elect and Anitialize its attributes An.called automatically

# Constructor is private. No one can call constructor.

#init the name of constructor in python

# to show something is private

    def __intit__(self, i, e):

    # all attributes are private hence encapsulated
        self.__carID = i
        self.__registration =""
        self.__dateOfRegitration = None
        self.__engineSize = e
        self.__purchasePrice = 0
    
    # Get methods 
    # return the ettributes
    def getCarId(self):
        return self.__carID
    def getRegitration(self):
        return self.__registration
