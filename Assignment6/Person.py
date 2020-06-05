from datetime import datetime

class Person():

    # https://www.simplifiedpython.net/python-convert-string-to-datetime/
    # Tool to help with date

    def __init__(self, name, address, birthday, bloodType):
        """
        Given a name (string), an address (string), birthday (string), and 
        blood type (string), store the parameters in instance variables as 
        name (string), address (string), birthday (datetime, in the format of month-day-year), 
        and bloodType (string). 

        HINT: Refer to the link above about converting datetime. 
            (You will have to scroll down a little bit for the function name)

        You must keep track of the number of milliliters in the body. 

        You must keep track of if the person is injuried. A person is considered injured 
        if they have less than 5200 ml of blood in the body or has more than 5600 ml in
        the body.

        The bloodInBody is 5500 units when you create a person
        """
        self.name = name
        self.address = address
        self.birthday = datetime.strptime(birthday, "%m-%d-%Y")
        self.bloodType = bloodType
        self.bloodInBody = 5500

        #pass # TODO: Implement this


    
    def getAge(self):
        """
        Returns the number of years the person is. 
        """
        #pass # TODO: Implement this
        #return currentTime - self.birthday
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    
    def isInjured(self):
        """
        Returns a boolean value. 

        True if the person is injured (less than 5200 or more than 5600 ml) (exclusive)
        False if the person is not injured
        """
        #pass # TODO: Implement this
        if self.bloodInBody >= 5200 and self.bloodInBody <= 5600:
            return False
        else:
            return True

    def getBloodCount(self):
        """
        Returns the amount of blood in the person's body
        """
        #pass # TODO: Implement this
        return self.bloodInBody
    
    def transferBlood(self, count):
        """
        For a given amount of blood, transfer a safe amount to the current 
        person or FROM the person. The count for blood can be positive 
        (recieving) and the count for blood can be negative (giving).

        A person is safe if there blood count is 5200 ml to 5600 ml 
            (inclusive on both ends)

        If the provided amount of blood GIVEN (+) to the person is 
        dangerous for the reciever (current person), do 
        not transfer any of it and return -1.

        If the provided amount of blood TAKEN (-) from the person is dangerous for the given), 
        do not take any of the blood and return -1

        Otherwise, complete the transfer and return 0
        """
        #pass # TODO: Implement this
        if self.bloodInBody + count >= 5200 and self.bloodInBody + count <= 5600:
            self.bloodInBody += count #i used += becuase it takes up less space (i need this line to actually do the transfer)
            return 0 #success
        elif self.bloodInBody < 5200 and self.bloodInBody + count <= 5600 and count > 0:
            self.bloodInBody += count
            return 0 #success
        elif self.bloodInBody > 5600 and self.bloodInBody + count >= 5200 and count < 0:
            self.bloodInBody += count
            return 0 #success
        else:
            return -1 #not success
        

    

    def resetBloodCount(self):
        """
        Sets the number of units for blood back to 
        the amount of blood in the body that a body normally has.

        Simulates a person recovering after donating.
        """
        #pass # TODO: Implement this
        self.bloodInBody = 5500 #just setting a value and not returning anything


    def __repr__(self):
        """
        Provided the name, blood type for the user, and blood count.

        NOTE: You do not need to touch this. This is made for you
        """
        return "< " + self.name + " ~ " + self.bloodType  +" ~ " + str(self.bloodInBody) +"ml >"

    def __str__(self):
        """
        Return the name, the age, the blood type, and blood count as follows:

        Larry Bates ~ 19 ~ A- ~ 5500ml
        """
        #pass # TODO: Implement this
        return self.name + " ~ " + str(self.getAge()) + " ~ " + self.bloodType + " ~ " + str(self.bloodInBody) + "ml"



if __name__ == "__main__":
    p = Person("Hello", "from the other", "05-05-1995", "side")
    #pass # Can do some testing without running all the code