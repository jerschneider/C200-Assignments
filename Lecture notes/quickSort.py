def qs(aList, start, end):
    if start >= end:
        return aList
    pivotValue = partition(aList, start, end)
    qs(aList, start, pivotValue)
    qs(aList, pivotValue + 1, end)

def partition(A, start, end):
    left = start
    right = end
    pivot = A[start]
    while left < right:
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1
        if left < right:
            # Swapping
            A[left], A[right] = A[right], A[left]
    return right

def visualQS(aList, start, end, indentLevel):
    print(":   " * indentLevel +"|-----------NewCall-----------\n" + ":   " * indentLevel + "|")
    print(":   " * indentLevel + "|Current List: {}  Starting: {}   End: {}".format(aList, start, end))
    if start >= end:
        print(":   " * indentLevel +"|Start ({}) >= End ({})".format(start, end))
        print(":   " * indentLevel +"|-----------EndCall-----------\n" + ":   " * indentLevel + "|")
        return aList
    pivotIndex = partition(aList, start, end)
    print(":   " * indentLevel +"|Moving list after partition: {}".format(aList))
    print(":   " * indentLevel +"|Less than: {}".format(aList[start:pivotIndex]))
    visualQS(aList, start, pivotIndex, indentLevel + 1)
    print(":   " * indentLevel +"|Greater than: {}".format(aList[pivotIndex+1:end]))
    visualQS(aList, pivotIndex + 1, end, indentLevel + 1)
    print(":   " * indentLevel +"|-----------EndCall-----------\n" + ":   " * indentLevel + "|")



if __name__ == "__main__":
    # theList = [10, 8, -2,  6, 11, 4]
    # qs(theList, 0, len(theList) -1 )
    # print(theList)

    newList= [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(newList)
    print()
    visualQS(newList, 0, len(newList) - 1, 0)
    print(newList)

