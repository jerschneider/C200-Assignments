#returns a value which is a string
#use this later for Assignment1 to solve the triangle problem-set
a = input("please enter the length of the first side: ")
print("you have entered: " + a) 
#this raises a by the square root
#the issue with this is whatever number I enter becomes entered as a string rather than a integerto solve this: apply float to a
b = float(a) ** 0.5
print("the square root of "+a+" is "+str(b)+"")


