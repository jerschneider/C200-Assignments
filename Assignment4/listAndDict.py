# REMEMBER TO ADD TEST CODE TO THESE
#===============================
def letterFrequency(strng):
    '''
    Given any string, return a dictionary containing the number of times 
    each character present in the string occurred
    For example, the string "Hi, Larry" would yield the 
    dictionary {"H" : 1, "i" : 1, " ": 1, "L" : 1, "a" : 1, "r" : 2, "y": 1} # this is the key and the objects have to be unique, but not the value
    '''
#===========================================================================
#            each item is seperated by a comma in a dictionary
#            each key aka >>> H is assigned a value as indicated the colon, which in this is 1
#            each key has to be unique but not necessarily the value
#   
#   
#(order of entries does not matter)
    
    freakOut = {} #this is my dictionary/intiliazes
    for i in strng: #iterates in each in the string
        if i in freakOut:# then this checks and sees if the letterw we are checking on is inside the dict or not
            freakOut[i] += 1 # += is shorthand for freakOut[i] = freakOut[i] + 1
        else: #it's more efficient to use an else statement here
            freakOut[i] = 1 #this creats the key in freakOut and sets its value to 1
    return freakOut



def primeList(n):
    pList = []
    for i in range(2,10000000): #I set range  2, 10000000 BECAUSE this loop will iterate between these two variables, I could probably do this another way but this works
        for j in range(2, i): #this nested for loop iterates through every number between (2 and i)
            if (i % j == 0): #this checks if i % j is equals to 0 AND if runs into any instance where it does the condition breaks
                break #exits you out of the current loop
        else: #Otherwise >>> this then appends it to the list
            pList.append(i)
        if len(pList) == n: #we are then making sure our list has the desired amount of prime numbers which is dictated by the inputs in the n varibale of the function
            return pList
    
    
#==================================================================================    
"""  
    for i in range(2, n + 1): #we're telling python to count from 2 to n+1
# prime number % itself is always going to be 0, and the same with 1
        if (i % (i + 1)) != 0:
            #if (i % 1) == i:
            primeList.append(i) #I decided to use append because we learned it today, what the function does is add varible(i) to the primeList
    return primeList
"""       
        



