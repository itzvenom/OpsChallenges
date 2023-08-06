#!/usr/bin/python3

# Script : OpsChallenge44 - Create a Port Scanner
# Purpose: Scan a host to check if a specific TCP port is open
# Why    : Determine open ports on a specific target

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # Set timeout to 5 seconds
sockmod.settimeout(timeout)

hostip = input("Enter host IP: ")
portno = int(input("Enter port number: "))

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:  
        print("Port open")
    else:
        print("Port closed")

portScanner(portno)
