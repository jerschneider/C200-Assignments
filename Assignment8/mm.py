import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    #TODO: Implement function
	#return 1

    for x in range(len(a)):
        for y in range(len(b[0])): ##start iterating at the 0 pos of b with this nested loop (this targets columns)
            for z in range(len(b)): #rows
                aTimesb = a[x][z] * b[z][y]
                return aTimesb

    ##numpy test code
    #axb = np.dot(a, b)
    #return axb



#INPUT scalar n and matrix a
#RETURN scalar product na
def sm(n,a):
    #TODO:Implement function
	#return 1
    for x in range(n):
        for y in range(n):
            return a[x][y]
    ##numpy test code
     #return n * np.array(a)


#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    #TODO:Implement function
	#return 1
    base = []
    for i in range(len(a[0])):  ##I know this loop does the same thing as numpy.zeroes but that function puts in a bunch of extra junk so i just did it myself
        item = []
        for x in range(len(a)):
            item.append(0)
        base.append(item)
    #for i in range(len(a)):
    #    base.append(np.zeros(len(a[1])))
    #print(base)
    for x in range(len(a)): #columns
        for y in range(len(a[0])): #rows
            base[y][x] = a[x][y]
    return base
'''
for a in tp([[12,7],[4 ,5], [3 ,8]]):
    print(a)
'''
    
    
    
    ##numpy test code
    #return np.transpose(a)


#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    #TODO:Implement function
	#return 1
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for y in range(len(a[0])):
            for x in range(len(a)):
                aAddb = a[x][y] + b[x][y]
                return aAddb


if __name__ == "__main__":
    a = np.array([[1,2,4],[3,4,3]])
    b = np.array([[-1,0],[1,-5],[-3,1]])
    print("numpy product\n", np.dot(a,b))
    d = mm(a,b)
    print(d)

    print("numpy scalar product\n", 4*a)
    e = sm(4,a)
    print(e)

    print("numpy tranpose\n", np.transpose(a))
    f = tp(a)
    print(f)

    print("numpy addition\n", a + a)
    g = add_m(a,a)
    print(g)