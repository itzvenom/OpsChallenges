#!/usr/bin/python3

# Script : OpsChallenge31.py - Signature-based Malware Detection Part 1 of 3
# Purpose: The purpose of this script is to search for a specific file in a specified directory and its subdirectories
# Why    : This script can be useful for quickly locating a specific file in a large directory and its subdirectories. 

import os # Import the OS system library
import glob # Import the glob library for file pattern matching

# Prompt the user for the file name and directory to search
file_name = input("Enter the file name to search for: ")
search_dir = input("Enter the directory to search in: ")

# Normalize the directory path by resolving relative path, removing '.' and '..'
search_dir = os.path.normpath(search_dir)

# Build the search pattern by joining the directory path, '**' which means search subdirectories recursively
and the file name to match
search_pattern = os.path.join(search_dir, "**", file_name)

# Perform the recursive glob search and save the matches
matches = glob.glob(search_pattern, recursive=True)

# Print the results
print("\nResults:")
for match in matches:
print(match) # Print each match

# Count the total number of files searched by performing a dummy recursive glob
num_files_searched = sum(1 for _ in glob.iglob(os.path.join(search_dir, "**", "*"), recursive=True))

# Get the number of matches
num_hits_found = len(matches)

# Print number of files searched and hits found
print(f"\n{num_files_searched} files were searched.")
print(f"{num_hits_found} hits were found.") 
