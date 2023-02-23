#!/bin/bash


 #Script         Ops Challenge: Class 05 - Clearing Logs
 #Purpose        This script prints to the console the file size of the log files before compressions, compresses them to a backup directory, names them with a timestamp, clears the contents of the original log files, prints to the screen the size of the compressed file and compares the size of the compressed files to the original log fiels.
 #Why            Automate log clearing and backup so log file sizes don't get out of hand.

 # Get a timestamp and a backup directory

 echo "\nList of log file sizes before compression:\n"
 ls -lh /var/log/syslog /var/log/wtmp | awk '{print "Log name:" $9 " | Log size:" $5}'

 # Save the original file size in a variable

 original_size_syslog=$(ls -lh /var/log/syslog | awk '{print $5}')
 original_size_wtmp=$(ls -lh /var/log/wtmp | awk '{print $5}')

 # Get a timestamp and a backup directory variable

 timestamp=$(date +"%Y%m%d%H%M%S")
 backupdirectory="./backup"

 # Make a directory using the backupdirectory variable

 mkdir -p $backupdirectory

 # Create a zip file of the syslog and wtmp files

 zip -q "$backupdirectory/syslog_$timestamp" /var/log/syslog
 zip -q "$backupdirectory/wtmp_$timestamp" /var/log/wtmp

 # Clear the contents of the log files

 truncate -s 0 /var/log/syslog
 truncate -s 0 /var/log/wtmp

 # Print the file size after compression

 echo ""
 echo "List of log file sizes after compression:\n"
 ls -lh backup/syslog_$timestamp.zip backup/wtmp_$timestamp.zip | awk '{print "Log name:" $9 " | Log size:" $5}'

 # Compare the file sizes before and after the compression

 echo "__________________________________________________\n\nFile Size Comparison:\n"

 echo "/var/log/syslog: original size $original_size_syslog, compressed size $(ls -lh backup/syslog_$timestamp.zip | awk '{print $5}')"
 echo "/var/log/wtmp: original size $original_size_wtmp, compressed size $(ls -lh backup/wtmp_$timestamp.zip | awk '{print $5}')"