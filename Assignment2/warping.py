def warpFactor(afloat):#afloat is the number of times speed of light
    
    if afloat is 0:
        WarpFactor = 0

    if afloat > 0 and afloat < 10:
        WarpFactor = 1

    if afloat >= 10 and afloat < 39:
        WarpFactor = 2
    
    if afloat >= 39 and afloat < 102:
        WarpFactor = 3

    if afloat >= 102 and afloat < 214:
        WarpFactor = 4
    
    if afloat >= 214 and afloat < 392:
        WarpFactor = 5
    
    if afloat >= 392 and afloat < 656:
        WarpFactor = 6
    
    if afloat >= 656 and afloat < 1024:
        WarpFactor = 7
    
    if afloat >= 1024 and afloat < 1516:
        WarpFactor = 8
    
    if afloat >= 1516:
        WarpFactor = 9

    return WarpFactor

print ("Speed 1588 >>> " + str(warpFactor(1588)))
print ("Speed .867 >>> " + str(warpFactor(.867)))
print ("Speed 41.0 >>> " + str(warpFactor(41.0)))
print ("Speed 12.5 >>> " + str(warpFactor(12.5)))
