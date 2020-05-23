def minVal(theLst):
   #i used the count method here to port over my for loop code
   i = 0 
   MinVal = theLst[0]
   while i < len(theLst):
       if theLst[i] < MinVal:
           MinVal = theLst[i]
       i = i + 1 # this is the same as >>>> i += 1 
   return MinVal


def minValIndex(theLst):
   i = 0 
   MinVal = theLst[0]
   while i < len(theLst):
       if theLst[i] <= MinVal:
           MinVal = theLst[i]
           minValIndex = i
       i = i + 1  
   return minValIndex



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


def maxVal(theLst):
    i = 0 
    MaxVal = theLst[0]
    while i < len(theLst):
        if theLst[i] > MaxVal:
            MaxVal = theLst[i]
        i = i + 1  
    return MaxVal
    

def maxValIndex(theLst):
   maxValIndex = 0 #  I had to add this to get this code to work (even though the setup worked for minValIndex). BECAUSE It doesnt set the index if the first item is the maxium
   i = 0 
   MaxVal = theLst[0]
   while i < len(theLst):
       if theLst[i] >= MaxVal:
           MaxVal = theLst[i]
           maxValIndex = i 
       i = i + 1
   return maxValIndex
    
    

def maxValTuple(theLst):
    i = 0 
    MaxVal = theLst[0]
    while i < len(theLst):
        if theLst[i] >= MaxVal:
            MaxVal = theLst[i]
            maxValIndex = i
        i = i + 1
        tup2 = (MaxVal, maxValIndex)
        MaxValTuple = tup2 
    return MaxValTuple



def tripTotal(logs):
   i = 0
   time = 0
   while i < len(logs):
       var = logs[i] # for var in logs: >>>> in the for loop var is automatically var = log[i]
       time = time + (var[0] / var[1])
       i = i + 1 
   return time


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