#Team SICK Software Engineering Final Project
#Hi everyone :D

from flask import Flask, redirect, url_for, render_template, request  #Vital for setting up the websites.

ticketWebsite = Flask(__name__) #Create the website

@ticketWebsite.route("/") #Homepage
def defaultPage():
    return render_template("homepage.html") #Renders the document.

@ticketWebsite.route("/homepage.html") #Actual Homepage
def homePage():
    return render_template("homepage.html") #Renders the document.

@ticketWebsite.route("/signin.html") #Sign In
def signInPage():
    return render_template("signin.html") #Renders the document.

@ticketWebsite.route("/register.html", methods=["POST", "GET"]) #Register, POST is returning the information, GET, well that gets the information
def registerPage():
    if request.method == "POST":
        print("Hey everyone :)")
        # firstName = request.form["firstname"] This code retrieves user data via the name.
        # lastName = request.form["lastname"]
        # userName = request.form["username"]
        # password = request.form["password"]
    else:
        return render_template("register.html") #Renders the document.

@ticketWebsite.route("/recordIT.html") #Record the ticket
def recordITPage():
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