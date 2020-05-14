def canBePresident (isCitizen, age, residentTime):
    c1 = isCitizen == True # determines if person is citizen
    c2 = age >= 35 
    c3 = residentTime >= 14#resident time is the time in the US
    #return c1 and c2 and c3
    return c1 and c2 and c3
    #if (c1 and c2 and c3) == ture:
    #   return (c1 and c2 and c3)
    #else:
    #   return (c1 and c2 and c3)
    