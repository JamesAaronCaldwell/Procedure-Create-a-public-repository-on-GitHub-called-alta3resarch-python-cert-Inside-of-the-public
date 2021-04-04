#! /usr/bin/python3

##############################################################################
"""This is a script by James Aaron Caldwell is for demonstrating the
basic understanding of python scripting language through 3 examples.
See README.md for more details"""
##############################################################################

# Import examples using standard library and other formatting libs
import requests #used for pulling api data
import json #used for formatting api data 
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as mp
import crayons #used for chaning color of text on commandline
import time #used for pausing app for one second so banners can be read
import tablib as tl #used as library (not used in training class) to show another way of exporting to json file


# global variable example
API = "http://www.neowsapp.com/rest/v1/neo/2216523?api_key=7cqHW801kCstlBsbcprRwwe01awpGk7XVVamgD0d"  # API with my key

##############################################################################
# Make func to Nasa API request to https://api.nasa.gov and 
# display some portion of the data returned in an easily read format
##############################################################################
def nasa():
    r = requests.get(API)
    # Kills app if API is down
    if r.status_code != 200:
        print("Error with API connection, try again later.")
        exit()
    print(json.dumps(r.json(), indent = 1)) #print formatted json 
    #User provides filename for json output file.
    filename = input(crayons.yellow("\nWhat is the name of the file?  ")) +".json"
    outFile = open(filename, "a") #open file with append
    #format readable and use tablib library for example of using other libs not used in class.
    tl.json = json.dumps(r.json(), indent = 1) 
    #append data to file
    print(tl.json, file=outFile)
    outFile.close() #closing file out
    print("File "+filename+" has been created in folder local to application.") #confirming end of function

##############################################################################    
#Use matplotlib for graphed data and save chart to pdf file
##############################################################################
def graph(): #need to customize to make unique
    
    N = 4
    teensPhonetime = (55, 65, 30, 35) # length of time on phone (mins) - Teens
    parentsPhonetime = (25, 32, 34, 20) # length of time on phone (min) - Parents
    ran = np.arange(N)    # the x locations for the groups
    # the barWidth of the bars
    barWidth = 0.22

    # describe where to display p1
    p1 = mp.bar(ran, teensPhonetime, barWidth)
    # stack p2 on top of p1
    p2 = mp.bar(ran, parentsPhonetime, barWidth, bottom=teensPhonetime)

    # Describe the table metadata
    mp.ylabel("Time on the phone (mins)")
    mp.title("PhoneUsage.pdf")
    mp.xticks(ran, ("Q1", "Q2", "Q3", "Q4"))
    mp.yticks(np.arange(0, 81, 10))
    mp.legend((p1[0], p2[0]), ("Teens", "Parents"))

    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    mp.savefig("2018summary.pdf")


##############################################################################
#uses panda to read excel and print to command line screen.
##############################################################################
def readExcel():
    
    phonecalls = pd.read_excel('example1.xlsx')
    print(phonecalls.head())  

##############################################################################
#    * Write a guessing game that uses the crayons library 
#   to post in green YOU WIN when the correct answer is supplied
##############################################################################
def guess():
    round = 0
    answer = " "
    while round < 3 and answer != "Purple":
        round += 1     # increase the round counter by 1
        answer = input(crayons.blue('What is your favorite color? : '))
        if answer == "Purple": # logic to check if user gave correct answer
            print(crayons.green("You Win!!!"))
        elif round == 3:    # logic to ensure round has not yet reached 3
            print(crayons.yellow("Sorry, the answer was Purple."))
        else:                 # if answer was wrong
            print(crayons.yellow("Sorry. Try again!"))

##############################################################################
#This is to be used as a break in commandline output to show start and end
# of each example within this application.
##############################################################################
def banner(words):
    print(crayons.blue("******************************************************"))
    print(crayons.blue("******************************************************"))
    print(crayons.red("             "+words+"                         "))
    print(crayons.blue("******************************************************"))
    print(crayons.blue("******************************************************\n\n\n"))
    time.sleep(1)

##############################################################################
# Main will ask for user input to choose what app will run
# One choice is Nasa API with json file output
# One choice is Color example with Guessing Game
# One choice is graph with static data to dataform and graph
##############################################################################
def main():
    banner("Welcome to my Python examples!")
    answer=""
    while answer != "Q" or "q":
        answer = input(crayons.yellow("Please enter 1, 2, 3 or 4 to run a function.\n To Quit enter q or Q:"))
        if answer == "1":
            banner("Starting NASA API Call...")
            nasa()
            answer = ""
            banner("NASA API Call Complete...")
        elif answer == "2":
            banner("Graphing Example...")
            graph()
            answer = ""
            banner("Graphing Example Complete...")
        elif answer == "3":
            banner("Guessing Game Example...")
            guess()
            answer = ""
            banner("Guessing Game Example Complete...")
        elif answer == "4":
            banner("Read Excel Example...")
            readExcel()
            answer = ""
            banner("Read Excel Example Complete...")
        elif answer == "Q" or answer == "q":
            print(crayons.green("Thanks for playing!!!"))
            banner("James Aaron Caldwell Citigroup...")
            exit()
        else: 
            answer = input(crayons.yellow("Bad entry!\nPlease enter 1, 2 or 3 to run a function.\nTo Quit enter q or Q:"))
            if answer == "Q" or "q":
                print(crayons.green("Thanks for playing!!!"))
                banner("James Aaron Caldwell Citigroup...")
                exit() 

if __name__ == "__main__":
    main()