# Classes have a relationship
#Containment means that ibe class contains other classes
# A class can have objects of another class
# Car class & tyre class
# Car class can contain objects of tyre class

class lesson:
    def __init__(self,t,d,r):
        self.lessonTitle = t
        self.duration = d
        self.requiresLab = r
    def outputLessonDetails(self):
        print("Lesson Details")
        print(f"Course Title = {self.lessonTitle} for the duration = {self.duration} and lab status = {self.requiresLab}")

class assessment:
    def __init__(self,t,m):
        self.assessmentTitle = t
        self.totalMarks = m
    def outputAssessmentDetails(self):
        print("Assessment Details:")
        print(f"Assessment Title = {self.assessmentTitle} and max marks is {self.totalMarks}")

class course:
    def __init__(self,t,s):
        self.courseTitle = t
        self.maxStudents = s
        # This is an empty list that will store lesson objects
        self.courseLesson = []
        self.totalLesson = 0
        # object of assessment class is stores in this variable
        self.courseAssessment = assessment
    def addLesson(self,t,d,r):
        self.courseLesson.append(lesson(t,d,r))
        self.totalLesson += 1
    def addAssessment(self,t,m):
        self.courseAssessment = assessment(t,m)
    def outputCourseDetails(self):
        self.courseAssessment.outputAssessmentDetails()
        for i in range(self.totalLesson):
            self.courseLesson[i].outputLessonDetails()

myCourse = course("Computer Science", 50)
myCourse.addLesson("OOP", 120, True)
myCourse.addLesson("Hardware", 180, False)
myCourse.addLesson("System Software", 100, False)
myCourse.addAssessment("Mock exam", 200)
myCourse.outputCourseDetails()