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
#^above is almost complete but it does not have a visual terminal output nor is it rounded
#^which results in a gross number if outputted without rounding
#
#So down here, this command will take the ball's volume and round it up to the 2nd number of digits in the decimal place
#Then the print statement will take the output and put the value entered back to string so it can be outputted :)
roundedBallVolume = round(ballVolume, 2)
print( "the volume of the ball is >>> " + str(roundedBallVolume))
#Finally when I enter a radius of 5.5 I then get a volume of 696.91 
#Or if I enter a ball radius of 0.5 the volume is 0.52 which is correct according to 'Assignment1'