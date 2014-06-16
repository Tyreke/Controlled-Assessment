answer = raw_input("Are You Creating An Entry [Press 1] \nOr Are You Searching An Entry [Press 2] ")

# IF we are creating 

if answer == "1" : 
    #print ("This is where we create")
    # collect information

    lastname = raw_input("What is the persons last name? ")
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What is the persons phone number? ")
    email = raw_input("What is the persons email address? ")
    address = raw_input("What is the persons address? ")
    town = raw_input("What is the persons town? ")
    dateofbirth = raw_input("What is the persons date of birth? ")
    postcode = raw_input("What is the persons postcode? ")
    
    #create or append addressbookdata

    temp1 = open("addressbookdata","a")
    
    #create string to print to file
    #print temp1
    #print (firstname + " " + lastname + ", " + phone + ", " + email + ", " + address + ", " + town + ", " + dateofbirth + ", " + postcode) 

    temp1.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address + ", " + town + ", " + dateofbirth + ", " + postcode)
    temp1.write("\n")

# SEARCHING FOR A RECORD

elif answer == "2" :
    print ("this is where we search")
    searchcriteria = raw_input("Enter your search Criteria. Name, Phone number, Address, Postcode, Town or Date Of Birth ")
    print searchcriteria
    temp1 = open("addressbookdata","r")
    for line in temp1:
        if searchcriteria in line:
            print line
    else:
        print ("no results found")

# USER DID NOT PICK CREATE OR SEARCH 

else :
    print ("Incorrect Answer")
    exit()
