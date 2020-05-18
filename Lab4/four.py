size = input("What's the size: ")
for i in range(int(size)): #i counts the lines (horizontal rows)
    row = ""
    for j in range(int(size)): # j counts the column (in a row)
        if j == 0 or i == j or j == int(size)-1: 
            row = row + "* "
        else:
            row = row + "  "

    print(row)
    #print(str(i) + ": " + row)
# this program produces a string of stars in a loop


