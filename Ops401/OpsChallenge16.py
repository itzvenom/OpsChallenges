#!/usr/bin/python3

# Script : OpsChallenge16.py
# Purpose: Iterates through a wordlist and either prints words line by line or detects if input word by user is present.
# Why    : To better understand the types of automation employed by adversaries.

import time

def menu():
# Prompt user to select a mode
    mode = int(input('Select a mode (1 or 2): '))

# Offensive mode 
    if mode == 1: 
    # Accept file path and open file 
        word_list = input('Enter file path of word list: ')
        file = open(word_list, 'r', encoding='iso-8859-1')

        # Iterate through word list and print each word with a delay 
        for word in file:
         print(word.strip())
         time.sleep(0.5) # Add 0.5 second delay
        
# Defensive mode
    elif mode == 2:
        # Accept input string and file path
        string = input('Enter input string: ')
        word_list = input('Enter file path of word list: ')

        # Open file and check if string appears
        with open(word_list, 'r', encoding='iso-8859-1') as file:
            words = file.readlines()
            found = False
            for word in words:
                if string == word.strip():
                    found = True
                    break

        # Print result
        if found:
            print(f'{string} was found in the word list.')
        else:
            print(f'{string} was not found in the word list.')
            
    # Invalid mode 
    else: 
        print('Invalid mode selected. Please select 1 or 2.')
    
if __name__ == "__main__":
    menu()
