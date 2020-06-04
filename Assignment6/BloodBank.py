class BloodBank:

    # https://www.disabled-world.com/calculators-charts/blood-chart.php
    # Dontate Blood To table
    DONATE_TO = { 'A+':['A+', 'AB+'], 'O+':['O+', 'A+', 'B+', 'AB+'], 'B+':['B+', 'AB+'], 'AB+':['AB+'], 'A-':['A+', 'A-', 'AB+', 'AB-'], 'O-':['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], 'B-':['B+', 'B-', 'AB+', 'AB-'], 'AB-':['AB+', 'AB-'] 
    } # TODO: FILL IN based on table about compatability 

    DONATE_FROM = { 'A+':['A+', 'A-', 'O+', 'O-'], 'O+':['O+', 'O-'], 'B+':['B+', 'B-', 'O+', 'O-'], 'AB+':['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], 'A-':['A-', 'O-'], 'O-':['O-'], 'B-':['B-', 'O-'], 'AB-':['AB-', 'A-', 'B-', 'O-']
    } # TODO: FILL IN based on table about compatability 


    def __init__(self, name, location):
        """
        Creates an instance of a of a BloodBank

        A blood bank will have a `name`, `location`, a list of `users`, and a bank of blood 
        to keep track of how much of each blood type they have. 

        HINT: You know the types of blood (and no new ones will not be created (hopefully)) 
            and you know a blood bank with start empty. 
        """
        pass # TODO: Implement this
    
    def totalUnitsOfBlood(self, bType=None):
        """
        Returns the total number of units of blood in the bank. 

        Unless specified with a specific type, returns the total for all units. 
        Can be provided a type.

        HINT: bType=None is a default parameter
        """
        pass # TODO: Implement this
    
    def findPeople(self, bType):
        """
        For the given blood type `bType`, return a list of people 
        that have bloods types that `bType` can receive

        Example: A+ can receive from A+, A-, O+, O-
        """
        pass # TODO: Implement this
    
    def addPerson(self, p):
        """
        Adds the given `Person` object to the Bank. 
        Assumes no Person will be given twice 
        (no need to check for repeats)

        This function does not return anything. 
        """
        pass # TODO: Implement this
    
    def giveBlood(self, p, quantity=5):
        """
        If there is not enough blood in the bank to transfer, return -1.

        If you are unable to transferBlood for the given person, return -2. 

        Given that there is enough blood in the bank for the given person (p), 
        transfer the blood to the person (BUT there are things to 
            consider before transfering). 
        Assuming the blood can be GIVEN to the person, subtract the quantity from 
            the bank and return 0. 
        """
        pass # TODO: Implement this
    
    def receiveBlood(self, p, quantity=5):
        """
        Takes blood from the provided person and if you are able to 
        successfully transfer blood from the person, then remove that from the 
        the current banks blood bank. Return 0. 
        (NOTE: you are TAKING blood, so there is something you will need to think about 
            before transfering blood from the person)

        If you are unable to transfer blood from the person, return -1 since you can't add 
        blood the bank if the you can't get blood from the person.
        """
        pass # TODO: Implement this

    
    def registeredUsers(self):
        """
        Returns the number of people registered in this 
        blood bank
        """
        pass # TODO: Implement this

    def __str__(self):
        """
        Returns the name of the bank and the number of 
        registered users

        NOTE: This was given to you, does not need changed
        """
        return self.name + ",Users: " + str(self.registeredUsers()) + ",Blood Total: " + str(self.totalUnitsOfBlood()) 


if __name__ == "__main__":
    testing = BloodBank("Who", "Where")
    pass # Can do some testing without running all the code