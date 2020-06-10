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

def numtoRom(num):
    number = [1, 4, 5, 6, 9, 10, 20, 40, 50, 90, 100]
    roman = ["I", "IV", "V", "VI", "IX", "X", "XX", "XL", "L", "XC", "C" ]

    i = 12
    while num:
        numIsDivded = num // number[i]
        num %= number[i]
        while numIsDivded:
            print(roman[i], end = "")
            numIsDivided -= 1
            i -= 1

##TestCode
#use :
#if __name__ == "__main__":
    #num = 19
    #print(num, " is converted to >>>", end = " " )
print(numtoRom(10))

