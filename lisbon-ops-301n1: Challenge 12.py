#!/bin/python

#Script         Ops Challenge: Class 12 - Python Requests Library
#Purpose        Create a Python file capable of using requests library to send different method requests to a url specified by the user
#Why            Learn how to use requests library to make requests and get header information.

import requests

# Prompt user for URL and HTTP method
url = input("Enter URL destination: ")
method = input("Enter HTTP Method (GET/POST/PUT/DELETE/HEAD/PATCH/OPTIONS): ")

# Print request and ask for confirmation, exit if answer is not y
print(f"Sending {method} request to {url}")
confirm = input("Would you like to proceed? (y/n): \n")
if confirm.lower() != "y":
    exit() 

# Send HTTP request
response = requests.request(method, url)

# Translate error codes into their descriptions
if response.status_code == 200:
    status = "OK"
elif response.status_code == 400:
    status = "Bad Request"
elif response.status_code == 401:
    status = "Unauthorized"
elif response.status_code == 403:
    status = "Forbidden"
elif response.status_code == 404:
    status = "Not Found"
elif response.status_code == 500:
    status = "Internal Server Error"
else:
    status = "Unknown Status Code"

# Print response header information
print(f"Response Status: {response.status_code} - {status}\n")
print("Response Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")