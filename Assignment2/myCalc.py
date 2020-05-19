import math # You might or might not need this

def speed(distance, time):
    Speed = (distance / time)
    return Speed 
#    """
#    Calculate the speed based on the distance time. 
#   Parameters: distance is in miles and time in hour
#    Returns: speed in miles per hour
#    """
#    #pass # Remove as needed

def distance(speed, time):
   Distance = (time * speed)
   return Distance
    #"""
    #Caluclates the distance travelled 
    #Paramters: speed is in MPH and time in hour
    #Returns: Distance in Miles
    #"""
    #pass # Remove as needed

def time(speed, distance):
    Time = (distance / speed)
    return Time
#    """
#    Calculates the time travelled
#    Parameters: speed in MPH, distance in Miles
#    Returns: Time in hours
#    """
#   pass # Remove as needed

def hour2min(numHours):
    Hour2min = (60 * numHours)
    return Hour2min
    
#    """
#    Converts from hours to minutes
#    """
#    #pass # Remove as needed

def min2hour(numMinutes):
    Min2hour = (numMinutes / 60)
    return Min2hour
#    """
#    Converts from minutes to hours
#    """
#    pass # Remove as needed

def min2sec(numMinutes):
    Min2sec = (numMinutes * 60)
    return Min2sec 
#    """
#    Convert minutes to seconds
#    """
#    pass # Remove as needed

def sec2min(numSec):
    Sec2min = (numSec / 60)
    return Sec2min
#    """
#    Convert seconds to minutes
#    """
#    pass # Remove as needed

def feet_to_mile(numFeet):
    Feet_to_mile = (numFeet / 5280)
    return Feet_to_mile

def miles_to_feet(numMile):
    Miles_to_feet = (numMile * 5280)
    return Miles_to_feet

def kilometers2miles(numKilo):
    Kilometer2miles = (numKilo / 1.60934)
    return Kilometer2miles


def miles2kilometers(numMiles):
    Miles2kilometers = (numMiles * 1.60934)
    return Miles2kilometers


def degrees_to_radians(numDegrees):
    Degrees_to_radians = (numDegrees * (math.pi / 180))
    return Degrees_to_radians

def sideLengthTriangle(a, b, gamma):
   SideLengthTriangle = (math.sqrt(((a * a) + (b * b)) - (2 * a * b) * (math.cos(gamma * (math.pi / 180)))))
   return SideLengthTriangle

def celsius2fahrenheit(numDegC):
   Celsius2fahrenheit = (9 / 5) * numDegC + 32
   return Celsius2fahrenheit

def fahrenheit2celsius(numDegF):
   Fahrenheit2celsius = (numDegF -32) / (9 / 5)
   return Fahrenheit2celsius

def kelvin2fahrenheit(numKel):
    kelvin2Celsius = numKel - 273
    Kelvin2fahrenheit = (9 / 5) * kelvin2Celsius +32
    return Kelvin2fahrenheit

def pc(s, d):
    Pc = ((s + d) - s) / s * 100
    return Pc

def parsecs2kilometer(numParsecs):
    Parsecs2kilometer = (numParsecs / (10 ** 13)) / 3.086
    return Parsecs2kilometer

def kilometer2parsecs(numKilo):
    Kilometer2parsecs = 3.086 * (10 ** 13) * numKilo
    return Kilometer2parsecs

def lightyears2parsecs(numLY):
    Lightyears2parsecs = numLY / 3.26
    return Lightyears2parsecs

def quadraticFormula(a, b, c):
   QuadraticFormula = [(-b) - (math.sqrt((b ** 2) - 4 * a *c))) / (2 * a)], [((-b) + (math.sqrt((b ** 2) - 4 * a *c))) / (2 * a)]
   return QuadraticFormula



###### Testing Code ######
#/\this command is call to an internal (python) function
if __name__ == "__main__":
    print("Speed: ", round(speed(100, 60), 2), " miles / hour")
    print("Speed: ", round(speed(1234, 10), 2), " miles / hour")
    print("Speed: ", round(speed(32, 60), 2), " miles / hour")

    print("Distance: ", distance(100, 60), " miles")
    print("Distance: ", distance(1234, 10), " miles")
    print("Distance: ", distance(32, 6), " miles")

    print("Time: ", round(time(100, 60), 3), " hours")
    print("Time: ", round(time(1234, 10), 3), " hours")
    print("Time: ", round(time(32, 60), 3), " hours")

    print("Hours to minutes: ", hour2min(1), " minutes")
    print("Hours to minutes: ", hour2min(1234), " minutes")
    print("Hours to minutes: ", hour2min(24), " minutes")

    print("Minutes to hours: ", round(min2hour(54), 2), " hours")
    print("Minutes to hours: ", round(min2hour(1234), 2), " hours")
    print("Minutes to hours: ", round(min2hour(60), 2), " hours")

    print("Minutes to seconds: ", min2sec(60), " seconds")
    print("Minutes to seconds: ", min2sec(1234), " seconds")
    print("Minutes to seconds: ", min2sec(32), " seconds")

    print("Seconds to minutes: ", round(sec2min(60), 2), " minutes")
    print("Seconds to minutes: ", round(sec2min(1234), 2), " minutes")
    print("Seconds to minutes: ", round(sec2min(32), 2), " minutes")

    print("Feet to miles: ", round(feet_to_mile(1234), 4), " miles")
    print("Feet to miles: ", round(feet_to_mile(12), 4), " miles")
    print("Feet to miles: ", round(feet_to_mile(32), 4), " miles")

    print("Miles to feet: ", miles_to_feet(1526), " feet")
    print("Miles to feet: ", miles_to_feet(1), " feet")
    print("Miles to feet: ", miles_to_feet(4), " feet")

    print("Kilometers to miles: ", round(kilometers2miles(100), 2), " miles")
    print("Kilometers to miles: ", round(kilometers2miles(1234), 2), " miles")
    print("Kilometers to miles: ", round(kilometers2miles(32), 2), " miles")

    print("Miles to kilometers: ", round(miles2kilometers(100), 2), " kilometers")
    print("Miles to kilometers: ", round(miles2kilometers(1234), 2), " kilometers")
    print("Miles to kilometers: ", round(miles2kilometers(32), 2), " kilometers")

    print("Degrees to radians: ", round(degrees_to_radians(10), 2), " radians")
    print("Degrees to radians: ", round(degrees_to_radians(12), 2), " radians")
    print("Degrees to radians: ", round(degrees_to_radians(271), 2), " radians")

    print("Length of the side of a triangle: ", round(sideLengthTriangle(8, 11, 37), 4), " length")
    print("Length of the side of a triangle: ", round(sideLengthTriangle(12, 3, 197), 4), " length")
    print("Length of the side of a triangle: ", round(sideLengthTriangle(7, 14, 40), 4), " length")

    print("Celsius to Fahrenheit: ", celsius2fahrenheit(100), " Fahrenheit")
    print("Celsius to Fahrenheit: ", celsius2fahrenheit(12), " Fahrenheit")
    print("Celsius to Fahrenheit: ", celsius2fahrenheit(32), " Fahrenheit")

    print("Fahrenheit to Celsius: ", round(fahrenheit2celsius(100), 4), " Celsius")
    print("Fahrenheit to Celsius: ", round(fahrenheit2celsius(12), 4), " Celsius")
    print("Fahrenheit to Celsius: ", round(fahrenheit2celsius(32), 4), " Celsius")

    print("Kelvin to Fahrenheit: ", round(kelvin2fahrenheit(100), 2), " Fahrenheit")
    print("Kelvin to Fahrenheit: ", round(kelvin2fahrenheit(12), 2), " Fahrenheit")
    print("Kelvin to Fahrenheit: ", round(kelvin2fahrenheit(60), 2), " Fahrenheit")

    print("Percent Change (pc): ", round(pc(170.90, 3.31), 2), " % ")
    print("Percent Change (pc): ", round(pc(170.90, -3.31), 2), " % ")
    print("Percent Change (pc): ", round(pc(-70.90, -3.31), 2), " % ")

    print("Parsecs to Kilometers: ", round(parsecs2kilometer(.08), 2), " kilometers")
    print("Parsecs to Kilometers: ", round(parsecs2kilometer(1234), 2), " kilometers")
    print("Parsecs to Kilometers: ", round(parsecs2kilometer(32), 2), " kilometers")

    print("Kilometers to Parsecs: ", round(kilometer2parsecs(100), 2), " Parsecs")
    print("Kilometers to Parsecs: ", round(kilometer2parsecs(1234), 2), " Parsecs")
    print("Kilometers to Parsecs: ", round(kilometer2parsecs(32), 2), " Parsecs")

    print("Lightyears to parsecs: ", round(lightyears2parsecs(60), 2), " Lightyear to Parsec")
    print("Lightyears to parsecs: ", round(lightyears2parsecs(10), 2), " Lightyear to Parsec")
    print("Lightyears to parsecs: ", round(lightyears2parsecs(32), 2), " Lightyear to Parsec")

    print("Quadratic Formula: ", quadraticFormula(2, 5, -10), " numbers")
    print("Quadratic Formula: ", quadraticFormula(2, 0, -64), " numbers")
    print("Quadratic Formula: ", quadraticFormula(4, 1, 4), " numbers")