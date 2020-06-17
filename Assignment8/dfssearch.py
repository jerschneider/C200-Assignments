from os import listdir # TODO: Replace me with correct function
from os.path import join, isdir  # TODO: Replace me with correct function
import sys


def dfsFiles(wd):
    """
    Fill me in with algorithm provided

    TODO: Complete the function based off the pseudocode
    """
    #pass
    files = getDirs(wd)
    while len(files) != 0:
        x = files.pop(0)
        print(x)
        newList = getDirs(x)
        if newList != 0:
            for x in newList:
                files.insert(0, x)


def getDirs(wd):
    """
    Returns a list of directories to be traversed

    TODO: Fix the 2 different TODO s in this function
    """
    resultList = []
    for f in listdir(wd): # TODO: Find function from OS that will complete this function
        if isdir(join(wd, f)): # TODO: Find this function in the os.path directory 
            resultList.append(join(wd, f))
    return resultList




if __name__ == "__main__":
    #make this into a loop
    word = sys.argv[1]
    print("commandline argument: ", word)
    wd = input("working directory>>>") # TODO: Replace this we a SINGLE command line argument 
    dfsFiles(wd) 

## replace this with code that takes a command line input
## and runs dfsFiles with it
## LOOK UP SYNTAX FOR THIS
"""
wd = "/home/jeremy/Documents"
dfsFiles(wd)
"""