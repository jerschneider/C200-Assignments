#design a course
#create assignments
    ##this is going to be a class
    #maybe a superclass
    #quizzes, exams, labs and homework, and attendance

    ##things to consider for Assignments >>> the 
##superclass
#superclass is course
#subclass is assignemnts

#list of students

import random as rn

class course(): 
    def __init__(self, name): #lets begin with just the course name
        self.name = name
        self.students = [] #list for student pool
    class student(): #subclass for students
        def __init__(self, name, startGrade = 0):
            self.grade = startGrade
            self.assignments = [] #plural
            self.name = name
        
        def isPassing(self):
            if self.grade >= 60: #D grade
                return True
            else:
                return False

    def addStudent(self, name, grade = 0): # start every student off with a grade  of 0, we will be doing this in percents
        self.students.append(self.student(name, grade))
    def dropStudent(self, name):
        del self.students[name]
    class assignment(): #specific 
        def __init__(self, xType, pointValue, xStudent, name, topic):
            self.xType = xType 
            self.pointValue = pointValue
            self.xStudent = xStudent
            self.name = name
            self.topic = topic
            ##here we defined the assignment subclass which includes weather its a hw,quiz, etc >>> its point worth >>> who the student assigned was >>> and the name of the assignment >>> and the topic of the assingment
        def turnItIn(self, grade): ## this represents the student completing the assignment and their grade being recorded
            xStudent = self.xStudent
            xStudent.grade += grade
        


    def assign(self, xType, pointValue, name, topic): #first method
        for i in self.students:
            newAssignment = self.assignment(xType, pointValue, i, name, topic)
            i.assignments.append(newAssignment)
            print(i.name + " was assigned " + name)
            #this method assigns a given assignment to a given student in the course
    



## test code
studentlist = ["John Dryden", "Terry Eagleton", "Brecht", "Chechov", "Sophocles"]
testcourse = course("CS200")
for i in studentlist:
    testcourse.addStudent(i)
print(testcourse.students)
testcourse.assign("Homework", 100, "Problem 3: Inheritance", "Object-Oriented Programming")

for i in testcourse.students:
    for x in i.assignments:
        x.turnItIn(rn.randint(1, 100)) #students turn in all their assignments and get graded
    if i.isPassing():
        print(i.name + " is passing " + testcourse.name + " with a grade of " + str(i.grade) + "!")
    else:
        print(i.name + " is failing " + testcourse.name + " with a grade of " + str(i.grade) + " :(")
