from firebase import firebase #import the firebase library, cool!

users = firebase.FirebaseApplication("https://testing-7f9ce-default-rtdb.firebaseio.com/", None) #Connect to the users database
tickets = firebase.FirebaseApplication("https://it-tickets-51e5b-default-rtdb.firebaseio.com/", None) #Connect to the tickets database
entireUserDatabase = users.get("testing-7f9ce-default-rtdb", "") #Get the entire dictionary set
entireTicketDatabase = tickets.get("it-tickets-51e5b-default-rtdb", None)

#This function will add a user to the user database


def addTicket(ticket):
    global entireTicketDatabase
    entireTicketDatabase = tickets.get("it-tickets-51e5b-default-rtdb", None)
    ticketNumber = entireTicketDatabase["-MpSFedLdYbML5FYVBmr"]["ticketNumber"] #The current ticket number, increase by 1 for every new ticket, stored in database?
    ticketString = f"Ticket number {'0' * (4 - len(str(ticketNumber))) + str(ticketNumber)}" #Ensures there's always a leading 0 if needed. Max is 9999 tickets
    print(ticketString)


def addUser(firstName, lastName, username, password):
    global entireUserDatabase
    try: #Try to search the entire dictionary for the user
        for keys in entireUserDatabase:
            if entireUserDatabase[keys]["username"] == username: #Check to see if the name is already taken
                return "username already taken, try again." #Return a message, replace with redirect.
    except TypeError:
        print("Database is empty exception.")

    user = { #Add the user parameters here
        "firstName": firstName,
        "lastName": lastName,
        "username": username,
        "password": password,
        "admin": False
    }  # Example from the IT sign up page

    users.post("testing-7f9ce-default-rtdb", user)  # Add the user to the database
    print("user successfully added")
    entireUserDatabase = users.get("testing-7f9ce-default-rtdb", "")  # Update the dictionary

def getUserIdentifier(username): #Trying to get the username identifier by passing the username as a parameter and going through the dict
    for key in entireUserDatabase: #Go through the dictionary
        if entireUserDatabase[key]["username"] == username: #If the username is equal to a username, then return that key.
            return key

def correctUsernamePassword(username, password):
    for key in entireUserDatabase: #Search the entire database for the user and password
        if entireUserDatabase[key]["username"] == username and entireUserDatabase[key]["password"] == password: #If they match...
            return True #Return true!
    return False #Or not...

def getUserData(keyIdentifier): #Prints out all the info pertaining to someone
    return f"First Name: {entireUserDatabase[keyIdentifier]['firstName']}\n" \
           f"Last Name: {entireUserDatabase[keyIdentifier]['lastName']}\n" \
           f"Username: {entireUserDatabase[keyIdentifier]['username']}\n" \
           f"Password: {entireUserDatabase[keyIdentifier]['password']}\n" \
           f"Admin: {entireUserDatabase[keyIdentifier]['admin']}"


print(addUser("Chris", "Benson", "sick", "12345678"))
addTicket("bob")
# users.put("testing-7f9ce-default-rtdb/-MpNHhO0fNJGv-LHWklS", "firstName", "YOOOOOOOO THIS IS SO COOL") #Changes or adds a value to a data set
# addUser("Chris", "Benson", "sick", "12345678")
# specificName = firebase.get("testing-7f9ce-default-rtdb", "-MpKuhUiRb_3oGDZGn_I") #Get the values in this record


#ticket example
# ticketNumber = 37 #The current ticket number, increase by 1 for every new ticket, stored in database?
# ticketString = f"Ticket number {'0' * (4 - len(str(ticketNumber))) + str(ticketNumber)}" #Ensures there's always a leading 0 if needed. Max is 9999 tickets
# print(ticketString)




