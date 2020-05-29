def myRemoveList(x, lst):
    """
    Remove first occurence of `x` in `lst` and return a list 
    that has the first instance of `x` removed from `cont`

    Will only use elements that are in the list

    The work will be done in the inner function

    Not allowed to use a loop.
    """
    def handlesValueIssue(copyOfList):
        # NOTE: x exists in this function because of scope
        # SO does lst, but DO NOT use lst here
        # `copyOfList` is a copy
        #pass # TODO: Complete here
        copyOfList.remove(x)
        return copyOfList

#    if x in lst:
#        return handlesValueIssues(x)
#    else:
#        return lst

    
    # Do not modify this line
    return handlesValueIssue(lst.copy())






def myRemoveString(x, string):
    """
    Remove every occurence of `x` in `string` and return a string 
    that has all the contents of `string` that are not `x`

    Not allowed to use a loop.
    """
    #pass
    sString = ""
    nString = string.replace(x, sString)
    return nString
    
"""    
    newString = string.replace("x", "")
    return newString
"""



def myInsertList(new, place, cont):
    """
    Return a list with the new item added at index `place`.

    This work will de done in the inner function
    """
    def handlesValueIssue(copyOfList):
        # NOTE: new and place exists in this function because 
        # of scope
        # SO does cont, but DO NOT use cont here
        # `copyOfList` is a copy
        #pass # TODO: Complete here
        copyOfList.insert(new, place)
        return copyOfList

    
    # Do not modify this line
    return handlesValueIssue(cont.copy())

"""
 place = [0]
        copyOfList = [place]
        
        nList = copyOfList.replace(new, place)
        return nList
nList = copyOfList[]
       nList[place] = new
       return nList
"""





def myReplaceString(old, new, cont):
    """
    Return a list of all contents of `cont` but any value that is 
    `old` is replaced with `new`

    Specifically for a string
    """
    #pass
    rString = cont.replace(old, new)
    return rString
   

"""
 sString = ""
    nString = string.replace(x, sString)
    return nString
 nConts = []
    nCont = cont.replace(old, new)
    return nCont
"""



def removePosList(x, cont):
    """
    Removes an item from the list `cont` that is at `x`.
    Returns a list of all items from `cont` that are not were not at the `x` position

    This work should be done in the inner function

    Example: removePosList(1, ['a', 'b', 'c']) --> ['a', 'c']
    """
    def handlesValueIssue(copyOfList):
        # NOTE: x exists in this function because of scope
        # SO does lst, but DO NOT use lst here
        # `copyOfList` is a copy
        #pass # TODO: Complete here
        copyOfList.pop(x)
        return copyOfList
        
         
    # Do not modify this line
    return handlesValueIssue(cont.copy())




def minList(lst):
    """
    Find the minimum value in the list
    """
    #pass
    return min(lst)

def maxList(lst):
    """
    Find the maximum value in the list
    """
    #pass
    return max(lst)

def minIndex(lst):
    """
    Find the index of the minimum value (first occurence of minimum)

    Can be done in one line but you can split it apart
    """
    #pass
    return lst.index(min(lst))


def maxIndex(lst):
    """
    Find the index of the minimum value (first occurence of maximum)

    Can be done in one line but you can split it apart
    """
    #pass
    return lst.index(max(lst))


def getIndex(char, strng):
    """
    Gets the index of the character in the string

    Assume the character is in the string. 

    We will not test on any char that does not exist
    """
    #pass
    return strng.index(char)




def areEqual(str1, str2):
    """
    Determines if 2 strings are equal

    Input: 2 strings of any length (Both can be different lengths)

    Return: Boolean

    """
    #pass
    if str1 == str2:
        return True
    else:
        return False

def main():
    """
    # TODO: Add tests to the function in the appropriate places
    """
    ex1 = []
    ex2 = []
    ex3 = []
    ex4 = []
    ex5 = []

    st1 = ""
    st1 = ""
    st1 = ""
    st1 = ""
    st1 = "" 

    print("TODO: Here is where tests will be written")
    print("Test output for function: myRemoveList")
    # TODO
    print(myRemoveList(3, [1, 2, 3,] ) )
    #print(myRemoveList(6, []))
    #print(myRemoveList(1, [1, 2, 3]))
    print(myRemoveList(6, [6, 6, 6] ))
    
    print("Test output for function: myRemoveString")
    # TODO
    print("")
    print("myRemoveString")
    print(myRemoveString ( "p", "boop" )  )
    print("")
    print("Test output for function: myInsertList")
    # TODO
    print("")
    print ("myInsertList")
    print(myInsertList (4, 2, [1, 2, 3, 4, 5, 6, 7]))
    print("Test output for function: myReplaceString")
    # TODO
    print(myReplaceString( "p", "o", "beep" ) )

    print("Test output for function: removePosList")
    # TODO
    print("")
    print(removePosList(1, ['m', 'b', 'c', 'd'] ) )
    print("")
    print("Test output for function: minList")
    # TODO
    print(minList( [1, 3, 4, 5, 6, 7, 8, 8, 9]))

    print("Test output for function: maxList")
    # TODO
    print(maxList ([1, 2, 3, 4, 5, 66, 7]))

    print("Test output for function: minIndex")
    # TODO
    print( minIndex ([1, 2, 3, 4, 55, 6, 7, 0] ) )

    print("Test output for function: maxIndex")
    # TODO
    print( maxIndex ( [1, 2, 3, 4, 5, 6, 7, 8 ]))

    print("Test output for function: getIndex")
    # TODO
    print(getIndex ('b', 'oob' ))

    print("Test output for function: areEqual")
    #TODO
    print( areEqual ("cat", "cat"))
    print( areEqual ("cat", "bat"))




if __name__ == "__main__":
    main()


    
    