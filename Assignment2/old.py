import math
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Problem 2

#tomato will be passed through this function
def themath(tomato):
    Themath = (tomato *150)-15
    return Themath



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Problem 3
def thecost(numColorPages, numBWPages):
    Thecost = (numColorPages * .25) + (numBWPages * .04)
    return Thecost


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Problem 4

def bouncing(radius):
    Ball = (4/3) * (math.pi) * (radius ** (3))
    Bouncing = round(Ball)
    return Bouncing


print("Assignment 1 Problem 2: " + str(themath(10)))
print("Assignment 1 Problem 3: " + str(thecost(4, 2)))
print("Assignment 1 Problem 4: " + str(bouncing(5.5)))
