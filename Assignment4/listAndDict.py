def letterFrequency(strng):
    '''
    Given any string, return a dictionary containing the number of times 
    each character present in the string occurred
    For example, the string "Hi, Larry" would yield the 
    dictionary {"H" : 1, "i" : 1, " ": 1, "L" : 1, "a" : 1, "r" : 2, "y": 1} # this is the key and the objects have to be unique, but not the value
            ===================
            each item is seperated by a comma in a dictionary
            each key aka >>> H is assigned a value as indicated the colon, which in this is 1
            each key has to be unique but not necessarily the value
   
   
    (order of entries does not matter)
    '''
    freakOut = {} #this is my dictionary/intiliazes
    for i in strng: #iterates in each in the string
        if i in freakOut:# then this checks and sees if the letterw we are checking on is inside the dict or not
            freakOut[i] += 1 # += is shorthand for freakOut[i] = freakOut[i] + 1
        else: #it's more efficient to use an else statement here
            freakOut[i] = 1 #this creats the key in freakOut and sets its value to 1
    return freakOut




def primeList(n):
    '''
    Return a list containing the first n Prime numbers
    '''
   #pass

   