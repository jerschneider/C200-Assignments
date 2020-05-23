def palindrome(x):
    i = 0
    string = x 
    length = len(string)
    while i < length:
        if (string[i] != string[length - i -1]):
            string = i
            return False
        i = i + 1 
    return True
    
    
    
    """
    For a given string, determine if the string is a palindrome. (The same forward and back)

    Input: String of any size (including empty)

    Return: Boolean (True if palindrome, False otherwise)

    Limitation: You must use a loop. Only functions allowed to be used is len or range (if needed). Cannot use "in" besides "for var in container"
    """
    #pass


def getCount(char, strng):
    i = 0
    count = 0
    while i < len(strng): # deleted the range which I had with the forloop variant
        if (strng[i] == char):
            count = count + 1
        i = i + 1
    return count
    
    """
    Get the number of times a character appears in a string.

    Input: A character (length 1) and a string of any length

    Return: Number of times a character appears

    Limitation: Only functions we have been taught in class. Must use a loop. Cannot use "in" besides "for var in container"
    """
   # pass

def getIndex(char, strng):
    i = 0
    index = 0
    while i < len(strng):
        if char == strng[i]:
            index = i
            return index
        i = i + 1
    return len(strng)
    
    """
    Gets the index of the character in the string

    Input: Character of length 1 and a string of any length

    Return: The first occurence of the character appearing in the string. 
    Return the length of the string if the character does not exist

    Limitation: Only functions we have been taught in class. Must use a loop. Cannot use "in" besides "for var in container"
    """
   # pass 

def areEqual(str1, str2):
    i = 0
    count = 0
    if len(str1) != len(str2):
        return False
    while i < len(str1):
        if str1[i] == str2[i]:
            count = i  
            pass
        else:
            return False
        i = i + 1 #had to move this after the else statement
    return True

   
    """
    Determines if 2 strings are equal

    Input: 2 strings of any length (Both can be different lengths)

    Return: Boolean

    Limitation:  Must use a single loop, and only 1 return statement in the code. Cannot use "in" besides "for var in container"
    """
    #pass


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