def aSort(listToSort):
    lengthOfList = len(listToSort)
    #minVal = listToSort[0]
    for i in range(lengthOfList-1): #for i <- 0 to n - 2 do #### the Range of the length(-1) purpose here is to mark the minVal
        for j in range(0, lengthOfList-i-1): #nested loop
            if listToSort[j] > listToSort[j + 1]: # sees if the element in the n* + 1 position is less than the element in the nth position ##since this is descending we need to do greater than
                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j] #swaps j if condition is met
    return listToSort 

"""
def minVal(theLst):
    MinVal = theLst[0] #this references the (0) position of a container and then goes forward from there
    for var in theLst:
        if var < MinVal: 
            MinVal = var #I redefine the variable(MinVal, so its now the least value in terms of a integer 
    return MinVal


 if i < minVal:
            minVal = i
    return minVal    
"""

"""
if cont == []:
        return cont
    elif cont[0] == old:
        return [ new ] + myReplace(old, new, cont[1:] )
    else:
        return [ cont[0] ] + myReplace(old, new, cont[1:] )
"""



print( "Actual >>> ", aSort( [4, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 9, 0, 10, 12, 13, 14, 11] ), "Expected >>> [0, 1, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14] "  )