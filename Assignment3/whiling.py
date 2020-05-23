def minVal(theLst):
   #i used the count method here to port over my for loop code
   i = 0 
   MinVal = theLst[0]
   while i < len(theLst):
       if theLst[i] < MinVal:
           MinVal = theLst[i]
       i = i + 1 # this is the same as >>>> i += 1 
   return MinVal

#def minVal(theLst):
#    MinVal = theLst[0] #this references the (0) position of a container and then goes forward from there
#    for var in theLst:
#        if var < MinVal: 
#            MinVal = var #I redefine the variable(MinVal, so its now the least value in terms of a integer 
#    return MinVal


#    for var in theLst:
#        if var < MinVal: 
#            MinVal = var
#    return MinVal
"""
    Given a list, determine the minimum value in the list

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Value of minimum value

    Limitation: The only function you can use (if you want to) is `len()` and `range()`. Cannot use "in" besides "for var in container"
"""
   # pass

def minValIndex(theLst):
   i = 0 
   MinVal = theLst[0]
   while i < len(theLst):
       if theLst[i] < MinVal:
           MinVal = theLst[i]
           minValIndex = i
       i = i + 1  
   return minValIndex


"""
def minValIndex(theLst):
    Index = 0
    MinVal = theLst[0] #starting point is at position 0 for the forloop
    for var in theLst:
        if var <= MinVal: # <= this is used to help with my counting of the indexes
            MinVal = var
            MinValIndex = Index #this records the current index
        Index = Index + 1 #as the forloop loops then this will go up (or counts)
    return MinValIndex


def minVal(theLst):
   #i used the count method here to port over my for loop code
   i = 0 
   MinVal = theLst[0]
   while i < len(theLst):
       if theLst[i] < MinVal:
           MinVal = theLst[i]
       i = i + 1 # this is the same as >>>> i += 1 
   return MinVal
"""




"""
    Given a list, determine the index of the minimum value (the last occurence)

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Index of the smallest value (the last occurence)

    Limitation: The only function you can use (if you want to) is `len()` and `range()`. Cannot use "in" besides "for var in container"
"""
    #pass

def minValTuple(theLst):
    i = 0 
    minVal = theLst[0]
    while i < len(theLst):
        if theLst[i] <= minVal:
            minVal = theLst[i]
            minValIndex = i
        i = i + 1
        tup1 = (minVal, minValIndex)
        MinValTuple = tup1 
    return MinValTuple

    
    
    """
    Given a list, determine the minimum value and index in the list

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Tuple, first item is the smallest value, second item is the index of the value (the last occurence)

    Limitation: The only function you can use (if you want to) is `len()` and `range()`. Cannot use "in" besides "for var in container"
    """
   # pass

def maxVal(theLst):
    i = 0 
    MaxVal = theLst[0]
    while i < len(theLst):
        if theLst[i] > MaxVal:
            MaxVal = theLst[i]
        i = i + 1  
    return MaxVal
    
    
    """
    Given a list, determine the maximum value in the list

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Value of maximum value

    Limitation: The only function you can use (if you want to) is `len()` and `range()`. Cannot use "in" besides "for var in container"
    """
   # pass

def maxValIndex(theLst):
    i = 0 
    MaxVal = theLst[0]
    while i < len(theLst):
        if theLst[i] > MaxVal:
            MaxVal = theLst[i]
            maxValIndex = i
        i = i + 1
    return maxValIndex
    
    
    
    
    
"""
    Given a list, determine the index of the maximum value (the last occurence)

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Index of the largest value (the last occurence)

    Limitation: The only function you can use (if you want to) is `len()` and `range()`. Cannot use "in" besides "for var in container"
"""
   # pass

def maxValTuple(theLst):
    """
    Given a list, determine the maximum value and index in the list (the last occurence)

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Tuple, first item is the largest value, second item is the index of the value (the last occurence)

    Limitation: The only function you can use (if you want to) is `len()` and `range()`. Cannot use "in" besides "for var in container"
    """
    pass

def tripTotal(logs):
    """
    Given a list containing sublists of size 2, each sublist 
    [number of miles traveled, speed traveled at that distance]. 
    You will find the total time of the trip

    Input: List of lists, containing at least 1 item.
    [[m1, s1], [m2, s2], [m3, s3], ...]

    Return: The total time the trip took.

    Required to use a single for loop
    """
    pass


if __name__ == "__main__":
    print("Testing Cases")
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lst2 = [15, 12, 10, 95, 101]
    lst3 = [5, 4, 3, 2]
    print("Min Val of LST1: ", minVal(lst1))
    print("Min Index of LST1: ", minValIndex(lst1))
    print("Min Val and Index of LST1: ", minValTuple(lst1))
    print("Max Val of LST1: ", maxVal(lst1))
    print("Max Index of LST1: ", maxValIndex(lst1))
    print("Max Val and Index of LST1: ", maxValTuple(lst1))
    print()
    print("Min Val of LST2: ", minVal(lst2))
    print("Min Index of LST2: ", minValIndex(lst2))
    print("Min Val and Index of LST2: ", minValTuple(lst2))
    print("Max Val of LST2: ", maxVal(lst2))
    print("Max Index of LST2: ", maxValIndex(lst2))
    print("Max Val and Index of LST2: ", maxValTuple(lst2))
    print()
    print("Min Val of LST3: ", minVal(lst3))
    print("Min Index of LST3: ", minValIndex(lst3))
    print("Min Val and Index of LST3: ", minValTuple(lst3))
    print("Max Val of LST3: ", maxVal(lst3))
    print("Max Index of LST3: ", maxValIndex(lst3))
    print("Max Val and Index of LST3: ", maxValTuple(lst3))
    print()
    testingLog = [[100, 50], [10, 10], [60, 60]]
    print("Testing the tripTotal function: ", tripTotal(testingLog))