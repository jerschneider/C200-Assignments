from functionsAsRec.py import all


#you must write in farTest.py two different test cases for each function
# 

print(removeString( ["boop", "boop", 3, 4, 4, 5, 4, 7, "beep", 9 ] ) )



print( myRemove(3 , [3, 1, 2, 5, 3, 3, 6]) ) # Expected [1, 2, 5, 6] as the x is defined as 3 and the function recursively removes all the 3's

print( myReplace(4, 5, [0, 9, 8, 7, 6, 5, 4, 3, 2, 1] ) ) #replaces 4 with 5 

print(lengthOfString( ["beep", 2, 3, 4, 5, 6, 7]  ))



print(removePos( 1, [1, 2, 3, 4, 5, 6] ) )




print( sum2Dlist( 4 ) ) # 4
print( sum2Dlist( [ 1, 2, 3] ) ) # 6 >>> this function adds 1 + 2 + 3
print( sum2Dlist( [ [1], [2], [3] ] ) ) # 6 because even though these are individual lists it still adds them together the same as if they were integers within one list

print(fibonnaci( 13 ) ) # thus making n= 20 which should output 