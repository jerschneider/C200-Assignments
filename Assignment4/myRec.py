# create the functions in myRec
#use a loop and print out the first 10 values
#the test code must be writeen in the recTest.py
def function1(n):
    n = n
    for i in range (1, n) :
        return (n - 1 + n)
        n = n - 1

#TestCode
print("")
print("===function1===")
print( function1 (11) )
print( function1 (10) )
print( function1 (9) )
print( function1 (8) )
print( function1 (7) )
print( function1 (6) )
print( function1 (5) )
print( function1 (4) )
print( function1 (3) )
print( function1 (2) )
print("===END===")
print ("")

def closedFunct1(n):
    n = n
    for i in range (1, n) :
        return (n * (1 + n)) // 2
        n = n - 1

print("")
print("===closedFunct1===")
print( closedFunct1 (11) )
print( closedFunct1 (10) )
print( closedFunct1 (9) )
print( closedFunct1 (8) )
print( closedFunct1 (7) )
print( closedFunct1 (6) )
print( closedFunct1 (5) )
print( closedFunct1 (4) )
print( closedFunct1 (3) )
print( closedFunct1 (2) )
print("===END===")
print ("")


def funct2(n):
    n = n
    for i in range (1, n) :
        return ( (n - 1) + 0.02 * (n -1))
        n = n - 1

print("")
print("===funct2===")
print( funct2 (13) )
print( funct2 (12) )
print( funct2 (11) )
print( funct2 (10))
print( funct2 (9) )
print( funct2 (8) )
print( funct2 (7) )
print( funct2 (6) )
print( funct2 (5) )
print( funct2 (4) )
print( funct2 (3) )
print( funct2 (2) )
print("===END===")
print("")

def closedFunc2(n):
    n = n
    for i in range (1, n) :
        return (1.02)**n * 10000
        n = n - 1



