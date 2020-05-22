def palindrome(x):
    string = x 
    length = len(string)
    for var in range(length):
        if (string[var] != string[length - var -1]): #!= (does not equal) checks to see
            return False
    return True

#    if(x==x[::-1]):
#        x = True
#    else:
#        x = False
#   return x
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    for c in x:
#        print(c)
#    return True
   #answer = True
   #for i in range(len(x)):
       #print("-->", x[i])
       #if not (x[i] == x[(len(x)-1)-i]):
           #check character at i against the chracter i positions to the left of the last character
       #    premature optimization is the root of all evil
       #    what about negative indexing? -->says Mr. German
       # madam
       # 01234 4 == len("madam") - 1
       #         return False
    #return True

def getCount(char, strng):
    count = 0 #set up a counter which I used in looping
    for i in range(len(strng)): #but combined the previous functions setup to solve this. 
        if(strng[i] == char):
            count = count + 1
    return count

def getIndex(char, strng):
    """
    Gets the index of the character in the string

    Input: Character of length 1 and a string of any length

    Return: The first occurence of the character appearing in the string. 
    Return the length of the string if the character does not exist

    Limitation: Only functions we have been taught in class. Must use a loop. Cannot use "in" besides "for var in container"
    """
    #pass 
#go back and edit this
    for value in range(len(strng)):
        if char == strng[value]:
            return value
    return len(strng)

def areEqual(str1, str2):
    """
    Determines if 2 strings are equal

    Input: 2 strings of any length (Both can be different lengths)

    Return: Boolean

    Limitation:  Must use a single loop, and only 1 return statement in the code. Cannot use "in" besides "for var in container"
    """
   #This is leo's code from lab which was incorrect because it didnt loop 
   # pass
   # if str1 == str2
    #    return True
    #else:
     #   return False
    
    #This is the code from lab 
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    
    print("Palindrome")
    print("Actual: ", palindrome("aba"), " Expected: ",  True)
    print("Actual: ", palindrome("a"), " Expected: ",  True)
    print("Actual: ", palindrome("abba"), " Expected: ",  True)
    print("Actual: ", palindrome("amanaplanacanalpanama"), " Expected: ",  True)
    print("Actual: ", palindrome("abca"), " Expected: ",  False)
    print("Actual: ", palindrome("ac"), " Expected: ",  False)
    print("Actual: ", palindrome("adabbba"), " Expected: ",  False)
    print("Actual: ", palindrome("amandaplanacanalpanama"), " Expected: ",  False)

    print()
    print("Total Count")
    print("Actual: ", getCount("t", "Tomato"), "Expected: ", 1)
    print("Actual: ", getCount("a", "supercalifragilisticexpialidocious"), "Expected: ", 3)
    print("Actual: ", getCount(" ", "The tomato is not a vegatable but a fruit. Into the salad"), "Expected: ", 11)

    print()
    print("Get Index")
    print("Actual: ", getIndex("t", "Tomato"), "Expected: ", 4)
    print("Actual: ", getIndex("a", "supercalifragilisticexpialidocious"), "Expected: ", 6)
    print("Actual: ", getIndex(" ", "The tomato is not a vegatable but a fruit. Into the salad"), "Expected: ", 3)

    print()
    print("Are Equal")
    s1 = "Tomato"
    s2 = "Potato"
    s3 = "Jotato"
    s4 = "Lotato"
    print("Actual: ", areEqual(s4, s4), "Expected: ", True)
    print("Actual: ", areEqual(s1, s2), "Expected: ", False)
    print("Actual: ", areEqual(s3, s2), "Expected: ", False)
    print("Actual: ", areEqual(s1, s1), "Expected: ", True)
    #test code from lab
    print("Actual Tom Tomato Cruise: ", areEqual("Tom", "Tomato"), "Expected: ", False)