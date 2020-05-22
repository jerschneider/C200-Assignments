#positionalSum: [ListOf Number] (ListOf Number] --> [ListOf Number]
#
def positionalSum(a, b):
    #found this is lecture6
   # myTable = [["A", "B", "C", "D"]
   # for r in myTable:
   #     for c in r:
   #         print(c end=" ")
   #     print()
    
  #  Given 2 lists, add the 2 lists together. The list will be as long as the shortest list. 

  #  Input: 2 lists of numbers

  #  Return: A new list of the size of the smaller list of the 2 lists added together positional.

#    Example:
 #   >>> positionalSum([1, 2, 3, 4], [4, 3, 2]) # [5, 5, 5]
  #  >>> positionalSum([1, 2, 3, 4], [1, 1, 1, 4]) # [2, 3, 4, 8]
#pass
   answer = []
   if len(a) < len(b):
        theLength = len(a)
   else:
        theLength = len(b)
   for index in range(theLength):
        answer = answer + [ a[index] + b[index] ]
   return answer

print("")
print("positionalSum Test")
print("Actual: ", positionalSum([1, 2, 3, 4,], [4, 3, 2]), "Expected:  [5, 5, 5]")    
print("Actual: ", positionalSum([1, 1, 6, 7,], [9, 4, 9]), "Expected:  [10, 5, 15]")    
print("")



# scalarMatrix: Number, Matrix -> Matrix 
def scalarMatrix(n, m):
    """
    Given a matrix, size a x b, multiply each position by n. 

    Input: an number to multiply each item in the matrix (list of list)

    Return: A new list of lists that multiplies all values by n

    Limitation: No using numpy

    Examples: n = 3

    [[4, 4, 4]
     [1, 2, 4]
     [10, -1, 2]]

     Result:

     [[12, 12, 12]
      [3, 6, 12]
      [30, -3, 6]]

    """
  #  pass
    #print(n, m)
    #
    #
    #use scalable 4 code from lab for this
    result = []
    for row in m:
        newRow = []
        for elem in row:
            newRow = newRow + [ elem * n ]
            #print ("adding: ", newRow)
        #print ("done: ", newRow)
        result = result + [ newRow ]
       # print ("adding to matrix: ", result)
   # print ("done with matrix: ", result)
    return result

print("")
print("scalarMatrix Test")
print("Actual: ", scalarMatrix(3, [[1, 2, -3], [5, 3, 4]]), "Expected:  [[3, 6, -9], [15, 9, 12]]")
print("Actual: ", scalarMatrix(4, [[1, 2, -3], [5, 3, 4]]), "Expected:  [[4, 8, -12], [20, 12, 16]]")
print ("")
#([1, 1, 6, 7,], [9, 4, 9]), "Expected:  [10, 5, 15]")    


def isSubString(sub, longStr):
    if sub:
        sub_len = len(sub)
        for var in range(len(longStr)):
            if longStr[var:var + sub_len] == sub:
                return True
    return False

print("")
print("isSubString Test")
print("Actual: ", isSubString("here", "there"), "Expected: ", True)
print("Actual: ", isSubString("boop", "zoopity"), "Expected: ", False)
print("Actual: ", isSubString("hare", "whatever"), "Expected: ", False)
print("Actual: ", isSubString("ate", "whatever"), "Expected: ", True)
print("") 
   
"""
    Determine if a string exists in another string. 

    Not allowed to check for direct membership. You need to use looping

    Input: 2 strings

    Returns: Boolean if there is substring.

    Limitation: No "in" membership

    Example:

    >>> isSubString("cat", "Concatenate")  # True
    >>> isSubString("orange", "Concatenate")  # False
    >>> isSubString("acsd", "car")  # False
    """

def whereSubString(sub, longStr):
    for var in range(len(longStr) - len(sub) + 1): 
        if longStr[var:var + len(sub)] == sub:
            return var
    return -1 



print("")
print("whereSubString Test")
print("Actual: ", whereSubString("shake", "shakespeare"), "Expected : 0") #0 position example
print("Actual: ", whereSubString("boop", "bippityboppity"), "Expected : -1") #this is an example of the -1 return working
print("Actual: ", whereSubString("cat", "Concatenateare"), "Expected : 3")
print("Actual: ", whereSubString("cat", "shakespeareConcatenateare"), "Expected : 14") #lol :)
print("")
    
"""
    Determine last position of the start of a substring occurs. 

    Not allowed to check for direct membership. You need to use looping

    Input: 2 strings

    Returns: Integer showing where the substring starts in the longStr. Return -1 if 
    the substring doesn't exist

    Limitation: No "in" membership

    Example:

    >>> whereSubString("cat", "Concatenate")  # 3
    >>> whereSubString("orange", "Concatenate")  # -1
    >>> whereSubString("acsd", "car")  # -1
"""