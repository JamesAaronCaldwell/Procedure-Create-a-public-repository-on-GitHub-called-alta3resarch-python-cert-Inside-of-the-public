#! /usr/bin/python3
"""This is a script by James Aaron Caldwell to demonstrate basic understanding of python scripting language"""


#Import examples using standard library 
import requests


#Make an API request to https://api.nasa.gov and display some portion of the data returned in an easily read format
API = "https://api.nasa.gov/planetary/apod?api_key=7cqHW801kCstlBsbcprRwwe01awpGk7XVVamgD0d"

#Use matplotlib to produce a graph



#Write a guessing game that uses the crayons library to post in green YOU WIN when the correct answer is supplied


#Use pandas to create a dataframe, and export some data into a format of your choice


#Anything else you find interesting!


# max number of pictures to DL
NUMTODL = 10

def main():
        counter = 0
        r = requests.get(API)

        # we want to grab the data off the 200 response
        nasadata = r.json()

        # loop across all the dictionaries within the list called "photos"
        for pic in nasadata.get("photos"):
           
            # increase the counter by 1
            counter += 1
            # we want to snag the value mapped to photos."pic".img_src
            # print(pic.get("img_src"))
            linktodownload = pic.get("img_src")

            # download the image
            imgdl = requests.get(linktodownload)
            # grab name of image
            imgNm = linktodownload.split("/")[-1]

            # show which image is about to be downloaded
            print(f"Downloading Image #{counter}: {imgNm}")

            # open the file we want to write our image to
            with open(f"/home/student/static/{imgNm}", 'wb') as f:
                # write the image
                f.write(imgdl.content)
        
            # if counter reaches the max number of photos to download
            # exit the loop (break)
            if counter == NUMTODL:
                break

if __name__ == "__main__":
    main()


