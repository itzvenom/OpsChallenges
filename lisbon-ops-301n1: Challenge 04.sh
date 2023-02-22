#!/bin/bash


 #Script         Ops Challenge: Class 04 - Conditionals in Menu Systems
 #Purpose        This script prompts users to choose a number from a menu, then evaluates the input and runs commands based on it.
 #Why            Introduce bash conditional statements


  # Creating while true loop so it always stays in the menu

while true; do
  # Displays the menu options
  echo "Menu:"
  echo "1. Hello world"
  echo "2. Ping self"
  echo "3. IP info"
  echo "4. Exit"

  # Prompts user input and stores that input into a variable named option
  echo "Choose the option number:"
  read option
  # Evaluates user input from the step above, converts it to a string and checks which option was chose so it can act accordingly # Blank echos for  clarity
  case "$option" in
    "1")
      echo ""
      echo "Hello world!"
      echo ""
      ;;
    "2")
      echo ""
      ping -c 4 127.0.0.1
      echo ""
      ;;
    "3")
      echo ""
      ifconfig
      echo ""
      ;;
    "4")
      echo ""
      echo "Exiting program."
      exit 0
      ;;
    *) #Anything other than 1, 2, 3 or 4
      echo ""
      echo "Invalid option. Please choose a number between 1 and 4."
      echo ""
      sleep 3
      ;;
  esac
done



