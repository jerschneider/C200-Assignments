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
    
    
print( positionalSum([1, 2, 3, 4,], [4, 3, 2]) ) #[5, 5, 5]
    

# scalarMatrix: Number, Matrix -> Matrix 
#
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
    #use scalable 4 code for this
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

print( scalarMatrix(3, [[1, 2, -3], [5, 3, 4]]) ) # [[3, 6, -9], [15, 9, 12]]

def isSubString(sub, longStr):
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
    pass

def whereSubString(sub, longStr):
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
    pass