#! /usr/bin/python3
"""This is a script by James Aaron Caldwell to demonstrate basic understanding of python scripting language"""

# Import examples using standard library
import requests
import json
import pandas as pd
import matplotlib
import crayons
import time

# global
API = "http://www.neowsapp.com/rest/v1/neo/2216523?api_key=7cqHW801kCstlBsbcprRwwe01awpGk7XVVamgD0d"  # API with my key


# Make func to Nasa API request to https://api.nasa.gov and 
#    * Use pandas to create a dataframe, and export some data into a format of your choice
#    display some portion of the data returned in an easily read format
def nasa():
    #counter = 0
    r = requests.get(API)
    # Kills app if API is down
    if r.status_code != 200:
        print("Error with API connection, try again later.")
        exit()
    
    print(json.dumps(r.json(), indent = 1)) #print formatted json 


#Use matplotlib for graphed data
def graph():
    print("Graph!")

#    * Write a guessing game that uses the crayons library 
#   to post in green YOU WIN when the correct answer is supplied
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


def banner(words):
    print(crayons.blue("******************************************************"))
    print(crayons.blue("******************************************************"))
    print(crayons.red("             "+words +"                         "))
    print(crayons.blue("******************************************************"))
    print(crayons.blue("******************************************************"))
    time.sleep(1)
# Main will ask for user input to choose what app will run
# One choice is Nasa API
# One choice is Color example

def main():
    banner("Starting NASA API Call...")
    nasa()
    banner("Graphing Example...")
    graph()
    banner("Guessing Game Example...")
    guess()
    banner("James Aaron Caldwell Citigroup...")

if __name__ == "__main__":
    main()