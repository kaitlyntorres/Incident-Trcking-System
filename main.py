#Team SICK Software Engineering Final Project
#Hi everyone :D

from flask import Flask, redirect, url_for, render_template, request  #Vital for setting up the websites.
from firebase import firebase #Firebase database :D
ticketWebsite = Flask(__name__) #Create the website

users = firebase.FirebaseApplication("https://testing-7f9ce-default-rtdb.firebaseio.com/", None) #Connect to the users database
tickets = firebase.FirebaseApplication("https://it-tickets-51e5b-default-rtdb.firebaseio.com/", None) #Connect to the tickets database
entireUserDatabase = users.get("testing-7f9ce-default-rtdb", "") #Get the entire dictionary set
entireTicketDatabase = tickets.get("it-tickets-51e5b-default-rtdb", None)

#11/27/2021, Let's work on signing up to the database.

#This will get the specified user key to use for identifying and getting username/password
def getUserIdentifier(username): #Trying to get the username identifier by passing the username as a parameter and going through the dict
    global entireUserDatabase
    entireUserDatabase = tickets.get("it-tickets-51e5b-default-rtdb", None)
    for key in entireUserDatabase: #Go through the dictionary
        if entireUserDatabase[key]["username"] == username: #If the username is equal to a username, then return that key.
            return key
    return False

def correctUsernamePassword(username, password):
    for key in entireUserDatabase: #Search the entire database for the user and password
        if entireUserDatabase[key]["username"] == username and entireUserDatabase[key]["password"] == password: #If they match...
            return True #Return true!
    return False #Or not...

#Add user will add a singular user to the database via the registration page.
#Duplicate usernames will not be allowed.
def addUser(firstName, lastName, username, password):
    global entireUserDatabase
    try: #Try to search the entire dictionary for the user
        for keys in entireUserDatabase:
            if entireUserDatabase[keys]["username"] == username: #Check to see if the name is already taken
                return False #Return a message, replace with redirect.
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
    entireUserDatabase = users.get("testing-7f9ce-default-rtdb", "")  # Update the dictionary
    return True

#Add a ticket to the database
def addTicket(firstName, lastName, date, ticketCategory, title, details, occurrenceRate):
    global entireTicketDatabase
    entireTicketDatabase = tickets.get("it-tickets-51e5b-default-rtdb", None)
    ticketNumber = entireTicketDatabase["-MpSFedLdYbML5FYVBmr"]["ticketNumber"] #The current ticket number, increase by 1 for every new ticket, stored in database?
    tickets.put("it-tickets-51e5b-default-rtdb/-MpSFedLdYbML5FYVBmr", "ticketNumber", ticketNumber + 1) #Increase the ticket number by 1
    ticketString = f"Ticket number {'0' * (4 - len(str(ticketNumber))) + str(ticketNumber)}" #Ensures there's always a leading 0 if needed. Max is 9999 tickets
    ticketData = { #Ticket data from the HTML code.
        "ticketNumber": ticketString,
        "firstName": firstName,
        "lastName": lastName,
        "date": date,
        "ticketCategory": ticketCategory,
        "title": title,
        "details": details,
        "occurrenceRate": occurrenceRate
    }
    tickets.post("it-tickets-51e5b-default-rtdb", ticketData) #Add it to the database.
    entireTicketDatabase = tickets.get("it-tickets-51e5b-default-rtdb", None) #Update the entire ticket database.
    return True

@ticketWebsite.route("/") #Homepage
def defaultPage():
    return render_template("homepage.html") #Renders the document.

@ticketWebsite.route("/homepage.html") #Actual Homepage
def homePage():
    return render_template("homepage.html") #Renders the document.

@ticketWebsite.route("/signin.html", methods=["POST", "GET"]) #Sign In, needs POST/GET for retrieving the password
def signInPage():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"] #Get the username and password
        if correctUsernamePassword(username, password): #Correct username/password
            return redirect(url_for("homePage"))
        else: #Incorrect username/password
            return redirect(url_for("signInPage"))
    else:
        return render_template("signin.html") #Renders the document by default.

@ticketWebsite.route("/register.html", methods=["POST", "GET"]) #Register, POST is returning the information, GET, well that gets the information
def registerPage():
    if request.method == "POST":
        print("Hey everyone :)")
        firstName = request.form["firstname"] #This code retrieves user data via the firstname.
        lastName = request.form["lastname"] #This code retrieves user data via the lastname.
        userName = request.form["username"] #This code retrieves user data via the username.
        password = request.form["password"] #This code retrieves user data via the password.
        success = addUser(firstName, lastName, userName, password)
        if success:
            return redirect(url_for("signInPage")) #Send the user to the register page to sign in
        else:
            return redirect(url_for("registerPage")) #If registration fails, refresh the page.
    else:
        return render_template("register.html") #Renders the document.

@ticketWebsite.route("/recordIT.html", methods=["POST", "GET"]) #Record the ticket
def recordITPage():
    if request.method == "POST": #After submitting the data
        firstName = request.form["firstname"]
        lastName = request.form["lastname"]
        date = request.form["date"]
        category = request.form["category"]
        title = request.form["title"]
        details = request.form["notes"]
        occurrenceRate = request.form["occurrence"]
        success = addTicket(firstName, lastName, date, category, title, details, occurrenceRate) #Add the ticket
        if success:
            return redirect(url_for("homePage"))
    else:
        return render_template("recordIT.html") #Renders the document.

@ticketWebsite.route("/editticket.html") #Edit the ticket
def editTicketPage():
    return render_template("editticket.html") #Renders the document.

@ticketWebsite.route("/viewreports.html") #view the reports
def viewReportsPage():
    return render_template("viewreports.html") #Renders the document.

@ticketWebsite.route("/viewtickets.html") #view the tickets
def viewTicketsPage():
    return render_template("viewtickets.html") #Renders the document.


if __name__ == "__main__": #Main python file
    ticketWebsite.run() #Start the website
