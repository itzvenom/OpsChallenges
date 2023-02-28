#!/bin/python

#Script         Ops Challenge: Class 06 - Bash in Python
#Purpose        Create a python script that executes bash commands, saves them as variables and outputs them to the terminal.
#Why            Learn how to import a module, save bash commands output as a variable and print it to the terminal.

# Import subprocess module that allows us to interact with the system
import subprocess

# Save the output of the whoami command as variable
whoami_variable2 = subprocess.getoutput("whoami")

# Print whoami_variable to terminal
print(whoami_variable2)
print("__________________________________________________________\n")

# Save the output of the ip a command as variable
ip_a_variable2 = subprocess.getoutput("ip a")

# Print ip_a_variable to terminal
print(ip_a_variable2)
print("__________________________________________________________\n")

# Save the output of the lshw -short command as variable
lshw_short_variable2 = subprocess.getoutput("lshw -short")

# Print lshw_short_variable to terminal
print(lshw_short_variable2)

########################################
######### import os script #############
########################################

# Import os module that allows us to interact with the system
# import os

# Save the output of the whoami command as variable
# whoami_variable = os.popen("whoami")

# Print whoami_variable to terminal
# print(whoami_variable)

# Save the output of the ip a command as variable
# ip_a_variable = os.popen("ip a")

# Print ip_a_variable to terminal
# print(ip_a_variable)

# Save the output of the lshw -short command as variable
# lshw_short_variable = os.popen("lshw -short")

# Print lshw_short_variable to terminal
# print(lshw_short_variable)


