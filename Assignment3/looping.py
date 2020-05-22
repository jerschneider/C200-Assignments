def minVal(theLst):
    MinVal = theLst[0] #this references the (0) position of a container and then goes forward from there
    for var in theLst:
        if var < MinVal: 
            MinVal = var #I redefine the variable(MinVal, so its now the least value in terms of a integer 
    return MinVal
#a list is a series of integers, and are ranked by their position
 #["red", "red", "blue", "x", 2, "boop"]
  #  0       1       2   3   4       5


def minValIndex(theLst):
    MinVal = theLst[0] 
    for var in theLst:
        if var < MinVal: 
            MinVal = var
    MinValIndex = theLst.index(MinVal) #I used the same code from the previous problem but added the index function to the minVal holder
    return MinValIndex


def minValTuple(theLst):
    MinVal = theLst[0] 
    for var in theLst:
        if var < MinVal: 
            MinVal = var
    MinValIndex = theLst.index(MinVal) 
    tup1 = (MinVal, MinValIndex)
    MinValTuple = tup1
    return MinValTuple
   

def maxVal(theLst):
    MaxVal = theLst[0]
    for var in theLst:
        if var > MaxVal: #this states that if a variable is less than the MinVal then the MinVal is var
            MaxVal = var
    return MaxVal

def maxValIndex(theLst):
    MaxVal = theLst[0]
    for var in theLst:
        if var > MaxVal: 
            MaxVal = var
    MaxValIndex = theLst.index(MaxVal)
    return MaxValIndex
    

def maxValTuple(theLst):
    MaxVal = theLst[0] 
    for var in theLst:
        if var > MaxVal: 
            MaxVal = var
    MaxValIndex = theLst.index(MaxVal) 
    tup1 = (MaxVal, MaxValIndex)
    MaxValTuple = tup1
    return MaxValTuple
   
def tripTotal(logs):
    time = 0
    for var in logs:
        time = time + (var[0] / var[1]) # i use time a second 'time' here, instead of totalTime because 'time = ' is needed because of how the program counts as it goes through the list
        totalTime = time #infact this line is completey uneeded (do not do this)
    return totalTime
#This probelm was a learning experience for me and I truly learned how for loops work
# In fact below is what I tried to do at first (and a few other failed attempts)
# THE BIGGEST TAKEAWAY FROM THIS PROBLEM IS THAT VAR IS EACH INDIVIDUAL ITEM IN A List given to a 'FOR LOOP' (but it could also be anything)
# 
# 
#  if var0 = logs.index[0]:
#            list0 = var0
#            list0Time = (var0.index(0) / var0.index(1))
#       if var1 = logs.index[1]:
#            list1 = var1
#            list1Time = (var1.index(0) / var1.index(1))
#        if var2 = logs.index[2]:
#            list2 = var2
#            list2Time = (var2.index(0) / var2.index(1))
#        trip = list0Time + list1Time + list2Time
#        TripTotal = trip
#        return TripTotal







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