# create the functions in myRec
#use a loop and print out the first 10 values
#the test code must be writeen in the recTest.py
def function1(n):
    n = n
    for i in range (1, n) :
        return (n - 1 + n)
        n = n - 1
    return 0


def closedFunct1(n):
    n = n
    for i in range (1, n) :
        return (n * (1 + n)) / 2
        n = n - 1
    return 0


def funct2(n):
    n = n
    for i in range (1, n) :
        return ( (n - 1) + 0.02 * (n - 1))
        n = n - 1


def closedFunc2(n):
    
    n = n
    for i in range (1, n) :
        return (1.02)**n * 10000
        n = n - 1
    return 10000


def func3(n):
    if n == 2:
        return 3
    n = n
    for i in range (1, n) :
        if n >= 3:
            return (n - 1) + (n -2)
        n = n - 1
    return 2


def func4(n):
    if n == 1:
        return 9
    n = n
    for i in range (1, n) :
        return 9 * (n - 1) + (10 ** (n - 1)) - (n - 1)
        n = n - 1


def func5(n):
    if n == 0:
        return 1
    n = n
    for i in range (1, n) :
        return 3 * (n - 1) + 1
        n = n - 1
    return 3


def closedFunc5(n):
    if n == 0:
        return 1
    n = n
    for i in range (1, n) :
        return ((3 ** (n+1)) -1) / 2
        n = n - 1
    return 2




