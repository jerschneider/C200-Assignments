#variables 
#assignment statements

#program = sequence of statements

#functions

#-------------------------------------

import math

radius = input("enter the radius: ") #call input let it do its wokr
r = float(radius) 
volume = 4 / 3 * math.pi * r * r * r
message = ""
message = message + "the volume of a sphere with radius"
mesage = message + radius
message += " is "

print(message) #print("the volume of a sphere with radius " + radius + " is " + str(volume))

#--------------------------------------

#a function is a named computation (like a generalized formula)
#
#
#What is the signature of this function?
def fun(number):
    if (number > 10):
        return number + 2
    else:
        print("How come?")
#This is extremely poor style but legal ---->according to Mr. German
#
#Design recipe
#---->The signature of a function describes the mapping that the function implements.
# 
# a Number is one of:
# -- 0
# -- 1 + Number
# examples: 0. 1, 3, 125
#
#
#What : Number -> Boolean (that's the signature)
#what whill tell us if its argumenet is even or not
#examples: what(2) is True
#          what(5) is False

def what(number):
    if number % 2 == 0:
        return True
    else:
        return False



