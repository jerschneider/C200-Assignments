import math

#Larry's test-problem in Assignment1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#this retrieves the number of color pages printing from a terminal input
colorPages = input("what is the number of pages in color? >>>")
#Then this converts the string into an integer
numColorPages = int(colorPages)

#This retrieves the number of black and white pages printing from a terminal input
bwPages = input("what is the number of page in black and white? >>>")
#this next line converts the string into a an integer that can then be manipulated with math
numBWPages = int(bwPages)
#This is the calculation which will properly calculate the two example shown in Assignment 1
#As in if you were to plug 4Colorpages and 2BW into the terminal then 1.08 will be produced
theCost = (numColorPages * .25) + (numBWPages * .04)

#Displays the cost. the last part converts the decimal to a string which can then be outputed
print("The cost is " + str(theCost))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~