from functionsAsRec import *


#you must write in farTest.py two different test cases for each function
# 
print("")
print("removeString")
print("Actual>>>>", removeString( ["boop", "boop", 3, 4, 4, 5, 4, 7, "beep", 9 ] ), "Expected >>> [3, 4, 4, 5, 4, 7, 9]" )
print("Actual>>>>", removeString( [1, 2, 3, 4, 5, 6, 7, "zoopity", "orange" ]), "Excpected >>> [1, 2, 3, 4, 5, 6, 7]" )
print("")

print("")
print("isPalindrome")
print("aba >>>", isPalindrome(" aba " ) )
print("loop >>>", isPalindrome(" loop " ) )
print("")

print("")
print("myRemove")
print("Actual >>>", myRemove(3 , [3, 1, 2, 5, 3, 3, 6]), "Expected >>> [1, 2, 5, 6]" ) # Expected [1, 2, 5, 6] as the x is defined as 3 and the function recursively removes all the 3's
print("Actual >>>", myRemove(2 , [3, 1, 2, 2, 1, 4, 2]), "Expected >>> [3, 1, 1, 4]"  )
print("")

print("")
print("myReplace")
print("Actual >>> ", myReplace(4, 5, [0, 9, 8, 7, 6, 5, 4, 3, 2, 1] ), "Excpected >>> [0, 9, 8, 7, 6, 5, 5, 3, 2, 1] " )
print("Actual >>> ", myReplace(1, 7, [1, 2, 3, 5, 7, 8, 9, 4, 1, 1, 1, 7, 7, 7, 7] ), "Excpted >>> [7, 2, 3, 5, 7, 8, 9, 4, 7, 7, 7, 7, 7, 7, 7]" )
print("")

print("")
print("lengthOfString")
print("Actual >>> ", (lengthOfString( ["beep", 2, 3, 4, 5, 6, 7] ), "Expected >>>  7"   ))
print("Actual >>> ", (lengthOfString( ["beep", 2, 3, 4, 5, 6, 7] ), "Expected >>>  7"   ))
print("")

print("")
print("removePos")
print("Actual >>> remove 1 ", (removePos( 1, [1, 2, 3, 4, 5, 6] ), "Expected >>> [2, 3, 4, 5, 6]  "   ))
print("Actual >>> remove 4 ", (removePos( 4, [1, 2, 3, 4, 5, 6] ), "Expected >>> [1, 2, 3, 5, 6] " ))
print("")

print("")
print("sum2Dlist")
print("Actual >>> ",  (sum2Dlist( 4 ) ), "Expected >>> 4") # 4
print("Actual >>> ", sum2Dlist( [ 1, 2, 3] ), "Expected >>> 6"  ) # 6 >>> this function adds 1 + 2 + 3
print("Actual >>> ", sum2Dlist( [ [1], [2], [3] ] ), "Expected >>> 6" ) # 6 because even though these are individual lists it still adds them together the same as if they were integers within one list
print("")

print("")
print("fibonnaci")
print("Actual >>> ", fibonnaci( 13 ), "Expected >>> 144" ) # thus making n= 20 which should output 
print("Actual >>> ", fibonnaci( 14 ), "Expected >>> 233" )
print("")