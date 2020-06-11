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
        self.birthYear = birthYear
        self.friends = []
    
    
    
    class student(Person):
        def __init__(self, name, birthYear, major, startCredits = 0):
            super().__init__(name, birthYear)
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

    
    
    
    class instructor(Person):
        def __init__(self, name, birthYear, officeHours, officeRoom, startSalary = 50000):
            super().__init__(name, birthYear)
            self.startSalary = startSalary
            self.officeHours = officeHours
            self.officeRoom = officeRoom
            self.name = name

        def earnedCredits(self, xStudent, credits):
            xStudent = self.xStudent
            xStudent.credits += credits
        
        def getMajors(self):
            majorslist = {}
            for i in self.listOfStudents:
                if not i in majorslist:
                    majorslist[i] = 1
                else:
                    majorslist[i] += 1
            return majorslist


    def giveOfficeHours(self, name, officeHours, officeRoom):
        for i in self.instructors:
            newOfficeHours = self.officeHours(name, i officeHours, officeRoom)
            i.officeHours.append(newOfficeHours)
            print(i.name + "has office hours at" + name)

##test code
studentNames = ["Edwin Johnston", "Isabella Stewart", "Donna Reed", "Luke Hall", "Carina Hunt", "Derek Chapman", "Emily Harris", "Arthur Harris", "Jeremy Schneider", "Natalie Mitchell", "Nicholas Douglas", "Sawyer Roberts", "Adrian Thompson", "Richard Long"]
studentMajors = ["Computer Science", "Computer Science", "Informatics", "Informatics", "Informatics", "Computer Science", "Biology", "Biology", "Biology", "Gender Studies", "Gender Studies", "English", "English", "English"]
studentYears = [1980, 1987, 1989, 1996, 1989, 1982, 1988, 1990, 1982, 1996, 1985, 1998, 1989, 1986]
testperson = Person()
instructorsNames = ["Belinda Hamilton", "Derek Bailey", "Lucy Perkins", "Leonardo Williams", "Jacob Riley", "Lenny Murray"]
instructorsYears = [1964, 1968, 1967, 1980, 1962, 1967]
instructorsHours = [("Tuesday", "4:00-6:30"), ("Wednesday", "2:30-3:30"), ("Monday", "3:00-4:30"), ("Thursday", "3:00-5:00"), ("Friday", "4:00-5:00")]
instructorsRooms = ["Lindley 220", "Luddy 310", "Luddy 215", "Woodburn 110", "Hodge 350", "Woodburn 120"]
studentlist = []
instructorlist = []
for i in range(1, 15):
    studentList.append(student(studentNames[i], studentYears[i] studentMajors[i]))
for i in range(1, 7):
    instructorlist.append(instructor(instructorNames[i], instructorsYears[i], instructorsHours[i], instructorsRooms[i]))

        

