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

import random
class Person():
    def __init__(self, name, birthYear):
        self.name = name
        self.birthYear = birthYear
        self.friends = []
    
    
    
class student(Person):
    def __init__(self, name, birthYear, major, studentID, startCredits = 0):
        super().__init__(name, birthYear)
        self.credits = startCredits
        self.major = major
        self.studentID = studentID #i just gave the students an id number based on their order of creation. 
        #since we don't have many students it might look alittle weird
        self.name = name
    
    def hasCredits(self):
        if self.credits >= 1:
            return True
        else:
            return False

    def earnedCredits(self, credits):
        self.credits += credits

    
    
    
class instructor(Person):
    def __init__(self, name, birthYear, officeHours, officeRoom, startSalary = 50000):
        super().__init__(name, birthYear)
        self.startSalary = startSalary
        self.officeHours = officeHours
        self.officeRoom = officeRoom
        self.name = name
        self.students = []
        
    def getMajors(self):
        majorslist = {}
        for i in self.students:
            if not i.major in majorslist:
                majorslist[i.major] = 1
            else:
                majorslist[i.major] += 1
        return majorslist

    def addStudent(self, name, credits = 0):
        self.students.append(self.student(name, credits)) #not sure if I implemeneted this correctly
    def dropStudent(self, name):
        del self.students[name]

    """
    def giveOfficeHours(self, name, officeHours, officeRoom):
        for i in self.instructors:
            newOfficeHours = self.officeHours(name, i officeHours, officeRoom)
            i.officeHours.append(newOfficeHours)
            print(i.name + "has office hours at" + name)
    """
##test code
studentNames = ["Edwin Johnston", "Isabella Stewart", "Donna Reed", "Luke Hall", "Carina Hunt", "Derek Chapman", "Emily Harris", "Arthur Harris", "Jeremy Schneider", "Natalie Mitchell", "Nicholas Douglas", "Sawyer Roberts", "Adrian Thompson", "Richard Long"]
studentMajors = ["Computer Science", "Computer Science", "Informatics", "Informatics", "Informatics", "Computer Science", "Biology", "Biology", "Biology", "Gender Studies", "Gender Studies", "English", "English", "English"]
studentYears = [1980, 1987, 1989, 1996, 1989, 1982, 1988, 1990, 1982, 1996, 1985, 1998, 1989, 1986]
instructorNames = ["Belinda Hamilton", "Derek Bailey", "Lucy Perkins", "Leonardo Williams", "Jacob Riley", "Lenny Murray"]
instructorsYears = [1964, 1968, 1967, 1980, 1962, 1967]
instructorsHours = [("Tuesday", "4:00-6:30"), ("Wednesday", "2:30-3:30"), ("Monday", "3:00-4:30"), ("Thursday", "3:00-5:00"), ("Friday", "4:00-5:00")]
instructorsRooms = ["Lindley 220", "Luddy 310", "Luddy 215", "Woodburn 110", "Hodge 350", "Woodburn 120"]
studentlist = []
instructorlist = []
for i in range(14):
    #studentlist.append(student("jim", 1982, "biology", 1))
    studentlist.append(student(studentNames[i], studentYears[i], studentMajors[i], i+1))
for i in range(5):
    instructorlist.append(instructor(instructorNames[i], instructorsYears[i], instructorsHours[i], instructorsRooms[i]))

for i in studentlist:
    for x in range(random.randint(2, 5)):
        newfriend = (random.choice(random.choice([studentlist, instructorlist])))
        if not newfriend in i.friends:
            i.friends.append(newfriend)
for i in instructorlist:
    for x in range(random.randint(2, 5)):
        newfriend = (random.choice(random.choice([studentlist, instructorlist])))
        if not newfriend in i.friends:
            i.friends.append(newfriend)

for i in instructorlist:
    for x in range(random.randint(3,8)):
        i.students.append(random.choice(studentlist))

examplestudent = random.choice(studentlist)
exampleinstructor = random.choice(instructorlist)
(day, hours) = exampleinstructor.officeHours
print("Hi my name is", exampleinstructor.name, "and I was born in", exampleinstructor.birthYear)
print("My office hours are on", day, "at " + str(hours) + ". You can find me at", exampleinstructor.officeRoom)
print("My friends are: ", end="")
for i in exampleinstructor.friends:
    print(i.name, end=", ")
print("")
print("I teach: ", end=" ")
for i in exampleinstructor.students:
    print(i.name, end=", ")
print("")
majorscount = exampleinstructor.getMajors()
#print(majorscount)
majorsdict = list(majorscount.keys())
print("I have", majorscount[majorsdict[0]], "students in the", majorsdict[0], "major")
print("I teach in the following deparments:")
print(majorsdict)

print("My name is", examplestudent.name)
print("I have an ID number and it is", examplestudent.studentID)