def letterInString(string, letter):
    """
    Given a string. Find the position of the letter

    If the letter is not in the string, return -1.
    """

    position = -1
    for i in range(len(string)):
        currentLetter = string[i]
        if currentLetter == letter:
            position = i
        #return position # do not put a [DO NOT PUT A RETURN STATEMENT IN A LOOP]
    return position

print(letterInString("The brown Cat", "a"))
print(letterInString("The brown Cat", "c"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def countTheEvens(aList):
    """
    Counts the number of even numbers in a list
    """
    count = 0
    for number in aList:
        if number % 2 == 0: # (number % 2) ---> odd
            count = count + 1 #count += 1

    return count

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def CountTheEvens(aList):
    """
    Counts the number of even numbers in a list
    """

    tomato = 0 #assigning tomato here so I can use it later in the loop
    for number in aList:
        if number % 2 == 0: # (number % 2) ---> odd
            tomato = tomato + 1 # tomato += 1

    return tomato
print(countTheEvens([1, 20, 5, 8, 12, 16, 11, 20]))