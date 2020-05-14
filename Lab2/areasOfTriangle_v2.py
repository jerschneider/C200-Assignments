import math
#I entered these lines from Mr. German's lab page with my own edits/comments
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a = input("Please enter the length of the first side of the triangle >>> ")
#reminder float makes (a) a integer that's usebale through float, while string changes the integer to a string type
a = float(a) 
b = float(input("... now the second >>> ")) # in one step (b is never a string) this is a shortned version of (a)
c = float(input("... and the third >>> ")) # careful with the parens(?)
print("You have entered: " + str(a) + ", " +str(b) + ", and " + str(c))
#we need to keep the user (ourselves, at this point) in the loop
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Heron's Forumula (imported from Mr. German's notes)
#\/ below you must import the math module to use the square root command
#import math
#BUT this is improper style and according to Mr. German, no one would put this module callout here
s = (a + b + c) / 2
#area = ( s * (s - a) * (s - b) * (s - c) ) ** 0.5
area = math.sqrt( s * (s - a) * (s - b) * (s - c))
#^ the math command----> math.whatevercommand --->this command specifically calls the math module
print("The area for the triangle with those sides is: " + str(area))