class Pizza:
    """
    as a place to enter more details about the class
    """

    # put class variables here for good practice

    def __str__(self): #this one will have only one parameter, self
        """
        TODO: come back and make this function
        """
        #pass
        aString = "Pizza ({0}) with Toppings: {1} and {2} crust"
        return aString.format(self.size, self.toppings, self)

    def __init__(self, size, toppings, crustType):
        """
        Constructor for the class

        parameters:
        -size: numerical value (DIamater of the pizza pie)
        -toppings: a list of strings
        -crustYpe: a string representing the crust type
        """

        self.size = size
        # NOTE: You don't always have to match parameter name to instance variable name
        self.toppingList = toppings.split(",")
        self.crust_type = crustType

        self.allergies = []
        #Note: Not all instance bariales need to be passed in a as a parameter

    #class variables
    sizePrice = {10: 8.00, 12: 10.00, 14: 12.00, 18: 22.00 }


    def getPrice(self):
        """
        Given the size of the pizza and the toppings, determine the price.
        """
        totalPrice = 0
        totalPrice += Pizza.sizePrice[self.size]
    