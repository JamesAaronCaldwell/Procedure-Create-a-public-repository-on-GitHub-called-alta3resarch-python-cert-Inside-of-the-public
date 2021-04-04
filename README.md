######################################################################################################
######################################################################################################
                            James Aaron Caldwell - Citigroup - 04/02/2021
This application is to show examples of python functionality learned this week in training. 
Run this from a command line with python3.
Menu has 3 function choices or Q for exiting the application.
1. Pulls from NASA API then format json to Human readable text and saves to json file
2. Is a barchart based on minutes of phone usage comparing teens to parents exports to pdf locally                            
3. Is a guessing game using a while loop and conditionals 
Q or q will exit the application
######################################################################################################
######################################################################################################
Imports used in this application
######################################################################################################
import requests #used for pulling api data
import json #used for formatting api data 
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as mp
import crayons #used for chaning color of text on commandline
import time #used for pausing app for one second so banners can be read
import tablib as tl #used as library (not used in training class) to show another way of exporting to json file

######################################################################################################
######################################################################################################