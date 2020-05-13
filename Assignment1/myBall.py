import math
#things to know for this problem:
#
#str() turns an integer into string 
#AND float() turns a string into a decimal value
#
#math.pi will give you the value of pi
#
#round (num, 2) will take a number (place num) and round to a certain number of digits, here 2.

radius = input("what is the radius of the ball? >>>")
ballRadius = float(radius)

ballVolume = (4/3) * (math.pi * (ballRadius ** (3)))
print( "the volume is >>> " + str(ballVolume))