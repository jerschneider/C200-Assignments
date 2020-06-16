from os import None # TODO: Replace me with correct function
from os.path import join, None # TODO: Replace me with correct function



def dfsFiles(wd):
    """
    Fill me in with algorithm provided

    TODO: Complete the function based off the pseudocode
    """
    pass

def getDirs(wd):
    """
    Returns a list of directories to be traversed

    TODO: Fix the 2 different TODO s in this function
    """
    resultList = []
    for f in TODO(wd): # TODO: Find function from OS that will complete this function
        if TODO(join(wd, f)): # TODO: Find this function in the os.path directory 
            resultList.append(join(wd, f))
    return resultList


if __name__ == "__main__":
    wd = input("working directory>>>") # TODO: Replace this we a SINGLE command line argument 
    dfsFiles(wd) 
