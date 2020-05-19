#this is a fairly clunky ---> 15size makes it a full X
size = int(input("What size for the X: "))
for line in range(size):
    row = ""
    for column in range(size): #print "****"
        if line == column or line+column == size-1: #line == 0 or column == size-1 or line == size-1 or column == 0:
            row = row + "* " 
        else: 
            row = row + " " # row = row + "(" + str(line) + ", " + str(column) + ")"
    print(row)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Scaleable E, clunkiness is similar to the X
size = int(input("What size for the E: "))
for line in range(size):
    row = ""
    for column in range(size):
        if line == 0 or column == 0 or line == size-1 or line == size//2 and column < size//2:
            row = row + "* " 
        else:  
            row = row + " "
    print(row)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Scalable 4
size = int(input("What size for the FOUR: "))
for line in range(size):
    row = ""
    for column in range(size):
        if line + column == size//2 or (line == size//2 and column < 2*size//3) or (column == size//2):
            row = row + "* " 
        else:  
            row = row + " "
    print(row)