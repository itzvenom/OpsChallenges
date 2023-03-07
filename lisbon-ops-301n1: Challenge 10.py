#!/bin/python


#Script         Ops Challenge: Class 10 - Python File Handling
#Purpose        Create a Python file capable of opening and manipulating an existing file.
#Why            Learn how to use Python’s file handling capabilities to open and manipulate an existing file.

# Import the os library
import os

# Pass the code to open and writeto the variable filename
filename = open("teste.txt", "w")

# Write the 3 lines to the file
filename.write("This is line 1\n")
filename.write("This is line 2\n")
filename.write("This is line 3\n")

# Close the file because you need to close the file before trying to read from it.
filename.close()

# Save all the text inside the teste.txt file to the variable contents
contents = open("teste.txt", "r")

# Use the readline function to read the first file of the file and assign it to the variable first_line and print it to the terminal
first_line = contents.readline()
print(first_line)

# Deletes the text file
os.remove('teste.txt')












