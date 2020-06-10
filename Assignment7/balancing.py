#checking and determing parentheses
#must use stacks

class Stack:
     def __init__(self):
         self.items = []

     def empty(self): #checks to see if stack is empty
         return self.items == []

     def push(self, item): #adds item to stack
         self.items.append(item)

     def pop(self): #removes item from the top of stack
         return self.items.pop()

     def peek(self): #checks the top item of the stack
         return self.items[len(self.items)-1]

     def size(self):#returns the size of the stack
         return len(self.items)

endparen = [")", "]", "}"]
parenlist = [")", "]", "}", "(", "[", "{"]
parendict = {"(":")", "[":"]", "{":"}"}
def balancing(paren):
    parenstack = Stack()
    while len(paren) > 0:
        if paren[0] in parenlist: #if its not a type of bracket (like a or string) then it ignores it
            if paren[0] in endparen:
                if parenstack.empty(): #if the string starts with an end bracket then no can it be valid
                    return False
                if paren[0] == parendict[parenstack.peek()] : #checks to see if there is a valid start bracket on the top of the stack
                    #print("pop")
                    parenstack.pop()
                    paren = paren[1:] #shortens the string by 1 ('pops' the first character in the string)
                else:
                    return False
            else:
                #print(paren[0])
                #print("push")
                parenstack.push(paren[0]) #if its a start bracket then this pushes it to the top
                paren = paren[1:]
        else:
            paren = paren[1:]
    #print(parenstack.items)
    if parenstack.empty():
        return True
    else:
        return False





#Example output from problem
print("1 ", balancing("a(a(a(a(")) # Output: False
print("2 ", balancing("()()()()()((())())")) # Output: True
print("3 ", balancing("((()))")) # Output: True
print("4 ", balancing("({}({)}")) # Output: False
print("5 ", balancing("[[[]]]()(){)")) # Output: False
print("6 ", balancing("")) # Output: True
print("7 ", balancing("def function(p1, p2)")) # Output: True
print("8 ", balancing("public int main(int argc, char[] argv) {(}")) # Output: False
print("9 ", balancing("[1, [1, [2],[3, 4], 5]]]")) # Output: False
