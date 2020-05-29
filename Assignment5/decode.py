# DO NOT MODIFY THE FOLLOWING DICTIONARY
ASCII_VALUES = {i: chr(i) for i in range(32, 126)}
"""
You don't need to understand HOW the dictionary was made (we will 
cover that later in the class) 

All you need to understand what the **keys** and the **values**
represent. There might be a link in the Assignment document
pointing to something that helps
"""
ASCII_VALUES[9] = "\t" # Tab Character
ASCII_VALUES[10] = "\n" # New Line Character



def read_file(file_name):
    """
    INPUT: a file name
    OUTPUT: A list of strings (not a single string) where each string is  #does this mean '1' because that's what i'm assuming
    a number

    Hint
    ---
    1. Open the file
    2. Read the File (Hint: you may need .split() and/or .replace())
    3. Close the File
    4. Return its contents
    """
    # TODO: complete the function
    #pass
    with open(file_name) as openFile: 
        lines = []
        for line in openFile:
            lines.append(line)
    openFile.close()
    return lines

def convert(list_of_codes):
    """
    INPUT: a list of ascii codes (in the form 
            of strings in a list)
    OUTPUT: a string with message in it
    """
    # TODO: convert message using dictionary above (ASCII_VALUES)
    #       If you are unsure about the dictionary, try printing it
    #pass
    messages = []
    for line in list_of_codes:
        lineMessage = []
        for num in line:
            value = ASCII_VALUES.get(num, "")
            lineMessage.append(value)
        messages.append(lineMessage)
    print(messages)
    



def write_file(file_name, message):
    """
    INPUT: a file name, a string of text
    OUPUT: None. But the file should be created in the folder

    Does not need to explicitly return anything. 
    """
    # TODO: write to the new file
    pass


def extraCredit(something):
    """
    EXTRA CREDIT

    This function is not required for full credit. 

    Have the message signed with your name instead of 
    what is the last line of the file.

    Remember, it is a string, so it is immutable.
    """




if __name__ == "__main__":
    file_content = read_file("Assignment5/code.txt") # Do not change the path

    message = convert(file_content)

    write_file("Assignment5/message.txt", message) # Do not change the path

    # Extra Credit:
    # Sign the message with your name instead of Camisa ()
    # Put the code in `extraCredit` function. It will
    # take in one parameter and you have to determine if 
    # it returns something