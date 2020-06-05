
from Person import Person
from BloodBank import BloodBank
from datetime import datetime

TYPES = ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"]

def listOfPeople(loc):
    """
    Given a location for a file, return a list of Person 
    objects for each person in the CSV file 
    """
    #pass # TODO: Implement this
    with open("info.data") as openFile: 
        lines = []
        personList = []
        for line in openFile: #loops through all of our positions in info.data

            stringList = line.split("~") #takes the string and splits it at the tilde
            name = stringList[0] #first postion is going to be 0
            address = stringList[2]
            birthday = stringList[4]
            bloodType = stringList[6]
            bloodType = bloodType.strip("\n")  
            if name != "Name":
                personList.append(Person(name, address, birthday, bloodType)) 
    openFile.close()
    return personList
    
  
   # Adrian Perkins~-~Ap #716-5517 Urna. St.~-~10-01-1997~-~AB+
    


def displayBankStats(bbs):
    """
    Displays all the banks and how many units for each type.

    This function can call print instead of returning
    """
    print()
    print("{:=^30}".format(" Blood Banks and Counts "))
    for b in bbs:
        print("Bank: {}".format(b))
        for x in TYPES:
            print("\t Type {:3}: Amount {}".format(x, b.totalUnitsOfBlood(x)))
    print("{:=^30}".format(" End "))
    print()
    

def displayPeopleNotFull(peeps):
    """
    Displays all the people that aren't at the normal number of units
    of blood
    """
    print()
    print("{:=^30}".format(" People != 5500 Units "))
    for p in peeps:
        if p.getBloodCount() != 5500:
            print(p)
    print("{:=^30}".format(" End "))
    print()

def displayPeopleInjured(peeps):
    """
    Displays all people that are injured
    """
    print()
    print("{:=^30}".format(" Is Injured "))
    for p in peeps:
        if p.isInjured():
            print(str(p) + "\t" + str(p.getBloodCount()))
    print("{:=^30}".format(" End "))
    print()


# To generate the data provided, I used the following site:
# https://www.generatedata.com/
def main():
    """
    Test Code

    DO NOT MODIFY
    """     

    # Provided blood banks
    bloodBanks = [
        BloodBank("Red Cross", "Indianapolis"), 
        BloodBank("St. Blood", "Bloomington"),
        BloodBank("Not Vampires", "Chicago"),
        BloodBank("Indiana University", "Bloomington"), 
        BloodBank("Drop it Like it's Hot", "New York")
    ]


    # Reads in the data, and adds each person to a blood bank
    peoples = listOfPeople("Assignment6/info.data")

    # Checks to make sure you are using datetime
    for p in peoples:
        if not isinstance(p.birthday, datetime):
            print("Instance variable birthday is NOT datetime object")
    
    for i in range(len(peoples)):
        bloodBanks[i % len(bloodBanks)].addPerson(peoples[i])
    
    # Each person donates blood based on the index 
    # stored inside of each Blood Bank
    for b in bloodBanks:
        for p in b.users:
            b.receiveBlood(p, b.users.index(p)*10)
            p.resetBloodCount() # Reset the account
    
    # Show people with not perfect blood
    # This case should be empty
    displayPeopleNotFull(peoples)
    
    # Show the bank statement AND how much is each type
    displayBankStats(bloodBanks)

    print("{:=^40}".format("People that can donate to {}".format(TYPES[0])))
    for b in bloodBanks:
        peeps = b.findPeople(TYPES[0])
        print("Count: {}, List: {}".format(len(peeps), peeps))
    print("{:=^40}".format(""))

    displayPeopleInjured(peoples)

    # Time to injury some people
    injured = [5, 56, 22, 98, 19] 
    for i in injured:
        peoples[i].bloodInBody -= (300 + i * 10)
    
    displayPeopleInjured(peoples)


    print("{:=^40}".format("Checking Transfer"))
    for i in range(5):
        p = peoples[injured[i]]
        print("Current Person: {}".format(p.name))
        b = bloodBanks[i]
        result = b.receiveBlood(p)
        if result == -1:
            print("Unable to take blood: '{}' is injured".format(p.name))
        result = b.giveBlood(p, 100)
        if result == -1:
            print("Unable to transfer blood to {}: '{}' does not have enough of type {} ({})".format(p.name, b.name, p.bloodType, b.totalUnitsOfBlood(p.bloodType))) 
        if result == -2:
            print("Unable to transfer blood to {}: would not take blood".format(p.name)) 
        # print(result) #Im not sure why drop it like it hot produces an incorrect result, but I think it has something to do with the entry not considering other bloop types????


        print("'{}' ({}) Status of Injury: {}".format(p.name, p.bloodInBody, p.isInjured()))
        print()
    print("{:=^40}".format(""))

    displayBankStats(bloodBanks)


if __name__ == "__main__":
    main()