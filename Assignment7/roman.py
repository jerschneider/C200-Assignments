#create a function that takes a number and converts it to a roman numeral
# hint: task is made easier if you use modulo and integer divsion

# 1 >>> I
# 4 >>> IV
# 5 >>> V
# 10 >>> X
# 20 >>> XX
# 30 >>> XXX
# 40 >>> XL
# 50 >>>  L
# 60 >>> LX
# 90 >>> XC
# 100 >>> C

def numtoRom(number):
    digits = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD' ], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

    result = ""
    while number:
            tup = digits[0]
            #print("tup", tup)
            quotient = number // tup[0] 
            number %= tup[0]
            #print("number", number)
            while quotient: 
                result += tup[1] 
                quotient -= 1
            
            digits.pop(0)
            #print(digits[0])
    return result
	
if __name__ == "__main__": 
	number = 349
	print("Roman numeral is:" + numtoRom(number))
 
 

    
##TestCode
#use :
"""
if __name__ == "__main__":
    num = 2
    print(" is converted to >>>", end = " " )
"""
print(numtoRom(1))
print(numtoRom(5))
print(numtoRom(10))



