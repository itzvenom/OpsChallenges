#!/bin/bash/


#Script         Ops Challenge: Class 03 - File Permissions
#Purpose        This script prompts users for input of directory and permissions, changes the permissions of the directory according to user input, prints directory contens and permissions settings and outputs a log file.
#Why            Keep improving Bash writing skills and introduce Linux permissions to the knowledge base

# Warning message
echo "Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS. Please proceed with caution!"

# Read user input and story it in a variable
read -p "Which directory path would you like to change permissions? " directory

# Read user input for permissions and store it in a variable
read -p "Please enter the permissions wanted using octal number (example 777): " permissions

# Change directory to directory path provided by user
cd "$directory"

# Change the permission of all files by using it recurvisely
chmod -R "$permissions" *

# Prints to the screen the directory contents
ls -l

# Prints to the screen the new permissions settings
echo "New permissions: $permissions"

# Output a log file of all actions that were taken by the script
timestamp=$(date +"%Y-%m-%d_%H:%M:%S")
log_file="permissions_changed_$timestamp.log"
echo "Log file: $log_file"
echo "Directory path: $directory" > "$log_file"
echo "Permissions: $permissions" >> "$log_file"
echo "Files changed:" >> "$log_file"
ls -l >> "$log_file"
