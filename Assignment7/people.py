#make a superclass Person
    #Person >>> has name and year of birth
    #every person has a list of friends which includes Student or an Instructor
#   >>>two classes >>>> Student and Instructor
# the classes inherit from Person
#Student has major, credits earned, and a student ID
#Intructor has a salary and office hours, and a list of students they teach, and an instructor can get the unique majors from all the students they teach and number for each major
#ALSO for office hours, you need to have a day and room they hold office hours (string each)


#Write:
#  the class declarations, the constructors, and the string method for all classes

#Also supply a test program that tests these classes and methods

class Person():
    def __init__(self, name, birthYear):
        self.name = name
        self.birthYear = yearOfBirth
        self.students = []
        self.instructor = []
        self.friends = []
    
    
    
    class student():
        def __init__(self, name, major, startCredits = 0):
            self.credits = startCredits
            self.major = major
            self.studentID = []
            self.name = name
    
    def hasCredits(self):
            if self.credits >= 1:
                return True
            else:
                return False
    
    def addStudent(self, name, credits = 0):
        self.students.append(self.student(name, credits)) #not sure if I implemeneted this correctly
    def dropStudent(self, name):
        del self.students[name]
        
        
    #I need to use a random generator here in function to make student's ID
    # I need to add a credit counter

    
    
    
    class instructor():
        def __init__(self, name, startSalary = 0, officeHours, officeRoom, xStudent):
            self.startSalary = startSalary
            self.officeHours = []
            self.officeRoom = []
            self.listOfStudents = []
            self.name = name

        def earnedCredits(self, credits):
            xStudent = self.xStudent
            xStudent.credits += credits

    def giveOfficeHours(self, name, officeHours, officeRoom):
        for i in self.instructors:
            newOfficeHours = self.officeHours(name, i officeHours, officeRoom)
            i.officeHours.append(newOfficeHours)
            print(i.name + "has office hours at" + name)

##test code
studentList = "Edwin Johnston", "Isabella Stewart", "Donna Reed", "Luke Hall", "Carina Hunt", "Derek Chapman", "Emily Harris", "Arthur Harris", "Jeremy Schneider", "Natalie Mitchell", "Nicholas Douglas", "Sawyer Roberts", "Adrian Thompson", "Richard Long"]
testperson = person("people")
for i in studentlist:
    testperson.addStudent(i)
    print(testperson.students)
    testperson.giveOfficeHours("time", 2:00, "room", 234)

        

