#this is a fairly clunky ---> 15size makes it a full X
size = int(input("What size: "))
for line in range(size):
    row = ""
    for column in range(size): #print "****"
        if line == column or line+column == size-1: #line == 0 or column == size-1 or line == size-1 or column == 0:
            row = row + "* " 
        else: 
            row = row + " " # row = row + "(" + str(line) + ", " + str(column) + ")"
    print(row)

