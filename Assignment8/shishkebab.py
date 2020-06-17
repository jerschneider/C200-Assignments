
#give the colors that contain fruit
fruit = ["apple", "peas", "corn"]
x = {"red": ["apple", "firetruck"], "blue": ["sky", "ocean"], "green": ["peas"], "yellow":["sun", "corn"]}
q1 = list(map(lambda z : list(filter(lambda y : z in x[y], x.keys())), fruit))
print("q1: {}".format(q1))

#rewrite as lambda/map/filter
s = [2*x+1 for x in range(0,13)]
q2 = list(map(lambda x : 2*x+1, range(0,13)))
print("q2: {}".format(q2))
t = [2*x+1 for x in range(0,13) if x%3]
q3 = list(map(lambda x : 2*x+1, filter(lambda x : x%3, range(0,13))))
print("q3: {}".format(q3))


a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

#match the output
a = []
for i in range(1,9):
    if i%2 == 0:
        a.append(i**2 - i +3)
q4 = [i**2 - i + 3 for i in range(1, 9) if i%2 == 0]
q5 = list(map(lambda i : i**2 - i + 3, filter(lambda i: i%2 == 0, range(1,9))))
print("q4: {}".format(q4))
print("q5: {}".format(q5))

#match the outputs
c1 = []
for n in range(1,16):
    if n%2 == 0:
        c1.append(n**2)
    else:
        c1.append(n**3)
q6 = [n**2 if n%2 == 0 else n**3 for n in range(1,16)]
q7 = list(map(lambda n : n**2 if n%2 == 0 else n**3, range(1,16)))
print("q6: {}".format(q6))
print("q7: {}".format(q7))


#This is technically transpose of a matrix
#But for now, just match output
e1 = [[1,2],[3,4],[5,6],[7,8]]
q8 = [[e1[x][y] for x in range(len(e1))] for y in range(len(e1[0]))]
q9 = list(map(lambda y : list(map(lambda x : e1[x][y], range(len(e1)))), range(len(e1[0]))))
print("q8: {}".format(q8))
print("q9: {}".format(q9))

#reverse the order of letters in the string
f1 = ["hello"]
q10 = [f1[0][len(f1[0]) - x - 1] for x in range(len(f1[0]))]
q11 = list(map(lambda x : f1[0][len(f1[0]) - x - 1], range(len(f1[0]))))
print("q10: {}".format(q10))
print("q11: {}".format(q11))

#reverse the order of letters in each string, preserving the order of the list
g1 = ["hello", "goodbye", "merhaba"]
q12 = [[g1[y][len(g1[y]) - x - 1] for x in range(len(g1[y]))] for y in range(len(g1))]
q13 = list(map(lambda y : list(map(lambda x : g1[y][len(g1[y]) - x - 1], range(len(g1[y])))), range(len(g1))))
print("q12: {}".format(q12))
print("q13: {}".format(q13))
