#probem 1
#count the number of vowels in its input

def vowelCount(word):
    #pass
    result = 0
    for letter in word:
        if letter in "eiuoaEIUOA":
        #if letter == 'a' or letter == 'e': #this is enefficient because you will need 10 conditions to do this method
            result = result + 1
        else:
            pass
    return result

print("Problem 1: Vowel Count")
print(vowelCount ("banana"), "expected: 3") # 3 vowels is expected
print("")

#probem 2
#a function to remove the vowels in a word or sentence
def vowelsRemove(string):
    result = ""
    for letter in string:
        if letter in "eiuoaEIUOA":
            pass
        else:
            result = result + letter

    return result

print("")
print("Problem 2: vowelsRemove ")
print(vowelsRemove("Eagleton wrote the best introduction to any work concering the post-structuralist decay in academia "))
print("")

#problem 3
#
#

#problem 4
#a function that throws a dice n times and returns  a hisogram as a dictionary
from random import randrange

histogram = {} #dictionary

for i in range(100):# running for 1000 times or whatever you want, must edit this manually to get different rations/occurances of dice rolls
    dice = randrange(6) + 1
    if dice in histogram:
        histogram[dice] = histogram[dice] + 1
    else:
        histogram[dice] = 1
print("")
print("Problem 4: Dictionary/Histogram of dice rolls ")
print(histogram)

#problem 5

#problem 6
#a function that returns the longest string in a list of strings
def longestString(string):
    ltf = "" #longest THUS far
    for elem in string:
        if len(elem) > len(ltf):
            ltf = elem

    return ltf
print("")
print("Problem 6: longestString")
print( longestString( ["shakespeare", "dog", "auster", "the wasteland", "safran"]))
print("")


#problem 11
#ascending order
def sortAListOfString(stringList):
    def isListSorted(stringList):
        sorted = True
        for index in range(len (stringList) - 1 ):
            if stringList[index] < stringList[index + 1]:
                sorted = False
        return sorted
    while not isListSorted(stringList):
        print(">>>", stringList)
        for index in range(len(stringList) - 1):
            if stringList[index] < stringList[index + 1]:
                (stringList[index], stringList[index + 1]) = (stringList[index + 1], stringList[index])
a = ["fanon", "dryden", "antigone", "shakespeare", "oedipus", "hecuba"]
print("")
print("Problem 11: sortAListOfString")
sortAListOfString(a)
#print(sortAListOfString(["shakespeare", "oedipus", "antigone", "hecuba", "fanon", "dryden" ] ) )
print("")





#problem 12
#sum of two matrixes




print("")
print("Problem 12: sumOfMatrices")

print("")

#problem 13




#problem 14



#problem 15
#write a function to produce a list of 10 random integers 0<= 20 without duplicates
def noListDup():
    result = []
    for i in range(10):
        num = randrange(0, 21)
        while num in result:
            num = randrange(0, 21)
        result = result + [ num ]
    
    return result

print("")
print("Problem 15: noListDupe")
print(noListDup ( ) ) 
print(noListDup ( ) ) 
print ("")


#problem 16
#write a function to calculate the intersection of two sets represented as lists

def intersection(a, b):
    #pass
    answer = []
    
    for i in a:
        if i in b:
            answer += [i]

    return answer

print("")
print("Problem 16: listIntersection")
print( intersection ([], [] ) )
print( intersection ([5, 1, 2], [2, 3, 5] ) ) # intersection is [2] between these two lists
print("")