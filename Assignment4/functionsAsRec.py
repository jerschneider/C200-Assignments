"""
None of the functions are allow to use loops (for or while).

Not allowed to use any built-in string or list methods 
(.append, .remove, .find, .index, or anything else that would avoid recursion).

Not allowed to use built-in max or min. 
"""

#Notes for myself here --->this is from lecture8
"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        part1 = fib(n - 1)
        part2 = fib(n - 2)
        return part1 + part2
if __name__ == "__main__":
    for i in range(10):
        print("Fib of {0} (F_{0}) = {1}".format(i, fib(i)))
"""
#this is mr. German's suggested design recipe >>>
#A something is one of :
#a number or a string
#
# a [ListOf Something] is one of:
# --empty
# -- [Something ] + ListOFSomething
#myRemove : Something [ListOF Something] ->
# all occurances of the first arguement (if any) are removed


def myRemove(x, cont): #cont is probably going to be a container
    """
    Recursively remove every occurence of `x` in `cont` and return a list 
    that has all the contents of `cont` that are not `x`

    Not allowed to use list operation .remove()
    """
    #pass
    #structure recursion template
    if cont == []:
        return cont
    else:
        #x...cont[0]...myRemove(x, cont[1:])...
        #mr german decribes this is as a promise ---> promise: result is x[1:] with x removed
        if x == first(cont): # x[1:] is the same as rest(x)
            return myRemove(x, rest(cont))
        else:
            return [ first(cont) ] + myRemove(x, rest(cont)) 
#for myRemove to work AS IS I need the following functions:
def first(nelos):
    return nelos[0]
def rest(nelos):
    return nelos[1:]

#test code        
print( myRemove(3 , [3, 1, 2, 5, 3, 3, 6]) ) # Expected [1, 2, 5, 6] as the x is defined as 3 and the function recursively removes all the 3's



def myReplace(old, new, cont):
    """
    Recursively return a list of all contents of `cont` but any value that is 
    `old` is replaced with `new`
    """
    #pass
    if cont == []:
        return cont
    elif cont[0] == old:
        return [ new ] + myReplace(old, new, cont[1:] )
    else:
        return [ cont[0] ] + myReplace(old, new, cont[1:] )

#test code
print( myReplace(4, 5, [0, 9, 8, 7, 6, 5, 4, 3, 2, 1] ) ) #replaces 4 with 5 

def isPalindrome(string):
    """ 
    Recursively returns true if the string is a palindrome. 

    Not allowed to use list / string iteration i.e. myList[::-1]
    """
    #pass
"""
    cont = len(string)
    if ( cont == 0):
        return True
    if (string)
"""

"""
    
    if len(string) < 1: #this is the base-case
        return True
    else:
        if string[0] == string[-1]:
            return isPalindrome( string[1 : -1 ] )
        else:
            return False
"""    
    
    
    
    
    
"""  
    length = len(string)
    if string == []:
        return True 
    else:
        if string == first(string):
            return isPalindrome(string - string())
        else:
            if [ first(string) != string(length - string -1) ]:
                return False
"""
#print(isPalindrome( "aba" ) )  # madam  --- racecar
#print(isPalindrome( "cat" ) )
# to recursively do this
    # chop up the problem
    # first vs the last position
    #second to the second to the last

def removeString(cont):
    """
    Recursively returns the contents of list `cont`, not including any that are strings. 
    """
    #pass
    if cont == []:
        return cont
    else:
        if type(first(cont)) == str: 
            return removeString(rest(cont))
        else:
            return [ first(cont) ] + removeString(rest(cont)) 


#test code
print(removeString( ["boop", "boop", 3, 4, 4, 5, 4, 7, "beep", 9 ] ) )

    



def lengthOfString(string):
    """
    Recursively returns the length of the cont
    """
   #pass
#this through recursion finds the length of the container, and its objects within in a list
#im unsure wheather or not it should be coutning only the string characters because the name of the function suggests so
    if string == []:
        return 0
    return 1 + lengthOfString( string [1:] )

"""       
        type(first(string)) == str:
            return lengthOfString(len(first(string)))
        else:
            return [ first(string) ] + lengthOfString(rest(string))
"""

#test code
print(lengthOfString( ["beep", 2, 3, 4, 5, 6, 7]  ))


def removePos(x, cont):
    """
    Recursively removes an item from the list `cont` that is at `x`.
    Returns a list of all items from `cont` that are not were not at the `x` position

    Example: removePos(1, ['a', 'b', 'c']) --> ['a', 'c']
    """
    pass

def sum2Dlist(mat):
    """
    Recursively go through and sum all the values from each row and add the result of
    each row together to get a final value
    ex) 
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]] ---> 45
    Returns an integer
    """
    #pass
# A mat is one of the following:
# -Number 
# -[ListOf Mat]
# 
# Sum2DList : mat -> number
#
# purpose statement : inside the function in green
    if (type(mat) == int): # determiens if what is inside the mat contianer is a number (aka an integer)
            return mat
    elif mat == []:
        return 0
    else: #mat is a list
        return sum2Dlist(first(mat)) + sum2Dlist(rest(mat))
        
#testcode
print( sum2Dlist( 4 ) ) # 4
print( sum2Dlist( [ 1, 2, 3] ) ) # 6 >>> this function adds 1 + 2 + 3
print( sum2Dlist( [ [1], [2], [3] ] ) ) # 6 because even though these are individual lists it still adds them together the same as if they were integers within one list


def fibonnaci(n):
    """
    Complete this to return the fibonacci sequence

    Input: The n-th fibonnaci number to find

    Return: The value of the n-th fibonnaci number

    Extra Credit Opportunity: 
    - Add memoization. Refer to Monday's lecture 
    - Do not use the internet to figure it out.
    - It is extra credit, implementation is practice
    - Before the exam, understand the idea
    """
    pass