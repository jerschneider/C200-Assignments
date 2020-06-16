#give the colors that contain fruit
fruit = ["apple", "peas", "corn"]
x = {"red": ["apple", "firetruck"], "blue": ["sky", "ocean"], "green": ["peas"], "yellow":["sun", "corn"]}
q1 = 

#TODO: List Comprehension


#rewrite as lambda/map/filter
s = [2*x+1 for x in range(0,13)]
q2 = #TODO: lambda/map/filter
t = [2*x+1 for x in range(0,13) if x%3]
q3 = #TODO: lambda/map/filter


#match the output
a = []
for i in range(1,9):
    if i%2 == 0:
        a.append(i**2 - i +3)
q4 = #TODO: List Comprehension
q5 = #TODO: lambda/map/filter


#match the outputs
c1 = []
for n in range(1,16):
    if n%2 == 0:
        c1.append(n**2)
    else:
        c1.append(n**3)
q6 = #TODO: List Comprehension
q7 = #TODO: lambda/map/filter


#This is technically transpose of a matrix
#But for now, just match output
e1 = [[1,2],[3,4],[5,6],[7,8]]
q8 = #TODO: List Comprehension
q9 = #TODO: lambda/map/filter

#reverse the order of letters in the string
f1 = ["hello"]
q10 = #TODO: List Comprehension
q11 = #TODO: lambda/map/filter

#reverse the order of letters in each string, preserving the order of the list
g1 = ["hello", "goodbye", "merhaba"]
q12 = #TODO: List Comprehension
q13 = #TODO: lambda/map/filter
