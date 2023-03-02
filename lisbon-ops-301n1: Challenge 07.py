#!/bin/python


#Script         Ops Challenge: Class 07 - Directory Creation
#Purpose        Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
#Why            Learn how a for loop and os.walk works as well as writing to a file and opening it with an application.

import os

# Ask the user for a directory path
directory_path = input("Enter a directory path: ")

# Open a file for writing
output_file = open("file_tree.txt", "w")

# Walk through the directory and its subdirectories and write the results to the file
for dirpath, dirnames, filenames in os.walk(directory_path):
    output_file.write(f"Directory: {dirpath}\n")

    # Write the names of the subdirectories to the file
    for dirname in dirnames:
        output_file.write(f"\tSubdirectory: {dirname}\n")

    # Write the names of the files in the directory to the file
    for filename in filenames:
        output_file.write(f"\tFile: {filename}\n")

# Close the file
output_file.close()

# Open the file in Libre Office Writer
os.system("libreoffice --writer file_tree.txt")
