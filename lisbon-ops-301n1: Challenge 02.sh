#!/bin/bash/


#Script         Ops Challenge: Class 02 - Append; Date and Time
#Purpose        This script copies the /var/log/journal to the current working directory, appends the current date and time to the copied filename as well as echoing statements on what is happening along with a simple verification check.
#Why            Learn how to create a bash script, practice how to write a simple script and learn how to use VC Code.

# Outputting to terminal that the script has started
echo "Starting Script..."

# Echoing what the script is doing as well as getting the current date and time into a variable.
echo "Getting Current Timestamp..."

timestamp=$(date "+%Y-%m-%d_%H:%M:%S")

# Echoing what the script is doing as well as copying the journal to the current directory with an appended timestamp to the filename with error verification if the cp command was successful or not.
echo "Copying journal to current directory..."
if cp -r /var/log/journal ./journal_$timestamp; then
    echo "/var/log/journal successfully copied to the current working directory."
else
    echo "/var/log/journal was not successfully copied, the script is not working properly."
fi

